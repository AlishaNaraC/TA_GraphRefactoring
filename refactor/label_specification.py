from refactor.kandidat_properti import KANDIDAT_PROPERTI
from refactor.label_utils import generate_labels


class LabelSpecification:
    def __init__(self, importer, kandidat_properti, limit=100):
        self.importer = importer
        self.kandidat_properti = kandidat_properti
        self.limit = limit

    def execute(self):
        for prop in self.kandidat_properti:
            print(f"\nRefactoring {prop} property...")
            limit_clause = f"LIMIT {self.limit}" if self.limit else ""
            query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL

            RETURN
                id(n) as id,
                n.{prop} as value
                {limit_clause}
            """
            rows = self.importer.run_query(query)
            total = 0
            for row in rows:
                node_id = row["id"]
                value = row["value"]
                labels = generate_labels(prop, value)
                for label in labels:
                    add_label_query = """
                    MATCH (n)
                    WHERE id(n) = $node_id

                    CALL apoc.create.addLabels(
                        n,
                        [$label]
                    )
                    YIELD node

                    RETURN count(*)
                    """
                    self.importer.run_query(add_label_query, {"node_id": node_id, "label": label})
                remove_query = f"""
                MATCH (n)
                WHERE id(n) = $node_id

                REMOVE n.{prop}
                """
                self.importer.run_query(remove_query, {"node_id": node_id})
                total += 1
            print(f"{total} node selesai")