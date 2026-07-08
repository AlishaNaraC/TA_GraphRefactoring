def get_relation_names(kandidat_properti):
    """
    Meminta input nama relasi baru dari pengguna untuk setiap 
    kandidat properti pada teknik property becoming a node.
    """
    nama_relasi = {}
    print("\n=== Penentuan Nama Relasi Baru ===")
    for prop in kandidat_properti:
        while True:
            rel_name = input(
                f"Berikan nama relasi yang akan mengarah kepada node baru "
                f"yang berasal dari properti '{prop}': "
            ).strip()
            if rel_name:
                nama_relasi[prop] = rel_name.upper().replace(" ", "_")
                break
            print("Nama relasi tidak boleh kosong. Silakan input ulang.")
    return nama_relasi