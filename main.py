from config import NEO4J_CONFIG, BASELINE_DB, PBN_DB, ES_DB
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
    importer = Neo4jImporter(**NEO4J_CONFIG, database=BASELINE_DB)
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
    return report

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
        
def show_properties(report):

    print("\nDaftar properti kandidat refaktorisasi:\n")

    for i, item in enumerate(report, start=1):
        print(
            f"{i}. {item['property']} "
            f"({item['total_redundancy']} redundancy)"
        )

def choose_property(report):

    show_properties(report)
    choice = input("\nPilih nomor properti: ").strip()

    try:
        index = int(choice) - 1
        return report[index]["property"]
    except:
        return None

def refactor_pbn(manager, report):

    manager.create_pbn_database()

    while True:
        prop = choose_property(report)

        if not prop:
            print("Pilihan tidak valid")
            continue

        print(f"\nRefactor PBN: {prop}")

        manager.run_pbn_refactor([prop])

        again = input("\nRefactor property lain? (y/n): ").strip().lower()

        if again != "y":
            break

def refactor_es(manager, report):

    manager.create_es_database()

    rel_type = input("\nMasukkan relationship type [contoh: ACTED_IN]: ").strip()

    while True:
        prop = choose_property(report)

        if not prop:
            print("Pilihan tidak valid")
            continue

        print(f"\nRefactor ES: "f"{rel_type} + {prop}")

        manager.run_es_refactor(rel_type,[prop])

        again = input(
            "\nRefactor property lain? (y/n): "
        ).strip().lower()

        if again != "y":
            break

def main():
    print("Pilih mode eksekusi:")
    print("0. Jalankan semua proses")
    print("1. Import skema data")
    print("2. Import dan analisis kueri")
    print("3. Refactor database")
    pilihan = input("Masukkan pilihan [contoh: 0]: ").strip()

    if pilihan == '0':
        import_data_imdb()
        report = read_and_analyze_query()
        print(report)
        manager = RefactorManager()
    elif pilihan == '1':
        import_data_imdb()
    elif pilihan == '2':
        report = read_and_analyze_query()
        print(report)
    elif pilihan == '3':
        report = read_and_analyze_query()
        manager = RefactorManager()

        print("Pilih teknik refaktorisasi:")
        print("1. Property Becoming a Node (PBN)")
        print("2. Edge Specification (ES)")
        teknik = input("Masukkan pilihan teknik [contoh: 1]: ").strip()
        if teknik == '1':
            refactor_pbn(manager, report)
        elif teknik == '2':
            refactor_es(manager, report)
        else:
            print("Pilihan teknik tidak valid.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
