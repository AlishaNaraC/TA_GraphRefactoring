from refactor.label_utils import (generate_labels)


class PropertyBecomingNode:
     def __init__(self, importer, kandidat_properti, nama_relasi_baru, limit=100):
        self.importer = importer
        self.kandidat_properti = kandidat_properti
        self.nama_relasi_baru = nama_relasi_baru
        self.limit = limit

     def execute(self):
        for prop in self.kandidat_properti:
            rel_name = self.nama_relasi_baru[prop]
            print(f"\nRefactoring {prop} property with new relationship {rel_name}...")
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
                labels = generate_labels(prop, value, pbn=True)

                for label in labels:
                    create_query = """
                    MATCH (n)
                    WHERE id(n)=$node_id

                    CALL apoc.merge.node([$label], {value: $label})
                    YIELD node

                    CALL apoc.merge.relationship(n,$rel,{},{},target,{})
                    YIELD rel

                    RETURN count(*)
                    """
                    self.importer.run_query(
                        create_query,
                        {
                            "node_id": node_id,
                            "label": label,
                            "rel": rel_name
                        }
                    )

                remove_query = f"""
                MATCH (n)
                WHERE id(n)=$node_id

                REMOVE n.{prop}
                """
                self.importer.run_query(
                    remove_query,
                    {"node_id": node_id}
                )
                total += 1

            print(f"{total} node selesai")
