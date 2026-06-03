from importer.neo4j_importer import (
    Neo4jImporter
)
from time import perf_counter

from refactor.property_becoming_node import (
    PropertyBecomingNode
)

from refactor.label_specification import (
    LabelSpecification
)


class RefactorManager:

    def __init__(self, technique):

        self.importer = Neo4jImporter()

        if technique == "pbn":
            self.refactor = PropertyBecomingNode(self.importer)
            self.name = "Property Becoming a Node"
        elif technique == "ls":
            self.refactor = LabelSpecification(self.importer)
            self.name = "Label Specification"


    def run(self):
        print(f"\n{self.name} Starting...")
        start_time = perf_counter()
        self.refactor.execute()
        self.importer.close()
        elapsed_minutes = (perf_counter() - start_time) / 60
        print(f"\nRefactor selesai dalam {elapsed_minutes:.2f} menit")