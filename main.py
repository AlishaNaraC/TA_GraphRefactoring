from config import NEO4J_CONFIG, DB
from execution.runner import run_baseline, run_refactored
from importer.neo4j_importer import Neo4jImporter
from importer.schema_initializer import create_indexes
from importer.label_manager import (
    drop_temp_indexes,
    remove_temp_labels
)
from reconstruction.pbn_query_reconstructor import run_reconstruction
from reconstruction.ls_query_reconstructor import run_reconstruction_label_specification
from refactor.refactor_manager import RefactorManager
from validation.validation_baseline import run_baseline_stats
from validation.validation_property_becoming_a_node import run_validation_property_becoming_node
from validation.validation_label_specification import run_validation_label_specification

def import_data_imdb():
    importer = Neo4jImporter()
    print("Import movies...")
    importer.import_movies()
    print("Import peoples...")
    importer.import_peoples()
    print("Create indexes...")
    create_indexes(importer)
    print("Import edges...")
    edges_result = importer.import_edges()
    print(f"Hasil import_edges: {edges_result}")
    
    total_edges = 0
    if edges_result:
        total_edges = edges_result[0].get("total", 0)
    if total_edges <= 0:
        print("Tidak ada edge yang berhasil diimpor. Proses dihentikan.")
        importer.close()
        return

    print("Remove temp labels...")
    drop_temp_indexes(importer)
    remove_temp_labels(importer, "TMP_PEOPLES")
    remove_temp_labels(importer, "TMP_MOVIES")
    importer.close()
    print("Import selesai")

def main():
    print("Pilih mode eksekusi:")
    print("1. Import skema data")
    print("-------------------------------")
    print("2. Refaktor database (property becoming a node)")
    print("3. Rekonstruksi kueri (property becoming a node)")
    print("4. Refaktor database (label specification)")
    print("5. Rekonstruksi kueri (label specification)")
    print("-------------------------------")
    print("6. Jalankan kueri baseline")
    print("7. Jalankan kueri refactored (property becoming a node)")
    print("8. Jalankan kueri refactored (label specification)")
    print("-------------------------------")
    print("9. Baca statistik baseline (sebelum refaktorisasi)")
    print("10. Validasi refaktorisasi (property becoming a node)")
    print("11. Validasi refaktorisasi (label specification)")


    pilihan = input("Masukkan pilihan [contoh: 1]: ").strip()

    if pilihan == '1':
        import_data_imdb()
    elif pilihan == '2':
        read_and_analyze_query()
    elif pilihan == '3':
        manager = RefactorManager(technique="pbn")
        manager.run()
    elif pilihan == '4':
        run_reconstruction()
    elif pilihan == '5':
        manager=RefactorManager(technique="ls")
        manager.run()
    elif pilihan=='6':
        run_reconstruction_label_specification()
    elif pilihan=='7':
        run_baseline(
            input_file  = "data/queries/Query_Where_80.txt",
            output_csv  = "data/report/baseline/hasil_baseline_index_prop_Nara.csv"
        )
    elif pilihan == '8':
        run_refactored(
            input_csv  = "data/queries/Query_Where_80_Refactored.csv",
            output_csv = "data/report/property_becoming_node/hasil_refactored_PBN_index_default_Nara.csv"
        )
    elif pilihan == '9':
        run_refactored(
            input_csv  = "data/queries/Query_LabelSpec_Refactored.csv",
            output_csv = "data/report/label_specification/hasil_refactored_LS_index_default_Nara.csv"
        )
    elif pilihan == '10':
        run_baseline_stats()
    elif pilihan == '11':
        run_validation_property_becoming_node()
    elif pilihan == '12':
        run_validation_label_specification()
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")
if __name__ == "__main__":
    main()