from neo4j import GraphDatabase


driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "12345678")
)


try:
    with driver.session() as session:

        result = session.run(
            "RETURN 'connected' AS message"
        )

        for row in result:

            print(row["message"])


finally:
    driver.close()