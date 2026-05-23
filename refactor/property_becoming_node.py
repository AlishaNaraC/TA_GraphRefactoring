from refactor.kandidat_properti import (
    KANDIDAT_PROPERTI
)

from refactor.nama_relasi_baru import (
    NAMA_RELASI_BARU
)

from refactor.label_utils import (
    generate_labels
)


class PropertyBecomingNode:

    def __init__(self, importer):

        self.importer=importer


    def execute(self):

        for prop in KANDIDAT_PROPERTI:

            print(
                f"\nRefactoring {prop} with new relationship {NAMA_RELASI_BARU[prop]}..."
            )

            rel_name=(
                NAMA_RELASI_BARU[prop]
            )


            query=f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL

            RETURN
                id(n) as id,
                n.{prop} as value
            """

            rows=self.importer.run_query(
                query
            )

            total=0


            for row in rows:

                node_id=row["id"]

                value=row["value"]

                labels=generate_labels(
                    prop,
                    value
                )

                for label in labels:

                    create_query="""
                    MATCH (n)
                    WHERE id(n)=$node_id

                    CALL apoc.merge.node([$label], {value: $label})
                    YIELD node

                    CALL apoc.create.relationship(
                        n,
                        $rel,
                        {},
                        node
                    )
                    YIELD rel

                    RETURN count(*)
                    """

                    self.importer.run_query(
                        create_query,
                        {
                            "node_id":node_id,
                            "label":label,
                            "rel":rel_name
                        }
                    )

                remove_query=f"""
                MATCH (n)
                WHERE id(n)=$node_id

                REMOVE n.{prop}
                """

                self.importer.run_query(
                    remove_query,
                    {
                        "node_id":node_id
                    }
                )

                total+=1


            print(
                f"{total} node selesai"
            )