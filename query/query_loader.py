from pathlib import Path

class QueryLoader:

    def __init__(self, query_folder):
        self.query_folder = Path(query_folder)

    def load_queries(self):
        queries = []

        for file in self.query_folder.glob("*.txt"):
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()

                for index, line in enumerate(lines):
                    query = line.strip()

                    if query:
                        queries.append({
                            "filename": file.name,
                            "query_id": index + 1,
                            "query": query
                        })

        return queries