def drop_temp_indexes(importer):

    queries = [

        """
        DROP INDEX people_id_index
        IF EXISTS
        """,

        """
        DROP INDEX movie_id_index
        IF EXISTS
        """

    ]


    for q in queries:
        importer.execute_query(q)

def remove_temp_labels(importer, label):

    while True:

        query = f"""
        MATCH (n:{label})

        WITH n
        LIMIT 10000

        REMOVE n:{label}

        RETURN count(*) AS updated
        """


        result = importer.execute_query(query)


        updated = result[0]["updated"]


        print(
            f"{label} updated: {updated}"
        )

        if updated == 0:
            break