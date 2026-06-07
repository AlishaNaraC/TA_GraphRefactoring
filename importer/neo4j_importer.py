from neo4j import GraphDatabase
from config import NEO4J_CONFIG


class Neo4jImporter:

    def __init__(self):
        # Gunakan parameter yang benar untuk GraphDatabase.driver
        uri = NEO4J_CONFIG["uri"]
        user = NEO4J_CONFIG["user"]
        password = NEO4J_CONFIG["password"]
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        from config import DB
        self.database = DB  # default database dari config.py

    def close(self):
        self.driver.close()

    def execute_query(self,query):
        with self.driver.session(
            database=self.database
        ) as session:
            result = session.run(query)
            return list(result)
    
    def run_query(self,query,parameters=None):
        with self.driver.session(
            database=self.database
        ) as session:
            result = session.run(query,parameters)
            return list(result)

    def import_movies(self):
        query = """
        LOAD CSV WITH HEADERS
        FROM 'file:///movies.csv'
        AS row

        FIELDTERMINATOR ','

        WITH row
        WHERE row.id IS NOT NULL

        CALL (row) {
            CREATE (n:TMP_MOVIES)

            SET n += {
                id: row.id,
                category: row.category,
                year: toInteger(
                    COALESCE(row.year,row['year:int'])
                )
            }

            WITH n, row
            CALL apoc.create.addLabels(n,split(row.labels, ':'))
            YIELD node
            RETURN count(node) AS total
        }
        IN TRANSACTIONS OF 10000 ROWS

        RETURN sum(total)
        AS totalImported
        """
        return self.execute_query(query)

    def import_peoples(self):
        query = """
        LOAD CSV WITH HEADERS
        FROM 'file:///peoples.csv'
        AS row

        FIELDTERMINATOR ','

        WITH row
        WHERE row.id IS NOT NULL

        CALL (row) {
            CREATE (n:TMP_PEOPLES)

            SET n += {
                id: row.id,
                name: row.name,
                birth: toInteger(
                    COALESCE(row.birth,row['birth:int'])
                ),
                death: toInteger(
                    COALESCE(row.death,row['death:int'])
                )
            }

            WITH n, row
            CALL apoc.create.addLabels(n,split(row.labels, ':'))
            YIELD node
            RETURN count(node) AS total
        }
        IN TRANSACTIONS OF 10000 ROWS

        RETURN sum(total)
        AS totalImported
        """
        return self.execute_query(query)

        # SET n += {
        #         id: row.id,
        #         name: row.name,
        #         birth: toInteger(
        #             COALESCE(row.birth,row['birth:int'])
        #         ),
        #         death: toInteger(
        #             COALESCE(row.death,row['death:int'])
        #         )
        #     }

    def import_edges(self):
        query = """
            LOAD CSV WITH HEADERS FROM 'file:///edges.csv' AS row 
            FIELDTERMINATOR ';'
            
            WITH row
            WHERE row.source IS NOT NULL AND row.dest IS NOT NULL
            
            CALL (row) {
                MATCH (source:TMP_PEOPLES {id: row.source})
                MATCH (dest:TMP_MOVIES {id: row.dest})
                
                // Menggunakan pembuat relasi dinamis bawaan Cypher versi baru
                CREATE (source)-[r:$(row.type)]->(dest)
                
                RETURN count(r) AS total
            }
            IN TRANSACTIONS OF 10000 ROWS
            
            RETURN sum(total) AS totalImported
        """
        return self.execute_query(query)

        # LOAD CSV WITH HEADERS FROM 'file:///edges.csv' AS row 
        # FIELDTERMINATOR ';'
        
        # WITH row
        # WHERE row.source IS NOT NULL AND row.dest IS NOT NULL
        
        # CALL (row) {
        #     MATCH (source:TMP_PEOPLES {id: row.source})
        #     MATCH (dest:TMP_MOVIES {id: row.dest})
            
        #     // Menggunakan pembuat relasi dinamis bawaan Cypher versi baru
        #     CREATE (source)-[r:$(row.type)]->(dest)
            
        #     RETURN count(r) AS total
        # }
        # IN TRANSACTIONS OF 1000 ROWS
        
        # RETURN sum(total) AS totalImported