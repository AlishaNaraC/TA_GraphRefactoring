from neo4j import GraphDatabase


class Neo4jCleaner:

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
    # DELETE ALL NODES + RELATIONSHIPS
    # =====================================

    def delete_all_nodes(self):

        print(
            "\nDeleting all nodes and relationships..."
        )

        while True:

            query = """
            MATCH (n)

            WITH n
            LIMIT 1000000

            DETACH DELETE n

            RETURN count(*) AS deleted
            """

            result = self.execute_query(query)

            deleted = result[0]["deleted"]


            print(
                f"Deleted batch: {deleted}"
            )


            if deleted == 0:

                break


        print(
            "All nodes deleted"
        )


    # =====================================
    # DROP ALL INDEXES
    # =====================================

    def drop_all_indexes(self):

        print(
            "\nDropping indexes..."
        )

        query = """
        SHOW INDEXES
        YIELD name

        RETURN name
        """

        indexes = self.execute_query(query)


        for idx in indexes:

            name = idx["name"]


            if name:

                drop_query = (
                    f"DROP INDEX `{name}` "
                )

                self.execute_query(
                    drop_query
                )

                print(
                    f"Dropped index: {name}"
                )


    # =====================================
    # DROP ALL CONSTRAINTS
    # =====================================

    def drop_all_constraints(self):

        print(
            "\nDropping constraints..."
        )

        query = """
        SHOW CONSTRAINTS
        YIELD name

        RETURN name
        """

        constraints = self.execute_query(
            query
        )


        for c in constraints:

            name = c["name"]


            if name:

                drop_query = (
                    f"DROP CONSTRAINT `{name}`"
                )

                self.execute_query(
                    drop_query
                )

                print(
                    f"Dropped constraint: {name}"
                )


    # =====================================
    # FULL CLEAN
    # =====================================

    def clean_database(self):

        self.drop_all_constraints()

        self.drop_all_indexes()

        self.delete_all_nodes()

        print(
            "\nDatabase fully cleaned"
        )


# =====================================
# MAIN
# =====================================

if __name__ == "__main__":

    cleaner = Neo4jCleaner(

        uri="bolt://localhost:7687",

        user="neo4j",

        password="12345678",

        database="neo4j"
    )


    cleaner.clean_database()


    cleaner.close()