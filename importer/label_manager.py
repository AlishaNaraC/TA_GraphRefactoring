def remove_temp_labels(importer):

    queries = [

        """
        MATCH (n:TMP_PEOPLES)
        REMOVE n:TMP_PEOPLES
        """,

        """
        MATCH (n:TMP_MOVIES)
        REMOVE n:TMP_MOVIES
        """

    ]

    for q in queries:

        importer.execute_query(q)