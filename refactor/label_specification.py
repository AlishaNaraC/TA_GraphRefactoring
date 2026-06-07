from refactor.kandidat_properti import (
    KANDIDAT_PROPERTI
)

from refactor.label_utils import (
    generate_labels
)


class LabelSpecification:

    def __init__(self, importer):

        self.importer = importer


    def execute(self):

        for prop in KANDIDAT_PROPERTI:

            print(
                f"\nRefactoring {prop} property..."
            )

            query = f"""
            MATCH (n)
            WHERE n.{prop} IS NOT NULL

            RETURN
                id(n) as id,
                n.{prop} as value
            """

            rows = self.importer.run_query(
                query
            )

            total = 0

            for row in rows:

                node_id = row["id"]

                value = row["value"]

                labels = generate_labels(
                    prop,
                    value
                )

                for label in labels:

                    # tambahkan label baru langsung
                    # ke node yang sama
                    add_label_query = """
                    MATCH (n)
                    WHERE id(n) = $node_id

                    CALL apoc.create.addLabels(
                        n,
                        [$label]
                    )
                    YIELD node

                    RETURN count(*)
                    """

                    self.importer.run_query(
                        add_label_query,
                        {
                            "node_id": node_id,
                            "label": label
                        }
                    )

                # hapus properti asal setelah
                # label baru ditambahkan
                remove_query = f"""
                MATCH (n)
                WHERE id(n) = $node_id

                REMOVE n.{prop}
                """

                self.importer.run_query(
                    remove_query,
                    {
                        "node_id": node_id
                    }
                )

                total += 1

            print(
                f"{total} node selesai"
            )