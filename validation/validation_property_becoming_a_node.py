import os
import csv
import json
from importer.neo4j_importer import Neo4jImporter

JSON_PATH = "data/report/validation/baseline_property_stats.json"

# Mapping properti -> relasi baru
PROPERTY_RELATION = {
    "category": "HAS_CATEGORY",
    "year":     "RELEASED_IN",
    "birth":    "BORN_IN",
    "death":    "DIED_IN",
}

# Prefix label baru untuk year/death/birth
YEAR_PREFIX = "year_"


class PropertyBecomingNodeValidator:

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
    def get_relation_counts(self, relation: str) -> list:
        """Ambil jumlah relasi per label target untuk satu tipe relasi."""
        query = f"""
            MATCH ()-[r:{relation}]->(target)
            RETURN labels(target)[0] AS label, count(r) AS jumlah
            ORDER BY jumlah DESC
        """
        result = self.importer.execute_query(query)
        return [(r["label"], r["jumlah"]) for r in result]

    def get_combined_relation_counts(self) -> list:
        """Ambil jumlah relasi gabungan RELEASED_IN+BORN_IN+DIED_IN per label target."""
        query = """
            MATCH ()-[r:RELEASED_IN|BORN_IN|DIED_IN]->(target)
            RETURN labels(target)[0] AS label, count(r) AS jumlah
            ORDER BY jumlah DESC
        """
        result = self.importer.execute_query(query)
        return [(r["label"], r["jumlah"]) for r in result]

    def get_total_new_labels(self) -> int:
        """Hitung total label baru yang terbentuk dari semua refaktorisasi."""
        query = """
            MATCH ()-[:HAS_CATEGORY|RELEASED_IN|BORN_IN|DIED_IN]->(target)
            RETURN count(DISTINCT labels(target)[0]) AS total
        """
        result = self.importer.execute_query(query)
        return result[0]["total"] if result else 0

    def get_total_new_relations(self) -> int:
        """Hitung total semua relasi baru yang terbentuk."""
        query = """
            MATCH ()-[r:HAS_CATEGORY|RELEASED_IN|BORN_IN|DIED_IN]->()
            RETURN count(r) AS total
        """
        result = self.importer.execute_query(query)
        return result[0]["total"] if result else 0

    # ------------------------------------------------------------------
    # Simpan CSV
    # ------------------------------------------------------------------
    def save_csv(self, baseline: dict, refactored: dict, output_dir: str = "data/report/validation"):
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "validasi_property_becoming_node.csv")

        # ── Siapkan data ringkasan ──────────────────────────────────────
        # Baseline
        total_unique_baseline = (baseline["summaries"]["category"]["unique_value"] + baseline["gabungan"]["unique_value"])
        total_node_category   = baseline["summaries"]["category"]["jumlah_node"]
        total_node_year       = baseline["summaries"]["year"]["jumlah_node"]
        total_node_birth      = baseline["summaries"]["birth"]["jumlah_node"]
        total_node_death      = baseline["summaries"]["death"]["jumlah_node"]
        total_node_baseline   = (
            total_node_category +
            baseline["gabungan"]["jumlah_node"]
        )

        # Refactored
        total_label_baru      = refactored["total_label_baru"]
        total_rel_category    = refactored["total_rel"]["category"]
        total_rel_year        = refactored["total_rel"]["year"]
        total_rel_birth       = refactored["total_rel"]["birth"]
        total_rel_death       = refactored["total_rel"]["death"]
        total_relation_baru   = refactored["total_relation_baru"]

        # ── Siapkan data detail ─────────────────────────────────────────
        # Baseline value_counts per properti (dict untuk lookup)
        bl_category = {str(v): c for v, c in baseline["value_counts"]["category"]}
        bl_year     = {str(v): c for v, c in baseline["value_counts"]["year"]}
        bl_birth    = {str(v): c for v, c in baseline["value_counts"]["birth"]}
        bl_death    = {str(v): c for v, c in baseline["value_counts"]["death"]}
        bl_gabungan = {str(v): c for v, c in baseline["value_counts_gabungan"]}

        # Refactored relation_counts per properti (dict untuk lookup)
        rf_category = {label: c for label, c in refactored["relation_counts"]["category"]}
        rf_year     = {label: c for label, c in refactored["relation_counts"]["year"]}
        rf_birth    = {label: c for label, c in refactored["relation_counts"]["birth"]}
        rf_death    = {label: c for label, c in refactored["relation_counts"]["death"]}
        rf_gabungan = {label: c for label, c in refactored["relation_counts"]["gabungan"]}

        # Urutan nilai dari baseline (pakai urutan baseline)
        cat_values     = [str(v) for v, _ in baseline["value_counts"]["category"]]
        year_values    = [str(v) for v, _ in baseline["value_counts"]["year"]]
        birth_values   = [str(v) for v, _ in baseline["value_counts"]["birth"]]
        death_values   = [str(v) for v, _ in baseline["value_counts"]["death"]]
        gabungan_values = [str(v) for v, _ in baseline["value_counts_gabungan"]]

        max_rows = max(
            len(cat_values), len(year_values),
            len(birth_values), len(death_values),
            len(gabungan_values)
        )

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")

            # ── Baris header validasi ───────────────────────────────────
            writer.writerow(["", "", "", "", "validasi"])

            # ── Ringkasan ───────────────────────────────────────────────
            writer.writerow([
                "total unique value baseline", total_unique_baseline,
                "total label baru", total_label_baru,
                total_unique_baseline == total_label_baru,
            ])
            writer.writerow([
                "total node category", total_node_category,
                "total relationship has_category", total_rel_category,
                total_node_category == total_rel_category,
            ])
            writer.writerow([
                "total node year", total_node_year,
                "total relationship released_in", total_rel_year,
                total_node_year == total_rel_year,
            ])
            writer.writerow([
                "total node birth", total_node_birth,
                "total relationship born_in", total_rel_birth,
                total_node_birth == total_rel_birth,
            ])
            writer.writerow([
                "total node death", total_node_death,
                "total relationship died_in", total_rel_death,
                total_node_death == total_rel_death,
            ])
            writer.writerow([
                "total node baseline", total_node_baseline,
                "total relationship baru", total_relation_baru,
                total_node_baseline == total_relation_baru,
            ])

            writer.writerow([])

            # ── Header tabel detail ─────────────────────────────────────
            writer.writerow([
                "category type", "jumlah category type", "nama label baru", "jumlah relationship", "validasi", "",
                "year type", "jumlah year type", "nama label baru", "jumlah relationship", "validasi", "",
                "birth type", "jumlah birth type", "nama label baru", "jumlah relationship", "validasi", "",
                "death type", "jumlah death type", "nama label baru", "jumlah relationship", "validasi", "",
                "year,death,birth type", "Jumlah year,death,birth type", "jumlah relationship", "validasi",
            ])

            # ── Baris detail ────────────────────────────────────────────
            for i in range(max_rows):
                row = []

                # Category
                if i < len(cat_values):
                    val         = cat_values[i]
                    bl_count    = bl_category.get(val, 0)
                    label_baru  = val                          # label = nilai itu sendiri
                    rf_count    = rf_category.get(label_baru, 0)
                    match       = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Year
                if i < len(year_values):
                    val         = year_values[i]
                    bl_count    = bl_year.get(val, 0)
                    label_baru  = f"{YEAR_PREFIX}{val}"
                    rf_count    = rf_year.get(label_baru, 0)
                    match       = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Birth
                if i < len(birth_values):
                    val         = birth_values[i]
                    bl_count    = bl_birth.get(val, 0)
                    label_baru  = f"{YEAR_PREFIX}{val}"
                    rf_count    = rf_birth.get(label_baru, 0)
                    match       = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Death
                if i < len(death_values):
                    val         = death_values[i]
                    bl_count    = bl_death.get(val, 0)
                    label_baru  = f"{YEAR_PREFIX}{val}"
                    rf_count    = rf_death.get(label_baru, 0)
                    match       = bl_count == rf_count
                    row += [val, bl_count, label_baru, rf_count, match, ""]
                else:
                    row += ["", "", "", "", "", ""]

                # Gabungan year+death+birth
                if i < len(gabungan_values):
                    val        = gabungan_values[i]
                    bl_count   = bl_gabungan.get(val, 0)
                    label_baru = f"{YEAR_PREFIX}{val}"
                    rf_count   = rf_gabungan.get(label_baru, 0)
                    match      = bl_count == rf_count
                    row += [val, bl_count, rf_count, match]
                else:
                    row += ["", "", "", ""]

                writer.writerow(row)

        print(f"\nHasil validasi disimpan ke: {path}")
        return path

    # ------------------------------------------------------------------
    # Main
    # ------------------------------------------------------------------
    def run(self, output_dir: str = "data/report/validation"):
        print("=" * 55)
        print("  VALIDASI: Property Becoming a Node")
        print("=" * 55)

        # 1. Load baseline dari JSON
        print("\nMemuat data baseline dari JSON...")
        baseline = self.load_baseline()

        # 2. Query Neo4j untuk data refactored
        print("Membaca data refactored dari Neo4j...")

        print("  - HAS_CATEGORY...")
        rc_category = self.get_relation_counts("HAS_CATEGORY")
        print("  - RELEASED_IN...")
        rc_year     = self.get_relation_counts("RELEASED_IN")
        print("  - BORN_IN...")
        rc_birth    = self.get_relation_counts("BORN_IN")
        print("  - DIED_IN...")
        rc_death    = self.get_relation_counts("DIED_IN")
        print("  - Gabungan RELEASED_IN|BORN_IN|DIED_IN...")
        rc_gabungan = self.get_combined_relation_counts()
        print("  - Total label baru...")
        total_label_baru    = self.get_total_new_labels()
        print("  - Total relasi baru...")
        total_relation_baru = self.get_total_new_relations()

        refactored = {
            "total_label_baru":    total_label_baru,
            "total_relation_baru": total_relation_baru,
            "total_rel": {
                "category": sum(c for _, c in rc_category),
                "year":     sum(c for _, c in rc_year),
                "birth":    sum(c for _, c in rc_birth),
                "death":    sum(c for _, c in rc_death),
            },
            "relation_counts": {
                "category": rc_category,
                "year":     rc_year,
                "birth":    rc_birth,
                "death":    rc_death,
                "gabungan": rc_gabungan,
            },
        }

        # 3. Simpan CSV
        self.save_csv(baseline, refactored, output_dir)

        # 4. Print ringkasan ke terminal
        print("\n── Ringkasan Validasi ──")
        checks = [
            ("total unique value baseline", baseline["summaries"]["category"]["unique_value"] + baseline["gabungan"]["unique_value"], "total label baru", total_label_baru),
            ("total node category",         baseline["summaries"]["category"]["jumlah_node"], "total rel HAS_CATEGORY", refactored["total_rel"]["category"]),
            ("total node year",             baseline["summaries"]["year"]["jumlah_node"],     "total rel RELEASED_IN",  refactored["total_rel"]["year"]),
            ("total node birth",            baseline["summaries"]["birth"]["jumlah_node"],    "total rel BORN_IN",      refactored["total_rel"]["birth"]),
            ("total node death",            baseline["summaries"]["death"]["jumlah_node"],    "total rel DIED_IN",      refactored["total_rel"]["death"]),
        ]
        all_passed = True
        for label_bl, val_bl, label_rf, val_rf in checks:
            match = val_bl == val_rf
            icon  = "✅" if match else "❌"
            print(f"  {icon} {label_bl}: {val_bl:,} | {label_rf}: {val_rf:,}")
            if not match:
                all_passed = False

        print()
        if all_passed:
            print("  ✅ Refaktorisasi Property Becoming a Node berhasil!")
        else:
            print("  ❌ Ada ketidakcocokan — cek CSV untuk detail.")
        print("=" * 55)

        self.close()


def run_validation_property_becoming_node():
    validator = PropertyBecomingNodeValidator()
    validator.run()