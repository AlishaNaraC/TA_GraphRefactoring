# Membuat index sementara untuk label TMP_PEOPLES dan TMP_MOVIES, supaya query bisa lebih cepat.
def create_indexes(importer):

    queries = [

        """
        CREATE INDEX people_id_index
        IF NOT EXISTS
        FOR (n:TMP_PEOPLES)
        ON (n.id)
        """,

        """
        CREATE INDEX movie_id_index
        IF NOT EXISTS
        FOR (n:TMP_MOVIES)
        ON (n.id)
        """

    ]


    for q in queries:

        importer.execute_query(q)