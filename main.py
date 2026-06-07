from config import NEO4J_CONFIG, DB
from execution.runner import run_baseline, run_refactored
from importer.neo4j_importer import Neo4jImporter
from importer.schema_initializer import create_indexes
from importer.label_manager import (
    drop_temp_indexes,
    remove_temp_labels
)
from query.query_loader import QueryLoader
from query.query_parser import QueryParser
from query.property_analyzer import PropertyAnalyzer
from reconstruction.query_reconstructor import run_reconstruction
from reconstruction.reconstructor_label_specification import run_reconstruction_label_specification
from refactor.refactor_manager import RefactorManager
from validation.validation_baseline import run_baseline_stats
from validation.validation_property_becoming_a_node import run_validation_property_becoming_node

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

def read_and_analyze_query():

    loader = QueryLoader("data/queries/Query_Where_80.txt")
    queries = loader.load_queries()

    parser = QueryParser()
    all_conditions = []

    for q in queries:
        conditions = parser.extract_conditions(q["query"])
        all_conditions.extend(conditions)

    analyzer = PropertyAnalyzer()
    property_counter, value_counter = analyzer.analyze(all_conditions)

    report = analyzer.generate_report(property_counter, value_counter)

    # Simpan report ke CSV
    import os
    output_dir = "data/report"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "hasil_report.csv")
    analyzer.save_report_to_csv(report, output_path)
    print(f"Report telah disimpan ke {output_path}\n")

    print("\n=== QUERY ANALYZING REPORT ===\n")
    for item in report:
        print(f">> {item['total_redundancy']} redundancy for \"{item['property']}\" property key")
        if item['is_redundant']:
            print(f"> \"{item['most_called_value']}\" is the most called ({item['value_redundancy']} redundancy)")
            for redundant in item["redundant_values"]:
                print(f"- \"{redundant['value']}\" "f"({redundant['count']} redundancy)")
        else:
            print("No redundant values (all values are unique)\n")
        print("-----------------------------\n")


def main():
    print("Pilih mode eksekusi:")
    print("1. Import skema data")
    print("2. Analisis properti kueri")
    print("-------------------------------")
    print("3. Refaktor database (property becoming a node)")
    print("4. Rekonstruksi kueri (property becoming a node)")
    print("5. Refaktor database (label specification)")
    print("6. Rekonstruksi kueri (label specification)")
    print("-------------------------------")
    print("7. Jalankan kueri baseline")
    print("8. Jalankan kueri refactored (property becoming a node)")
    print("9. Jalankan kueri refactored (label specification)")
    print("-------------------------------")
    print("10. Baca statistik baseline (sebelum refaktorisasi)")
    print("11. Validasi refaktorisasi (property becoming a node)")
    print("12. Validasi refaktorisasi (label specification)")


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
            output_csv  = "data/report/hasil_baseline.csv"
        )
    elif pilihan == '8':
        run_refactored(
            input_csv  = "data/report/Query_Where_80_Refactored.csv",
            output_csv = "data/report/hasil_refactored.csv"
        )
    elif pilihan == '9':
    elif pilihan == '10':
        run_baseline_stats()
    elif pilihan == '11':
        run_validation_property_becoming_node()
    elif pilihan == '12':
        run_validation_label_specification()

if __name__ == "__main__":
    main()