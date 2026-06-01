import re
import csv

PROPERTY_REFACTOR_MAP = {
    "year":     {"relation": "RELEASED_IN",  "label_format": "year_{val}"},
    "category": {"relation": "HAS_CATEGORY", "label_format": "{val}"},
    "death":    {"relation": "DIED_IN",     "label_format": "year_{val}"},
    "birth":    {"relation": "BORN_IN",      "label_format": "year_{val}"},
}

# Tambahkan list node Person dan Movie
PERSON_NODES = {
    "actor", "actress", "animation_department", "art_department", "art_director",
    "assistant", "assistant_director", "camera_department", "casting_department",
    "casting_director", "cinematographer", "composer", "costume_department",
    "costume_designer", "director", "editor", "editorial_department", "executive",
    "electrical_department", "legal", "location_management", "make_up_department",
    "manager", "miscellaneous", "music_department", "producer", "production_department",
    "production_designer", "production_manager", "publicist", "script_department",
    "set_decorator", "sound_department", "soundtrack", "special_effects", "stunts",
    "talent_agent", "transportation_department", "visual_effects", "writer"
}

MOVIE_NODES = {
    "action", "adult", "adventure", "animation", "biography", "comedy", "crime",
    "documentary", "drama", "family", "fantasy", "film_noir", "game_show", "history",
    "horror", "music", "musical", "mystery", "news", "reality_tv", "romance",
    "sci_fi", "sport", "talk_show", "thriller", "war", "western"
}

# Baca semua baris dari file txt, buang spasi/newline di tiap baris (strip()), dan skip baris kosong (if line.strip()). 
# Hasilnya list of string, tiap elemennya satu query.
def read_queries_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    queries = [line.strip() for line in lines if line.strip()]
    return queries

# Fungsi ini menghitung jumlah properti dalam WHERE. Dipanggil 2 kali per query, sebelum dan sesudah refaktorisasi
# untuk menghitung berapa properti yang berhasil direduksi. Caranya: 
# cari blok WHERE dengan regex, 
# pisahkan tiap kondisi berdasarkan AND, 
# lalu hitung jumlahnya.
def count_where_properties(query):
    """Hitung jumlah properti dalam klausa WHERE"""
    where_block = re.search(r'WHERE\s*\((.+?)\)\s*RETURN', query, re.IGNORECASE)
    if not where_block:
        return 0
    
    where_content = where_block.group(1)
    conditions = [c.strip() for c in re.split(r'\s+AND\s+', where_content, flags=re.IGNORECASE)]
    return len([c for c in conditions if c])  # skip kosong

def refactor_where_to_node(query):
    # Ambil semua kondisi di dalam WHERE, pisahkan per AND.
    where_block = re.search(r'WHERE\s*\((.+?)\)\s*RETURN', query, re.IGNORECASE)
    if not where_block:
        return query

    where_content = where_block.group(1)
    conditions = [c.strip() for c in re.split(r'\s+AND\s+', where_content, flags=re.IGNORECASE)]

    cond_pattern = re.compile(r'(\w+)\.(\w+)\s*=\s*["\']?(\w+)["\']?')

    refactor_groups = {}
    remaining_conditions = []

# Tiap kondisi dicek, kalau propnya ada di mapping (year/category/death/birth) maka direfaktor, kalau tidak, dibiarkan tetap di WHERE. 
# Kondisi yang direfaktor dikelompokkan berdasarkan variabelnya (n2, n3, dst).
    for cond in conditions:
        m = cond_pattern.match(cond)
        if not m:
            remaining_conditions.append(cond)
            continue

        var_name  = m.group(1)
        prop_name = m.group(2).lower()
        prop_val  = m.group(3)

        if prop_name not in PROPERTY_REFACTOR_MAP:
            remaining_conditions.append(cond)  # tidak direfaktor, sisakan di WHERE
            continue

        mapping   = PROPERTY_REFACTOR_MAP[prop_name]
        relation  = mapping["relation"]
        new_label = mapping["label_format"].format(prop=prop_name, val=prop_val)

        if var_name not in refactor_groups:
            refactor_groups[var_name] = []
        refactor_groups[var_name].append((relation, new_label)) # masuk antrian refaktor

    # Setelah semua kondisi diklasifikasi, klausa WHERE dihapus dulu seluruhnya dari query. Nanti yang tersisa akan ditambahkan kembali.
    query_no_where = re.sub(r'\s*WHERE\s*\(.+?\)', '', query, flags=re.IGNORECASE).strip()

    def get_node_label(var, q):
        m = re.search(rf'\({var}:(\w+)\)', q)
        return m.group(1) if m else None

    extra_patterns = []

    for var_name, prop_list in refactor_groups.items():
        node_label = get_node_label(var_name, query_no_where)

        # Cek apakah node ini Person atau Movie. Jika Person, semua properti diubah jadi pattern baru. 
        # Jika Movie, properti pertama disisipkan ke node, sisanya jadi pattern baru.
        is_person = node_label in PERSON_NODES
        is_movie  = node_label in MOVIE_NODES

        if is_person:
            # Person node -> SEMUA properti jadi pattern baru
            for relation, new_label in prop_list:
                extra_patterns.append(f"({var_name}:{node_label})-[:{relation}]->(:{new_label})")

        elif is_movie:
            # Movie node -> properti pertama disisipkan, sisanya jadi pattern baru
            first_relation, first_label = prop_list[0]
            node_pattern = re.compile(rf'\({var_name}:{node_label}\)')
            matches_node = list(node_pattern.finditer(query_no_where))

            if matches_node:
                last_match = matches_node[-1]
                insert_pos = last_match.end()
                insert_str = f"-[:{first_relation}]->(:{first_label})"
                query_no_where = (
                    query_no_where[:insert_pos]
                    + insert_str
                    + query_no_where[insert_pos:]
                )

            for relation, new_label in prop_list[1:]:
                extra_patterns.append(f"({var_name}:{node_label})-[:{relation}]->(:{new_label})")

    # Setelah semua refaktor siap, sisipkan pattern baru ke query.
    # Jika ada kondisi yang tidak direfaktor, gabungkan kembali ke WHERE.
    if extra_patterns:
        extra_str = ", " + ", ".join(extra_patterns)
        query_no_where = re.sub(r'(RETURN)', f'{extra_str} \\1', query_no_where, flags=re.IGNORECASE)

    if remaining_conditions:
        leftover = " AND ".join(remaining_conditions)
        query_no_where = re.sub(r'(RETURN)', f'WHERE ({leftover}) \\1', query_no_where, flags=re.IGNORECASE)

    result = re.sub(r'\s{2,}', ' ', query_no_where).strip()
    return result

# Fungsi untuk menyimpan query hasil refaktorisasi ke file txt, satu query per baris.
def save_queries_to_file(queries, file_path):
    with open(file_path, 'w') as f:
        for query in queries:
            f.write(query + '\n')

# Fungsi untuk menyimpan data ke file csv.
def save_queries_to_csv(data, file_path):
    """
    data: list of dict dengan key:
    - kueri_awal, kueri_baru, jumlah_where_awal, jumlah_where_baru, persentase_penurunan
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'Kueri Awal',
            'Kueri Baru',
            'Jumlah Properti WHERE Awal',
            'Jumlah Properti WHERE Sesudah',
            'Persentase Penurunan'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def get_where_pattern(jumlah_properti):
    """Konversi jumlah properti WHERE ke label pola"""
    pola = {
        0: "-",          # tidak ada WHERE
        1: "A",
        2: "A AND B",
        3: "A AND B AND C",
        4: "A AND B AND C AND D"
    }
    return pola.get(jumlah_properti, f"{jumlah_properti} kondisi")

def run_reconstruction():
    input_file  = "data/queries/Query_Where_80.txt"
    output_txt  = "data/report/Query_Where_80_Refactored.txt"
    output_csv  = "data/report/Query_Where_80_Refactored.csv"

    queries = read_queries_from_file(input_file)
    print(f"Berhasil membaca {len(queries)} query dari {input_file}\n")

    refactored_queries = []
    csv_data = []

    for i, query in enumerate(queries, 1):
        result = refactor_where_to_node(query)

        # Hitung properti WHERE sebelum dan sesudah
        count_before = count_where_properties(query)
        count_after  = count_where_properties(result)

        # Hitung persentase penurunan
        if count_before > 0:
            penurunan = (count_before - count_after) / count_before * 100
            persentase = f"{penurunan:.0f}%"
        else:
            persentase = "0%"

        refactored_queries.append(result)
        csv_data.append({
            'Kueri Awal'                    : query,
            'Kueri Baru'                    : result,
            'Jumlah Properti WHERE Awal'    : count_before,
            'Jumlah Properti WHERE Sesudah' : count_after,
            'Persentase Penurunan'          : persentase
        })

        print(f"Query {i} Input      : {query}")
        print(f"Query {i} Output     : {result}")
        print(f"         WHERE Awal  : {count_before} properti")
        print(f"         WHERE Baru  : {count_after} properti")
        print(f"         Penurunan   : {persentase}")
        print()

    save_queries_to_file(refactored_queries, output_txt)
    save_queries_to_csv(csv_data, output_csv)
    print(f"Hasil disimpan ke {output_txt} dan {output_csv}")
