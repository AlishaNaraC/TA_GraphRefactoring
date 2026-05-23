from config import NEO4J_CONFIG, DB
from importer.neo4j_importer import Neo4jImporter
from importer.schema_initializer import create_indexes
from importer.label_manager import (
    drop_temp_indexes,
    remove_temp_labels
)
from query.query_loader import QueryLoader
from query.query_parser import QueryParser
from query.property_analyzer import PropertyAnalyzer
from refactor.refactor_manager import RefactorManager

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

    loader = QueryLoader("data/queries")
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
    print("1. Jalankan semua proses")
    print("2. Import skema data")
    print("3. Analisis properti kueri")
    print("4. Refaktor database (property becoming a node)")
    pilihan = input("Masukkan pilihan [contoh: 0]: ").strip()

    if pilihan == '1':
        import_data_imdb()
        report = read_and_analyze_query()
        print(report)
        manager = RefactorManager()
    elif pilihan == '2':
        import_data_imdb()
    elif pilihan == '3':
        read_and_analyze_query()
    elif pilihan=='4':
        manager=RefactorManager()
        manager.run()

if __name__ == "__main__":
    main()
