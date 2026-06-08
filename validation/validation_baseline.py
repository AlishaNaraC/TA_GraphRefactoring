import os
import csv
import json
from importer.neo4j_importer import Neo4jImporter

PROPERTIES = ["category", "year", "birth", "death"]


class BaselineStatsReader:

    def __init__(self):
        self.importer = Neo4jImporter()

    def close(self):
        self.importer.close()

    def get_summary(self, prop: str) -> dict:
        query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL
            RETURN
                count(n)                 AS jumlah_node,
                count(DISTINCT n.{prop}) AS unique_value
        """
        result = self.importer.execute_query(query)
        if result:
            return {
                "jumlah_node":  result[0]["jumlah_node"],
                "unique_value": result[0]["unique_value"],
            }
        return {"jumlah_node": 0, "unique_value": 0}

    def get_value_counts(self, prop: str) -> list:
        query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL
            RETURN n.{prop} AS value, count(n) AS jumlah
            ORDER BY jumlah DESC
        """
        result = self.importer.execute_query(query)
        return [(r["value"], r["jumlah"]) for r in result]

    def get_combined_year_stats(self) -> dict:
        """
        Scan sekali semua node yang punya year/death/birth,
        kumpulkan nilainya jadi list, unwind, lalu group by nilai.
        """
        query = """
            MATCH (n)
            WHERE n.year IS NOT NULL OR n.death IS NOT NULL OR n.birth IS NOT NULL
            WITH
                CASE WHEN n.year  IS NOT NULL THEN [n.year]  ELSE [] END +
                CASE WHEN n.death IS NOT NULL THEN [n.death] ELSE [] END +
                CASE WHEN n.birth IS NOT NULL THEN [n.birth] ELSE [] END AS vals
            UNWIND vals AS val
            RETURN val AS tahun, count(*) AS jumlah
            ORDER BY jumlah DESC
        """
        result = self.importer.execute_query(query)
        value_counts = [(r["tahun"], r["jumlah"]) for r in result]

        unique_value = len(value_counts)
        jumlah_node  = sum(c for _, c in value_counts)

        return {
            "unique_value": unique_value,
            "jumlah_node":  jumlah_node,
            "value_counts": value_counts,
        }

    def collect(self) -> dict:
        summaries    = {}
        value_counts = {}

        for prop in PROPERTIES:
            print(f"  Membaca properti '{prop}'...")
            summaries[prop]    = self.get_summary(prop)
            value_counts[prop] = self.get_value_counts(prop)

        print("  Membaca gabungan (year, birth, death)...")
        combined_year = self.get_combined_year_stats()

        return {
            "summaries":     summaries,
            "value_counts":  value_counts,
            "combined_year": combined_year,
        }

    # ------------------------------------------------------------------
    # Simpan CSV
    # ------------------------------------------------------------------
    def save_csv(self, data: dict, output_dir: str = "data/report/validation"):
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "baseline_property_stats.csv")

        summaries    = data["summaries"]
        value_counts = data["value_counts"]
        combined     = data["combined_year"]

        max_rows = max(
            max(len(value_counts[p]) for p in PROPERTIES),
            len(combined["value_counts"])
        )

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")

            # ── Tabel 1: Ringkasan ──────────────────────────────────────
            writer.writerow(["Jenis property", "Jumlah node", "Unique Value"])
            for prop in PROPERTIES:
                s = summaries[prop]
                writer.writerow([prop, s["jumlah_node"], s["unique_value"]])
            writer.writerow([
                "gabungan (year,birth,death)",
                combined["jumlah_node"],
                combined["unique_value"],
            ])

            writer.writerow([])

            # ── Tabel 2 + Tabel 3 berdampingan ─────────────────────────
            header = []
            for prop in PROPERTIES:
                header += [f"{prop} type", f"jumlah {prop} type", ""]
            header += ["Gabungan properti year, death, Birth", "Jumlah node gabungan"]
            writer.writerow(header)

            for i in range(max_rows):
                row = []
                for prop in PROPERTIES:
                    vc = value_counts[prop]
                    if i < len(vc):
                        row += [vc[i][0], vc[i][1], ""]
                    else:
                        row += ["", "", ""]
                cvc = combined["value_counts"]
                if i < len(cvc):
                    row += [cvc[i][0], cvc[i][1]]
                else:
                    row += ["", ""]
                writer.writerow(row)

        print(f"CSV disimpan ke: {path}")
        return path

    # ------------------------------------------------------------------
    # Simpan JSON
    # ------------------------------------------------------------------
    def save_json(self, data: dict, output_dir: str = "data/report/validation"):
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "baseline_property_stats.json")

        # Konversi tuple ke list agar JSON serializable
        json_data = {
            "summaries": {
                prop: data["summaries"][prop]
                for prop in PROPERTIES
            },
            "gabungan": {
                "jumlah_node":  data["combined_year"]["jumlah_node"],
                "unique_value": data["combined_year"]["unique_value"],
            },
            "value_counts": {
                prop: [[v, c] for v, c in data["value_counts"][prop]]
                for prop in PROPERTIES
            },
            "value_counts_gabungan": [
                [v, c] for v, c in data["combined_year"]["value_counts"]
            ],
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        print(f"JSON disimpan ke: {path}")
        return path

    # ------------------------------------------------------------------
    # Main
    # ------------------------------------------------------------------
    def run(self, output_dir: str = "data/report/validation"):
        print("=" * 50)
        print("  MEMBACA STATISTIK BASELINE")
        print("=" * 50)

        data = self.collect()

        print("\n── Ringkasan ──")
        print(f"{'Properti':<30} {'Jumlah Node':>15} {'Unique Value':>14}")
        print("-" * 62)
        for prop in PROPERTIES:
            s = data["summaries"][prop]
            print(f"{prop:<30} {s['jumlah_node']:>15,} {s['unique_value']:>14,}")
        cy = data["combined_year"]
        print(f"{'gabungan (year,birth,death)':<30} {cy['jumlah_node']:>15,} {cy['unique_value']:>14,}")

        self.save_csv(data, output_dir)
        self.save_json(data, output_dir)
        self.close()
        return data


def run_baseline_stats():
    reader = BaselineStatsReader()
    reader.run()