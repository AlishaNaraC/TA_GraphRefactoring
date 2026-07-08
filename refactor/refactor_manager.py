from importer.neo4j_importer import (
    Neo4jImporter
)
from time import perf_counter

from refactor.identify_candidate_property import IdentifyCandidateProperty
from refactor.property_becoming_node import (
    PropertyBecomingNode
)

from refactor.label_specification import (
    LabelSpecification
)
from refactor.relation_input import get_relation_names


class RefactorManager:

    def __init__(self, technique):
        self.importer = Neo4jImporter()

        print("Mengidentifikasi kandidat properti (analisis DVR)...")
        identifier = IdentifyCandidateProperty(self.importer)
        kandidat_properti = identifier.execute()
        print(f"\n=== Kandidat Properti (DVR < 1%) ===")
        print(kandidat_properti)

        if technique == "pbn":
            nama_relasi_baru = get_relation_names(kandidat_properti)
            print(f"\nNama relasi yang akan dibentuk: {nama_relasi_baru}")

            input("\nMulai Refactoring? (Tekan Enter untuk lanjut) ")

            self.refactor = PropertyBecomingNode(self.importer, kandidat_properti, nama_relasi_baru)
            self.name = "Property Becoming a Node"

        elif technique == "ls":
            input("\nMulai Refactoring? (Tekan Enter untuk lanjut) ")

            self.refactor = LabelSpecification(self.importer, kandidat_properti)
            self.name = "Label Specification"

    def run(self):
        print(f"\n{self.name} Starting...")
        start_time = perf_counter()
        self.refactor.execute()
        self.importer.close()
        elapsed_minutes = (perf_counter() - start_time) / 60
        print(f"\nRefactor selesai dalam {elapsed_minutes:.2f} menit")