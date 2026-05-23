from importer.neo4j_importer import (
    Neo4jImporter
)

from refactor.property_becoming_node import (
    PropertyBecomingNode
)


class RefactorManager:

    def __init__(self):

        self.importer = Neo4jImporter()

        self.refactor = PropertyBecomingNode(
            self.importer
        )


    def run(self):

        print("\nProperty Becoming Node...")

        self.refactor.execute()

        self.importer.close()

        print("\nRefactor selesai")