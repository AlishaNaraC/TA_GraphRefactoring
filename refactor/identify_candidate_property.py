class IdentifyCandidateProperty:
    DVR_THRESHOLD = 1.0  # dalam persen
    DEFAULT_EXCLUDE = []  # unique identifier, bukan kandidat refaktorisasi

    def __init__(self, importer):
        self.importer = importer

    def get_property_keys(self):
        query = "CALL db.propertyKeys() YIELD propertyKey RETURN propertyKey"
        rows = self.importer.run_query(query)
        return [row["propertyKey"] for row in rows]

    def calculate_dvr(self, prop):
        query = f"""
        MATCH (n)
        WHERE n.{prop} IS NOT NULL
        RETURN count(DISTINCT n.{prop}) AS distinct_count, count(n.{prop}) AS total_count
        """
        result = self.importer.run_query(query)[0]
        distinct_count = result["distinct_count"]
        total_count = result["total_count"]
        if total_count == 0:
            return None
        return {
            "property": prop,
            "distinct": distinct_count,
            "total": total_count,
            "dvr_percent": (distinct_count / total_count) * 100
        }

    def analyze(self, exclude=None):
        """Mengembalikan detail DVR seluruh properti."""
        exclude = exclude or self.DEFAULT_EXCLUDE
        results = []
        for prop in self.get_property_keys():
            if prop in exclude:
                continue
            stats = self.calculate_dvr(prop)
            if stats:
                results.append(stats)
        return results

    def execute(self, exclude=None):
        """Mengembalikan array nama properti dengan DVR < threshold (kandidat refaktorisasi)."""
        results = self.analyze(exclude=exclude)
        kandidat = [r["property"] for r in results if r["dvr_percent"] < self.DVR_THRESHOLD]
        return kandidat


if __name__ == "__main__":
    from importer.neo4j_importer import Neo4jImporter

    importer = Neo4jImporter()
    identifier = IdentifyCandidateProperty(importer)

    print("=== Detail DVR Seluruh Properti ===")
    detail = identifier.analyze()
    for r in sorted(detail, key=lambda x: x["dvr_percent"]):
        kategori = "low cardinality" if r["dvr_percent"] < IdentifyCandidateProperty.DVR_THRESHOLD else "high cardinality"
        print(f"{r['property']:20s} | distinct={r['distinct']:>10} | total={r['total']:>10} | DVR={r['dvr_percent']:.6f}% | {kategori}")

    print("\n=== Kandidat Properti (DVR < 1%) ===")
    kandidat = identifier.execute()
    print(kandidat)

    importer.close()