from neo4j import GraphDatabase
from config import NEO4J_CONFIG

class EdgeSpecification:

    def __init__(self):
        self.driver = GraphDatabase.driver(**NEO4J_CONFIG)
        self.database = NEO4J_CONFIG.get("database")

    def close(self):
        self.driver.close()

    def execute_query(self, query):
        with self.driver.session(database=self.database) as session:
            return list(session.run(query))

    def specialize_relationships(self, rel_type, properties):

        for prop in properties:

            query = f"""
            MATCH (a)-[r:{rel_type}]->(b)
            WHERE b.{prop} IS NOT NULL

            WITH a,b,r,toUpper(toString(b.{prop})) AS val

            CALL apoc.create.relationship(
                a,
                '{rel_type}_{prop.upper()}_' + val,
                properties(r),
                b
            )
            YIELD rel

            DELETE r
            """

            print(f"ES refactoring property: {prop}")

            self.execute_query(query)