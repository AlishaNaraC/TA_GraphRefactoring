from neo4j import GraphDatabase


class Neo4jImporter:

    def __init__(
        self,
        uri,
        user,
        password,
        database
    ):

        self.driver = GraphDatabase.driver(
            uri,
            auth=(user, password)
        )

        self.database = database


    def close(self):

        self.driver.close()


    def execute_query(
        self,
        query
    ):

        with self.driver.session(
            database=self.database
        ) as session:

            result = session.run(query)

            return list(result)


    # =====================================
    # IMPORT MOVIES
    # =====================================

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
                    COALESCE(
                        row.year,
                        row['year:int']
                    )
                )
            }

            WITH n, row

            CALL apoc.create.addLabels(
                n,
                split(row.labels, ':')
            )
            YIELD node

            RETURN count(node) AS total
        }

        IN TRANSACTIONS OF 10000 ROWS

        RETURN sum(total)
        AS totalImported
        """

        return self.execute_query(query)


    # =====================================
    # IMPORT PEOPLES
    # =====================================

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
                    COALESCE(
                        row.birth,
                        row['birth:int']
                    )
                ),

                death: toInteger(
                    COALESCE(
                        row.death,
                        row['death:int']
                    )
                )
            }

            WITH n, row

            CALL apoc.create.addLabels(
                n,
                split(row.labels, ':')
            )
            YIELD node

            RETURN count(node) AS total
        }

        IN TRANSACTIONS OF 10000 ROWS

        RETURN sum(total)
        AS totalImported
        """

        return self.execute_query(query)


    # =====================================
    # IMPORT EDGES
    # =====================================

    def import_edges(self):
        query = """
            CALL apoc.periodic.iterate(
            "LOAD CSV WITH HEADERS FROM 'file:///edges.csv' AS row FIELDTERMINATOR ','
            RETURN row",
            "WITH row
            MATCH (source:PersonNode {id: row.source})
            MATCH (dest:MovieNode {id: row.dest})
            CALL apoc.create.relationship(source, row.type, {}, dest) YIELD rel
            RETURN count(rel)",
            {batchSize: 20000, parallel: false}
            )
            YIELD batches, total, errorMessages;
        """
        # Jalankan dengan :auto atau CALL ... IN TRANSACTIONS besar di luar
        return self.execute_query("CALL { " + query + " } IN TRANSACTIONS OF 10000 ROWS RETURN sum(totalImported) AS total")