from pathlib import Path

class QueryLoader:

    def __init__(self, query_path):
        self.query_path = Path(query_path)

    def load_queries(self):
        queries = []

        if self.query_path.is_file():
            files = [self.query_path]
        else:
            files = list(self.query_path.glob("*.txt"))

        for file in files:
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