from config import NEO4J_CONFIG, DB
from execution.runner import run_baseline, run_refactored
from importer.neo4j_importer import Neo4jImporter
from importer.schema_initializer import create_indexes
from importer.label_manager import (
    drop_temp_indexes,
    remove_temp_labels
)
from query.transform_query_to_numeric import transform_file_kueri_baseline_to_numeric
from query.transform_query_to_numeric_pbn import transform_file_kueri_pbn_to_numeric
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
    print("6. Baca statistik baseline (sebelum refaktorisasi)")
    print("7. Validasi refaktorisasi (property becoming a node)")
    print("8. Validasi refaktorisasi (label specification)")
    print("-------------------------------")
    print("9. Transformasi kueri baseline ke numerik")
    print("10. Transformasi kueri refactored (property becoming a node) ke numerik")
    print("11. Transformasi kueri refactored (label specification) ke numerik")
    print("-------------------------------")
    print("12. Jalankan kueri baseline")
    print("13. Jalankan kueri refactored (property becoming a node)")
    print("14. Jalankan kueri refactored (label specification)")

    pilihan = input("Masukkan pilihan [contoh: 1]: ").strip()

    match pilihan:
        case '1':
            import_data_imdb()

        case '2':
            manager = RefactorManager(technique="pbn")
            manager.run()

        case '3':
            run_reconstruction()

        case '4':
            manager = RefactorManager(technique="ls")
            manager.run()

        case '5':
            run_reconstruction_label_specification()

        case '6':
            run_baseline_stats()

        case '7':
            run_validation_property_becoming_node()

        case '8':
            run_validation_label_specification()

        case '9':
            transform_file_kueri_baseline_to_numeric(
                input_file="data/queries/Query_Where.txt",
                output_file="data/report/baseline/Query_Where_Baseline_Numerik.csv"
            )

        case '10':
            transform_file_kueri_pbn_to_numeric(
                input_file="data/queries/Query_Where_80_Refactored.txt",
                output_file="data/report/property_becoming_node/Refactored_Query_Where_PBN_Numerik.csv"
            )
    # HARUS DIGANTI CODENYA============================================================
    # HARUS DIGANTI CODENYA============================================================
    # HARUS DIGANTI CODENYA============================================================
        case '11':
            transform_file_kueri_pbn_to_numeric(
                input_file="data/queries/Query_Where_80_Refactored_LS.txt",
                output_file="data/report/label_specification/Refactored_Query_Where_LS_Numerik.csv"
            )

        case '12':
            run_baseline(
                input_file="data/queries/Query_Where.txt",
                output_csv="data/report/baseline/executed_190_baseline.csv"
            )

        case '13':
            run_refactored(
                input_csv="data/queries/Query_PBN.csv",
                output_csv="data/report/property_becoming_node/executed_190_PBN.csv"
            )

        case '14':
            run_refactored(
                input_csv="data/queries/Query_LS_OR.csv",
                output_csv="data/report/label_specification/hasil_refactored_LS_OR.csv"
            )

        case _:
            print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")


if __name__ == "__main__":
    main()