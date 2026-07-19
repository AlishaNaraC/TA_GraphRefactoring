import re
import csv
import itertools

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
    """
    Tujuan  : Membaca daftar kueri dari file teks, satu kueri per baris.
    Input   : file_path (path ke file .txt berisi kueri Cypher, satu per baris)
    Output  : list berisi kueri-kueri (string), baris kosong diabaikan
    """
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
    """
    Tujuan  : Menghitung jumlah kondisi filter properti dalam klausa WHERE (pola AND murni).
    Input   : query (kueri Cypher lengkap, contoh: "MATCH (...) WHERE (n1.year=1999 AND n1.category='movie') RETURN ...")
    Output  : jumlah kondisi (integer), 0 kalau tidak ada WHERE
    """
    where_block = re.search(r'WHERE\s*\((.+?)\)\s*RETURN', query, re.IGNORECASE)
    if not where_block:
        return 0
    
    where_content = where_block.group(1)
    conditions = [c.strip() for c in re.split(r'\s+AND\s+', where_content, flags=re.IGNORECASE)]
    return len([c for c in conditions if c])  # skip kosong

#Fungsi buat memisahkan kueri yang mengandung AND
def refactor_where_to_node(query):
    """
    Tujuan  : Merekonstruksi kueri berpola AND murni — mengubah kondisi filter properti
              di WHERE (contoh: n1.year=1999) menjadi pola traversal relasi baru di MATCH
              (contoh: (n1)-[:RELEASED_IN]->(:year_1999)), sesuai teknik property becoming a node.
    Input   : query (kueri Cypher lengkap)
    Output  : kueri hasil rekonstruksi (string)
    """
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

# Fungsi untuk menyimpan data ke file csv.
def save_queries_to_csv(data, file_path):
    """
    Tujuan  : Menyimpan hasil rekonstruksi kueri (baseline, hasil refactor, statistik
              pengurangan properti) ke dalam sebuah file CSV.
    Input   : data (list of dict, tiap dict berisi kolom Kueri Baseline, Kueri Refactored,
              Jumlah Properti WHERE Baseline/Refactored, Persentase Penurunan),
              file_path (path tujuan penyimpanan file CSV)
    Output  : tidak ada (langsung menulis ke file)
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'Kueri Baseline',
            'Kueri Refactored',
            'Jumlah Properti WHERE Baseline',
            'Jumlah Properti WHERE Refactored',
            'Persentase Penurunan'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def split_by_keyword(text, keyword):
    """
    Tujuan  : Memecah teks WHERE menjadi beberapa bagian berdasarkan kata kunci AND/OR.
    Input   : text (contoh: "n1.year=1999 AND n1.category='movie'"), keyword ("AND" atau "OR")
    Output  : list bagian teks yang sudah terpisah, contoh: ["n1.year=1999", "n1.category='movie'"]
    Catatan : Pemisahan hanya dilakukan jika keyword berada di LUAR kurung (depth==0),
              supaya AND yang ada di dalam kurung (A AND B) tidak ikut kepecah saat sedang mencari OR.
    """
    pattern = re.compile(r'\b' + keyword + r'\b', re.IGNORECASE)
    parts = []
    depth = 0
    last = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '(':
            depth += 1
            i += 1
            continue
        elif ch == ')':
            depth -= 1
            i += 1
            continue
        if depth == 0:
            m = pattern.match(text, i)
            if m:
                parts.append(text[last:i].strip())
                i = m.end()
                last = i
                continue
        i += 1
    parts.append(text[last:].strip())
    return [p for p in parts if p]


def strip_outer_parens(s):
    """
    Tujuan  : Membuang kurung pembungkus jika kurung tersebut membungkus SELURUH teks.
    Input   : s (contoh: "(n1.year=1999 AND n1.category='movie')")
    Output  : teks tanpa kurung luar, contoh: "n1.year=1999 AND n1.category='movie'"
    Catatan : Tidak asal buang kurung pertama & terakhir — dicek dulu apakah keduanya
              memang sepasang (bukan kasus seperti "(A) OR (B)" yang kurungnya tidak menyatu).
    """
    s = s.strip()
    if s.startswith('(') and s.endswith(')'):
        depth = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0 and idx != len(s) - 1:
                    return s
        return s[1:-1].strip()
    return s


def classify_conditions(conditions):
    """
    Tujuan  : Memilah daftar kondisi WHERE ke dalam 2 kelompok: yang bisa direfaktor
              menjadi relasi baru, dan yang harus tetap di klausa WHERE.
    Input   : conditions (list kondisi, contoh: ["n1.year=1999", "n1.name='Budi'"])
    Output  : refactor_groups (dict kondisi yang bisa direfaktor, dikelompokkan per variabel node)
              remaining (list kondisi yang tidak bisa direfaktor, misal properti "name")
    """
    cond_pattern = re.compile(r'(\w+)\.(\w+)\s*=\s*["\']?(\w+)["\']?')
    refactor_groups = {}
    remaining = []

    for cond in conditions:
        m = cond_pattern.match(cond)
        if not m:
            remaining.append(cond)
            continue

        var_name, prop_name, prop_val = m.group(1), m.group(2).lower(), m.group(3)

        if prop_name not in PROPERTY_REFACTOR_MAP:
            remaining.append(cond)
            continue

        mapping = PROPERTY_REFACTOR_MAP[prop_name]
        relation = mapping["relation"]
        new_label = mapping["label_format"].format(val=prop_val)

        refactor_groups.setdefault(var_name, [])
        if (relation, new_label) not in refactor_groups[var_name]:
            refactor_groups[var_name].append((relation, new_label))

    return refactor_groups, remaining


def merge_clusters(clusters, indices):
    """
    Tujuan  : Menggabungkan hasil klasifikasi dari beberapa klaster OR sekaligus,
              dipakai untuk menghitung irisan antar klaster (rumus inclusion-exclusion).
    Input   : clusters (list semua klaster hasil classify_conditions),
              indices (index klaster mana saja yang mau digabung, contoh: (0, 1))
    Output  : refactor_groups & remaining_conditions gabungan dari klaster-klaster tersebut
    """
    merged_groups = {}
    merged_remaining = []
    for idx in indices:
        rg, rem = clusters[idx]
        for var, plist in rg.items():
            merged_groups.setdefault(var, [])
            for item in plist:
                if item not in merged_groups[var]:
                    merged_groups[var].append(item)
        for cond in rem:
            if cond not in merged_remaining:
                merged_remaining.append(cond)
    return merged_groups, merged_remaining


def build_match_and_where(base_match, refactor_groups, remaining_conditions):
    """
    Tujuan  : Membangun ulang klausa MATCH (dengan pola traversal baru) dan klausa WHERE
              (dengan sisa kondisi yang tidak direfaktor) untuk satu blok CALL().
    Input   : base_match (teks pola MATCH asli tanpa kata "MATCH"),
              refactor_groups & remaining_conditions (hasil dari classify_conditions/merge_clusters)
    Output  : match_clause (teks MATCH baru), where_clause (teks WHERE baru, bisa kosong)
    """
    match_clause = base_match
    extra_patterns = []

    for var_name, prop_list in refactor_groups.items():
        m_label = re.search(rf'\({var_name}:(\w+)\)', match_clause)
        node_label = m_label.group(1) if m_label else None
        is_movie = node_label in MOVIE_NODES

        if is_movie and prop_list:
            first_relation, first_label = prop_list[0]
            node_pattern = re.compile(rf'\({var_name}:{node_label}\)')
            matches_node = list(node_pattern.finditer(match_clause))
            if matches_node:
                insert_pos = matches_node[-1].end()
                insert_str = f"-[:{first_relation}]->(:{first_label})"
                match_clause = match_clause[:insert_pos] + insert_str + match_clause[insert_pos:]
            rest = prop_list[1:]
        else:
            rest = prop_list

        for relation, new_label in rest:
            extra_patterns.append(f"({var_name})-[:{relation}]->(:{new_label})")

    if extra_patterns:
        match_clause = match_clause + ", " + ", ".join(extra_patterns)

    where_clause = ""
    if remaining_conditions:
        where_clause = "WHERE " + " AND ".join(remaining_conditions)

    return match_clause, where_clause


def refactor_or_query(query):
    """
    Tujuan  : Merekonstruksi kueri yang klausa WHERE-nya mengandung OR di level teratas,
              menggunakan pendekatan inclusion-exclusion via banyak blok CALL().
    Input   : query (kueri Cypher lengkap, contoh: "MATCH (...) WHERE (A) OR (B) RETURN count(n1)")
    Output  : kueri baru berupa rangkaian CALL(){} + satu klausa RETURN penjumlahan/pengurangan
    """
    m = re.search(r'^MATCH\s+(.+?)\s*WHERE\s*(.+?)\s*RETURN\s*(.+)$',
                  query, re.IGNORECASE | re.DOTALL)
    if not m:
        return query

    base_match = m.group(1).strip()   # <-- sekarang TIDAK termasuk kata "MATCH" lagi
    where_content = m.group(2).strip()
    or_parts = split_by_keyword(where_content, 'OR')

    if len(or_parts) <= 1:
        return refactor_where_to_node(query)

    clusters = []
    for part in or_parts:
        stripped = strip_outer_parens(part)
        conditions = split_by_keyword(stripped, 'AND')
        conditions = [c.strip() for c in conditions if c.strip()]
        rg, rem = classify_conditions(conditions)
        clusters.append((rg, rem))

    n = len(clusters)
    call_blocks = []
    terms = []

    for r in range(1, n + 1):
        for combo in itertools.combinations(range(n), r):
            merged_groups, merged_remaining = merge_clusters(clusters, combo)
            match_clause, where_clause = build_match_and_where(
                base_match, merged_groups, merged_remaining
            )
            var_name = "t" + "".join(str(i + 1) for i in combo)
            lines = [f"CALL () {{", f"  MATCH {match_clause}"]
            if where_clause:
                lines.append(f"  {where_clause}")
            lines.append(f"  RETURN count(*) AS {var_name}")
            lines.append("}")
            call_blocks.append("\n".join(lines))
            sign = 1 if (r % 2 == 1) else -1
            terms.append((var_name, sign))

    formula_parts = []
    for i, (v, s) in enumerate(terms):
        if i == 0:
            formula_parts.append(v if s == 1 else f"-{v}")
        else:
            formula_parts.append(f"+ {v}" if s == 1 else f"- {v}")
    formula = " ".join(formula_parts)

    return "\n".join(call_blocks) + f"\nRETURN {formula} AS total"


def count_where_properties_full(query):
    """
    Tujuan  : Menghitung total kondisi filter properti dalam klausa WHERE,
              termasuk kueri yang memiliki beberapa klaster OR.
    Input   : query (kueri Cypher lengkap)
    Output  : jumlah total kondisi (integer)
    """
    m = re.search(r'WHERE\s*(.+?)\s*RETURN', query, re.IGNORECASE | re.DOTALL)
    if not m:
        return 0
    where_content = m.group(1).strip()
    or_parts = split_by_keyword(where_content, 'OR')
    total = 0
    for part in or_parts:
        stripped = strip_outer_parens(part)
        conditions = split_by_keyword(stripped, 'AND')
        total += len([c for c in conditions if c.strip()])
    return total


def refactor_query_full(query):
    """
    Tujuan  : Titik masuk utama proses rekonstruksi. Menentukan otomatis apakah
              kueri perlu ditangani lewat jalur OR (inclusion-exclusion) atau jalur AND biasa.
    Input   : query (kueri Cypher lengkap)
    Output  : kueri hasil rekonstruksi
    """
    m = re.search(r'WHERE\s*(.+?)\s*RETURN', query, re.IGNORECASE | re.DOTALL)
    if not m:
        return query
    where_content = m.group(1).strip()
    or_parts = split_by_keyword(where_content, 'OR')
    if len(or_parts) > 1:
        return refactor_or_query(query)
    return refactor_where_to_node(query)

def get_where_pattern(query_or_count):
    """
    Tujuan  : Menerjemahkan kueri (atau angka jumlah properti) menjadi label pola
              yang mudah dibaca manusia, contoh: "A AND B", "(A AND B) OR (C AND D)".
    Input   : query_or_count (bisa berupa teks kueri Cypher, atau angka int untuk mode lama)
    Output  : string label pola WHERE
    """
    # Backward compatibility: kalau dipanggil dengan angka (int), pakai mapping lama
    if isinstance(query_or_count, int):
        pola = {
            0: "-",
            1: "A",
            2: "A AND B",
            3: "A AND B AND C",
            4: "A AND B AND C AND D"
        }
        return pola.get(query_or_count, f"{query_or_count} kondisi")

    query = query_or_count

    # Kasus: kueri hasil refaktorisasi OR -> berupa banyak blok CALL{}
    if re.search(r'\bCALL\s*\{', query, re.IGNORECASE):
        where_blocks = re.findall(r'WHERE\s*(.+?)\s*RETURN', query, re.IGNORECASE | re.DOTALL)
        if not where_blocks:
            return "-"
        total_sisa = sum(
            len(split_by_keyword(strip_outer_parens(w), 'AND'))
            for w in where_blocks
        )
        return f"{total_sisa} kondisi tersisa (lintas cabang OR)"

    # Kasus: kueri linear biasa (baseline / hasil refaktor AND murni)
    m = re.search(r'WHERE\s*(.+?)\s*RETURN', query, re.IGNORECASE | re.DOTALL)
    if not m:
        return "-"

    where_content = m.group(1).strip()
    or_parts = split_by_keyword(where_content, 'OR')

    if len(or_parts) <= 1:
        jumlah = len([c for c in split_by_keyword(strip_outer_parens(where_content), 'AND') if c.strip()])
        return get_where_pattern(jumlah)  # panggil versi angka di atas untuk konsistensi label lama

    huruf = iter("ABCDEFGHIJKLMNOP")
    label_parts = []
    for part in or_parts:
        stripped = strip_outer_parens(part)
        conditions = split_by_keyword(stripped, 'AND')
        conditions = [c for c in conditions if c.strip()]
        huruf_klaster = [next(huruf) for _ in conditions]
        if len(huruf_klaster) > 1:
            label_parts.append("(" + " AND ".join(huruf_klaster) + ")")
        else:
            label_parts.append(huruf_klaster[0])

    return " OR ".join(label_parts)

def run_reconstruction():
    input_file  = "data/queries/Query_Where.txt"
    output_csv  = "data/queries/Query_PBN.csv"

    queries = read_queries_from_file(input_file)
    print(f"Berhasil membaca {len(queries)} query dari {input_file}\n")

    refactored_queries = []
    csv_data = []

    for i, query in enumerate(queries, 1):
        result = refactor_query_full(query)

        count_before = count_where_properties_full(query)
        count_after  = count_where_properties_full(result)
        pola = get_where_pattern(query)          # <-- manfaatkan get_where_pattern yang sudah ada

        if count_before > 0:
            penurunan = (count_before - count_after) / count_before * 100
            persentase = f"{penurunan:.0f}%"
        else:
            persentase = "0%"

        refactored_queries.append(result)
        csv_data.append({
            'Kueri Baseline'                    : query,
            'Kueri Refactored'                  : result,
            'Jumlah Properti WHERE Baseline'    : count_before,
            'Jumlah Properti WHERE Refactored'  : count_after,
            'Persentase Penurunan'              : persentase
        })

        print(f"Query {i} Input      : {query}")
        print(f"Query {i} Output     : {result}")
        print(f"         Pola            : {pola}")
        print(f"         WHERE Baseline  : {count_before} properti")
        print(f"         WHERE Refactored: {count_after} properti")
        print(f"         Penurunan       : {persentase}")
        print()

    save_queries_to_csv(csv_data, output_csv)
    print(f"Hasil disimpan ke {output_csv}")