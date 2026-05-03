from neo4j import GraphDatabase
from config import *

class DBCloner:

    def __init__(self):
        self.driver = GraphDatabase.driver(**NEO4J_CONFIG)
        self.database = NEO4J_CONFIG.get("database")

    def close(self):
        self.driver.close()

    def run_system_query(self, query):
        with self.driver.session(database="system") as session:
            return list(session.run(query))

    def clone_database(self, source_db, target_db):
        self.run_system_query(f"DROP DATABASE {target_db} IF EXISTS")
        self.run_system_query(f"CREATE DATABASE {target_db} AS COPY OF {source_db}")