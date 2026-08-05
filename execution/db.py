import threading

from neo4j import GraphDatabase
from config import NEO4J_CONFIG, DB


def total_db_hits(profile):
    """Rekursif jumlahkan semua dbHits dari tiap operator"""
    total = profile.get("dbHits", 0)
    for child in profile.get("children", []):
        total += total_db_hits(child)
    return total


class DBConnection:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_CONFIG["uri"],
            auth=(NEO4J_CONFIG["user"], NEO4J_CONFIG["password"])
        )
        self.db = DB

    def close(self):
        self.driver.close()

    def run_profile(self, query, timeout_sec=600):
        result_container = {}
        error_container  = {}

        def execute():
            try:
                with self.driver.session(database=self.db) as session:
                    result = session.run(f"PROFILE {query}")

                    # Kumpulkan semua records dulu sebelum consume()
                    records = list(result)
                    jumlah_hasil = records[0][0] if records else 0

                    # Baru consume() — summary.profile sekarang terisi lengkap
                    summary  = result.consume()
                    db_hits  = total_db_hits(summary.profile)
                    run_time = summary.result_available_after + summary.result_consumed_after

                    result_container["data"] = {
                        "jumlah_hasil": jumlah_hasil,
                        "db_hits":      db_hits,
                        "run_time":     run_time
                    }
            except Exception as e:
                error_container["error"] = str(e)

        thread = threading.Thread(target=execute)
        thread.start()
        thread.join(timeout=timeout_sec)

        if thread.is_alive():
            raise TimeoutError(f"Query timeout setelah {timeout_sec} detik")

        if "error" in error_container:
            raise Exception(error_container["error"])

        return result_container["data"]
