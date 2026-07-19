from refactor.label_utils import (generate_labels)

# Fungsi untuk melakukan refaktorisasi properti becoming a node
class PropertyBecomingNode:
     def __init__(self, importer, kandidat_properti, pbn_configs, limit=None):
        self.importer = importer
        self.kandidat_properti = kandidat_properti
        self.pbn_configs = pbn_configs
        self.limit = limit

     def execute(self):
        for prop in self.kandidat_properti:
            config = self.pbn_configs[prop]
            rel_name = config["rel"]
            prefix = config["prefix"]

            print(f"\nRefactoring '{prop}' property with new relationship '{rel_name}' and label prefix '{prefix}'...")
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
                
                labels = generate_labels(value, prefix=prefix)

                for label in labels:
                    create_query = """
                    MATCH (n)
                    WHERE id(n)=$node_id

                    CALL apoc.merge.node([$label], {value: $label})
                    YIELD node 

                    CALL apoc.merge.relationship(n, $rel, {}, {}, node, {})
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
