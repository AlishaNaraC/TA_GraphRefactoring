from neo4j import GraphDatabase
from config import NEO4J_CONFIG

class PropertyBecomingNode:

    def __init__(self):
        self.driver = GraphDatabase.driver(**NEO4J_CONFIG)
        self.database = NEO4J_CONFIG.get("database")

    def close(self):
        self.driver.close()

    def execute_query(self, query):
        with self.driver.session(database=self.database) as session:
            return list(session.run(query))

    def refactor_properties(self, properties):

        for prop in properties:

            relation = f"HAS_{prop.upper()}"
            label = prop.capitalize()

            query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL

            WITH n,n.{prop} AS value

            MERGE (p:{label} {{value:value}})

            MERGE (n)-[:{relation}]->(p)

            REMOVE n.{prop}
            """

            print(f"PBN refactoring property: {prop}")

            self.execute_query(query)