from config import NEO4J_CONFIG
from importer.neo4j_importer import Neo4jImporter
from importer.schema_initializer import create_indexes
from importer.label_manager import (
    drop_temp_indexes,
    remove_temp_labels
)

def import_skema_data():
    importer = Neo4jImporter(**NEO4J_CONFIG)
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
    if edges_result and isinstance(edges_result, list):
        if isinstance(edges_result[0], dict):
            total_edges = edges_result[0].get('total', 0)
    if not total_edges:
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
    print("0. Jalankan semua proses")
    print("1. Import skema data")
    pilihan = input("Masukkan pilihan [contoh: 0]: ").strip()
    if pilihan == '0':
        import_skema_data()
        import_dan_analisis_kueri()
    elif pilihan == '1':
        import_skema_data()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()