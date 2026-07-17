from refactor.label_utils import generate_labels

class LabelSpecification:
    def __init__(self, importer, kandidat_properti, label_configs, limit=None):
        self.importer = importer
        self.kandidat_properti = kandidat_properti
        self.limit = limit
        self.label_configs = label_configs

    def execute(self):
        for prop in self.kandidat_properti:
            config = self.label_configs[prop]
            prefix = config.get('prefix', "")
            
            print(f"\nRefactoring {prop} dengan label prefix: '{prefix}'...")
            
            limit_clause = f"LIMIT {self.limit}" if self.limit else ""
            query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL
            RETURN id(n) as id, n.{prop} as value
            {limit_clause}
            """
            rows = self.importer.run_query(query)
            total = 0
            
            for row in rows:
                node_id = row["id"]
                value = row["value"]
                
                labels = generate_labels(value, prefix=prefix)
                
                for label in labels:
                    add_label_query = """
                    MATCH (n)
                    WHERE id(n) = $node_id
                    CALL apoc.create.addLabels(n, [$label])
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
            print(f"{total} node selesai untuk properti {prop}")
