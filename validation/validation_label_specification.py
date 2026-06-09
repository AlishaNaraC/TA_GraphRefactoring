import os
import csv
import json
from importer.neo4j_importer import Neo4jImporter

JSON_PATH  = "data/report/validation/baseline_property_stats.json"
YEAR_PREFIX  = "year_"
BIRTH_PREFIX = "birth_"
DEATH_PREFIX = "death_"


class LabelSpecificationValidator:

    def __init__(self):
        self.importer = Neo4jImporter()

    def close(self):
        self.importer.close()

    # ------------------------------------------------------------------
    # Load baseline dari JSON
    # ------------------------------------------------------------------
    def load_baseline(self) -> dict:
        if not os.path.exists(JSON_PATH):
            raise FileNotFoundError(
                f"File baseline tidak ditemukan: {JSON_PATH}\n"
                "Jalankan dulu opsi 'Baca statistik baseline'."
            )
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    # ------------------------------------------------------------------
    # Query Neo4j refactored
    # ------------------------------------------------------------------
    def get_new_labels_by_prefix(self, prefix: str) -> list:
        query = f"""
            CALL db.labels() YIELD label
            WHERE label STARTS WITH '{prefix}'
            RETURN collect(label) AS labels
        """

        result = self.importer.execute_query(query)

        return result[0]["labels"] if result else []

    def get_new_labels_category(
        self,
        baseline: dict
    ) -> list:
        """Ambil label category dari nilai distinct baseline."""
        return [
            str(v)
            for v, _ in baseline["value_counts"]["category"]
        ]

    def get_node_count_with_label(
        self,
        label: str
    ) -> int:

        query = f"""
            MATCH (n)
            WHERE '{label}' IN labels(n)
            RETURN count(n) AS total
        """

        result = self.importer.execute_query(query)

        return result[0]["total"] if result else 0

    def get_remaining_property_count(
        self,
        prop: str
    ) -> int:

        query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL
            RETURN count(n) AS total
        """

        result = self.importer.execute_query(query)

        return result[0]["total"] if result else 0
    
    def get_label_node_counts_bulk(
        self,
        prefix: str
    ) -> dict:

        empty_dict = "{}"

        query = f"""
            CALL db.labels() YIELD label
            WHERE label STARTS WITH '{prefix}'
            CALL apoc.cypher.run(
                'MATCH (n:`' + label + '`) 
                RETURN count(n) AS total',
                {empty_dict}
            ) YIELD value
            RETURN label, value.total AS total
        """

        result = self.importer.execute_query(query)

        return {r["label"]: r["total"] for r in result}


    def get_label_node_counts_category(
        self,
        labels: list
    ) -> dict:

        labels_str = "[" + ", ".join(
            f"'{l}'" for l in labels
        ) + "]"

        empty_dict = "{}"

        query = f"""
            UNWIND {labels_str} AS label
            CALL apoc.cypher.run(
                'MATCH (n:`' + label + '`) 
                RETURN count(n) AS total',
                {empty_dict}
            ) YIELD value
            RETURN label, value.total AS total
        """

        result = self.importer.execute_query(query)

        return {r["label"]: r["total"] for r in result}

    # ------------------------------------------------------------------
    # Simpan CSV
    # ------------------------------------------------------------------
    def save_csv(
        self,
        baseline: dict,
        refactored: dict,
        output_dir: str = "data/report/validation"
    ):
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(
            output_dir,
            "validasi_label_specification.csv"
        )

        # ── Siapkan data ringkasan ──────────────────────────────────
        total_unique_baseline = (
            baseline["summaries"]["category"]["unique_value"] +
            baseline["summaries"]["year"]["unique_value"] +
            baseline["summaries"]["birth"]["unique_value"] +
            baseline["summaries"]["death"]["unique_value"]
        )
        total_node_category = baseline["summaries"]["category"]["jumlah_node"]
        total_node_year     = baseline["summaries"]["year"]["jumlah_node"]
        total_node_birth    = baseline["summaries"]["birth"]["jumlah_node"]
        total_node_death    = baseline["summaries"]["death"]["jumlah_node"]

        total_label_baru  = refactored["total_label_baru"]
        total_node_rf_cat = refactored["total_node"]["category"]
        total_node_rf_year  = refactored["total_node"]["year"]
        total_node_rf_birth = refactored["total_node"]["birth"]
        total_node_rf_death = refactored["total_node"]["death"]
        sisa_category       = refactored["sisa_properti"]["category"]
        sisa_year           = refactored["sisa_properti"]["year"]
        sisa_birth          = refactored["sisa_properti"]["birth"]
        sisa_death          = refactored["sisa_properti"]["death"]

        # ── Siapkan data detail ─────────────────────────────────────
        bl_category = {
            str(v): c
            for v, c in baseline["value_counts"]["category"]
        }
        bl_year  = {
            str(v): c
            for v, c in baseline["value_counts"]["year"]
        }
        bl_birth = {
            str(v): c
            for v, c in baseline["value_counts"]["birth"]
        }
        bl_death = {
            str(v): c
            for v, c in baseline["value_counts"]["death"]
        }

        rf_category = refactored["label_node_counts"]["category"]
        rf_year     = refactored["label_node_counts"]["year"]
        rf_birth    = refactored["label_node_counts"]["birth"]
        rf_death    = refactored["label_node_counts"]["death"]

        cat_values   = [str(v) for v, _ in baseline["value_counts"]["category"]]
        year_values  = [str(v) for v, _ in baseline["value_counts"]["year"]]
        birth_values = [str(v) for v, _ in baseline["value_counts"]["birth"]]
        death_values = [str(v) for v, _ in baseline["value_counts"]["death"]]

        max_rows = max(
            len(cat_values), len(year_values),
            len(birth_values), len(death_values)
        )

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")

            # ── Header validasi ─────────────────────────────────────
            writer.writerow(["", "", "", "", "validasi"])

            # ── Ringkasan ───────────────────────────────────────────
            writer.writerow([
                "total unique value baseline",
                total_unique_baseline,
                "total label baru",
                total_label_baru,
                total_unique_baseline == total_label_baru,
            ])
            writer.writerow([
                "total node category (baseline)",
                total_node_category,
                "total node dengan label baru (category)",
                total_node_rf_cat,
                total_node_category == total_node_rf_cat,
            ])
            writer.writerow([
                "total node year (baseline)",
                total_node_year,
                "total node dengan label baru (year)",
                total_node_rf_year,
                total_node_year == total_node_rf_year,
            ])
            writer.writerow([
                "total node birth (baseline)",
                total_node_birth,
                "total node dengan label baru (birth)",
                total_node_rf_birth,
                total_node_birth == total_node_rf_birth,
            ])
            writer.writerow([
                "total node death (baseline)",
                total_node_death,
                "total node dengan label baru (death)",
                total_node_rf_death,
                total_node_death == total_node_rf_death,
            ])
            writer.writerow([
                "sisa properti category",
                sisa_category,
                "sisa properti year",
                sisa_year,
                "",
            ])
            writer.writerow([
                "sisa properti birth",
                sisa_birth,
                "sisa properti death",
                sisa_death,
                "",
            ])

            writer.writerow([])

            # ── Header tabel detail ─────────────────────────────────
            writer.writerow([
                "category type", "jumlah node baseline",
                "nama label baru", "jumlah node refactored", "validasi", "",
                "year type", "jumlah node baseline",
                "nama label baru", "jumlah node refactored", "validasi", "",
                "birth type", "jumlah node baseline",
                "nama label baru", "jumlah node refactored", "validasi", "",
                "death type", "jumlah node baseline",
                "nama label baru", "jumlah node refactored", "validasi",
            ])

            # ── Baris detail ────────────────────────────────────────
            for i in range(max_rows):
                row = []

                # Category
                if i < len(cat_values):
                    val        = cat_values[i]
                    bl_count   = bl_category.get(val, 0)
                    label_baru = val
                    rf_count   = rf_category.get(label_baru, 0)
                    match      = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Year
                if i < len(year_values):
                    val        = year_values[i]
                    bl_count   = bl_year.get(val, 0)
                    label_baru = f"{YEAR_PREFIX}{val}"
                    rf_count   = rf_year.get(label_baru, 0)
                    match      = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Birth
                if i < len(birth_values):
                    val        = birth_values[i]
                    bl_count   = bl_birth.get(val, 0)
                    label_baru = f"{BIRTH_PREFIX}{val}"
                    rf_count   = rf_birth.get(label_baru, 0)
                    match      = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Death
                if i < len(death_values):
                    val        = death_values[i]
                    bl_count   = bl_death.get(val, 0)
                    label_baru = f"{DEATH_PREFIX}{val}"
                    rf_count   = rf_death.get(label_baru, 0)
                    match      = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match]
                else:
                    row += ["", "", "", "", ""]

                writer.writerow(row)

        print(f"\nHasil validasi disimpan ke: {path}")
        return path

    # ------------------------------------------------------------------
    # Main
    # ------------------------------------------------------------------
    def run(
        self,
        output_dir: str = "data/report/validation"
    ):
        print("=" * 55)
        print("  VALIDASI: Label Specification")
        print("=" * 55)

        # 1. Load baseline
        print("\nMemuat data baseline dari JSON...")
        baseline = self.load_baseline()

        # 2. Ambil label baru dari Neo4j
        print("Membaca label baru dari Neo4j...")

        print("  - Label category...")
        labels_category = self.get_new_labels_category(baseline)

        print("  - Label year (year_)...")
        labels_year = self.get_new_labels_by_prefix(YEAR_PREFIX)

        print("  - Label birth (birth_)...")
        labels_birth = self.get_new_labels_by_prefix(BIRTH_PREFIX)

        print("  - Label death (death_)...")
        labels_death = self.get_new_labels_by_prefix(DEATH_PREFIX)

        total_label_baru = (
            len(labels_category) +
            len(labels_year) +
            len(labels_birth) +
            len(labels_death)
        )

        # 3. Hitung node per label
        print("  - Menghitung node per label category...")
        lnc_category = self.get_label_node_counts_category(labels_category)

        print("  - Menghitung node per label year...")
        lnc_year  = self.get_label_node_counts_bulk(YEAR_PREFIX)

        print("  - Menghitung node per label birth...")
        lnc_birth = self.get_label_node_counts_bulk(BIRTH_PREFIX)

        print("  - Menghitung node per label death...")
        lnc_death = self.get_label_node_counts_bulk(DEATH_PREFIX)


        # 4. Hitung total node dengan label baru per properti
        print("  - Menghitung total node per properti...")
        total_node_cat   = sum(lnc_category.values())
        total_node_year  = sum(lnc_year.values())
        total_node_birth = sum(lnc_birth.values())
        total_node_death = sum(lnc_death.values())

        # 5. Hitung sisa properti
        print("  - Mengecek sisa properti...")
        sisa = {
            prop: self.get_remaining_property_count(prop)
            for prop in ["category", "year", "birth", "death"]
        }

        refactored = {
            "total_label_baru": total_label_baru,
            "total_node": {
                "category": total_node_cat,
                "year":     total_node_year,
                "birth":    total_node_birth,
                "death":    total_node_death,
            },
            "sisa_properti": sisa,
            "label_node_counts": {
                "category": lnc_category,
                "year":     lnc_year,
                "birth":    lnc_birth,
                "death":    lnc_death,
            },
        }

        # 6. Simpan CSV
        self.save_csv(baseline, refactored, output_dir)

        # 7. Print ringkasan ke terminal
        print("\n── Ringkasan Validasi ──")

        total_unique_baseline = (
            baseline["summaries"]["category"]["unique_value"] +
            baseline["summaries"]["year"]["unique_value"] +
            baseline["summaries"]["birth"]["unique_value"] +
            baseline["summaries"]["death"]["unique_value"]
        )

        checks = [
            (
                "total unique value baseline",
                total_unique_baseline,
                "total label baru",
                total_label_baru
            ),
            (
                "total node category (baseline)",
                baseline["summaries"]["category"]["jumlah_node"],
                "total node label baru (category)",
                total_node_cat
            ),
            (
                "total node year (baseline)",
                baseline["summaries"]["year"]["jumlah_node"],
                "total node label baru (year)",
                total_node_year
            ),
            (
                "total node birth (baseline)",
                baseline["summaries"]["birth"]["jumlah_node"],
                "total node label baru (birth)",
                total_node_birth
            ),
            (
                "total node death (baseline)",
                baseline["summaries"]["death"]["jumlah_node"],
                "total node label baru (death)",
                total_node_death
            ),
        ]

        all_passed = True

        for label_bl, val_bl, label_rf, val_rf in checks:
            match = val_bl == val_rf
            icon  = "✅" if match else "❌"
            print(
                f"  {icon} {label_bl}: {val_bl:,} | "
                f"{label_rf}: {val_rf:,}"
            )
            if not match:
                all_passed = False

        # cek sisa properti
        print("\n── Validasi Properti Terhapus ──")
        for prop, sisa_count in sisa.items():
            icon = "✅" if sisa_count == 0 else "❌"
            print(
                f"  {icon} sisa properti {prop}: "
                f"{sisa_count:,}"
            )
            if sisa_count != 0:
                all_passed = False

        print()
        if all_passed:
            print(
                "  ✅ Refaktorisasi Label Specification berhasil!"
            )
        else:
            print(
                "  ❌ Ada ketidakcocokan — cek CSV untuk detail."
            )
        print("=" * 55)

        self.close()


def run_validation_label_specification():
    validator = LabelSpecificationValidator()
    validator.run()