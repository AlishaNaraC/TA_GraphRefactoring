from importer.neo4j_importer import (
    Neo4jImporter
)
from time import perf_counter

from refactor.identify_candidate_property import IdentifyCandidateProperty
from refactor.label_utils import get_label_config
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
            print("\n=== Penentuan Konfigurasi PBN ===")
            pbn_configs = {} 
            
            for prop in kandidat_properti:
                # 1. Panggil fungsi kodemu yang modular
                config = get_label_config(prop)
                
                # 2. Tambahkan input khusus PBN (nama relasi) ke dalam dict config
                rel_name = input(f"Masukkan nama relasi untuk properti '{prop}' (contoh: HAS_{prop.upper()}): ")
                config["rel"] = rel_name
                
                pbn_configs[prop] = config

            input("\nMulai Refactoring? (Tekan Enter untuk lanjut) ")

            self.refactor = PropertyBecomingNode(self.importer, kandidat_properti, pbn_configs)
            self.name = "Property Becoming a Node"

        elif technique == "ls":
            print("\n=== Penentuan Konfigurasi Label (LS) ===")
            label_configs = {}
            
            for prop in kandidat_properti:
                # Panggil fungsi get_label_config yang sudah kamu buat
                config = get_label_config(prop)
                label_configs[prop] = config
            
            # Masukkan config ke dalam LabelSpecification
            self.refactor = LabelSpecification(self.importer, kandidat_properti, label_configs)
            self.name = "Label Specification"

    def run(self):
        print(f"\n{self.name} Starting...")
        start_time = perf_counter()
        self.refactor.execute()
        self.importer.close()
        elapsed_minutes = (perf_counter() - start_time) / 60
        print(f"\nRefactor selesai dalam {elapsed_minutes:.2f} menit")