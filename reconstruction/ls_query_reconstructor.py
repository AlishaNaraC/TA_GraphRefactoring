import re
import csv

# Mapping properti ke format label baru
PROPERTY_LABEL_MAP = {
    "year":     {"label_format": "year_{val}"},
    "category": {"label_format": "{val}"},
    "death":    {"label_format": "death_{val}"},
    "birth":    {"label_format": "birth_{val}"},
}

# Baca semua query dari file txt, buang spasi/newline, skip baris kosong
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

# Hitung jumlah properti dalam klausa WHERE (sebelum dan sesudah refaktorisasi)
def count_where_properties(query):
    """
    Tujuan  : Menghitung jumlah kondisi filter properti dalam klausa WHERE (pola AND murni).
    Input   : query (kueri Cypher lengkap, contoh: "MATCH (...) WHERE (a.category='tvMovie') RETURN ...")
    Output  : jumlah kondisi (integer), 0 kalau tidak ada WHERE
    """
    where_block = re.search(r'WHERE\s*\((.+?)\)\s*RETURN', query, re.IGNORECASE)
    if not where_block:
        return 0

    where_content = where_block.group(1)
    conditions = [c.strip() for c in re.split(r'\s+AND\s+', where_content, flags=re.IGNORECASE)]
    return len([c for c in conditions if c])

def refactor_label_specification(query):
    """
    Tujuan  : Merekonstruksi kueri berpola AND murni — mengubah kondisi filter properti
              di WHERE (contoh: a.category='tvMovie') menjadi label tambahan langsung
              pada node yang sudah ada di MATCH (contoh: (a:adventure:tvMovie)), sesuai
              teknik label specification. Tidak ada relasi/node baru yang dibentuk.
    Input   : query (kueri Cypher lengkap)
    Output  : kueri hasil rekonstruksi (string)
    """
    where_block = re.search(r'WHERE\s*\((.+?)\)\s*RETURN', query, re.IGNORECASE)
    if not where_block:
        return query

    where_content = where_block.group(1)
    conditions = [c.strip() for c in re.split(r'\s+AND\s+', where_content, flags=re.IGNORECASE)]

    cond_pattern = re.compile(r'(\w+)\.(\w+)\s*=\s*["\']?(\w+)["\']?')

    extra_labels = {}
    remaining_conditions = []

    for cond in conditions:
        m = cond_pattern.match(cond)
        if not m:
            remaining_conditions.append(cond)
            continue

        var_name  = m.group(1)
        prop_name = m.group(2).lower()
        prop_val  = m.group(3)

        if prop_name not in PROPERTY_LABEL_MAP:
            remaining_conditions.append(cond)
            continue

        mapping   = PROPERTY_LABEL_MAP[prop_name]
        new_label = mapping["label_format"].format(val=prop_val)

        if var_name not in extra_labels:
            extra_labels[var_name] = []
        extra_labels[var_name].append(new_label)

    query_no_where = re.sub(r'\s*WHERE\s*\(.+?\)', '', query, flags=re.IGNORECASE).strip()

    # ── FIX: pisahkan MATCH dan RETURN dulu ──────────────────────────────
    match_return = re.match(r'(MATCH\s+.+?)\s*(RETURN\s+.+)$', query_no_where, re.IGNORECASE | re.DOTALL)
    if not match_return:
        return query_no_where

    match_part  = match_return.group(1)   # hanya bagian MATCH
    return_part = match_return.group(2)   # bagian RETURN dibiarkan utuh

    for var_name, labels in extra_labels.items():
        def replace_node(match):
            existing = match.group(0)
            inner    = existing[1:-1]
            suffix   = ":" + ":".join(labels)
            return f"({inner}{suffix})"

        # Hanya replace di match_part, bukan return_part
        node_pattern = re.compile(rf'\({re.escape(var_name)}(?::\w+)*\)')
        match_part = node_pattern.sub(replace_node, match_part)

    if remaining_conditions:
        leftover   = " AND ".join(remaining_conditions)
        return_part = re.sub(r'^(RETURN)', f'WHERE ({leftover}) \\1', return_part, flags=re.IGNORECASE)

    result = re.sub(r'\s{2,}', ' ', f"{match_part} {return_part}").strip()
    return result

# Simpan hasil ke CSV beserta statistik penurunan properti WHERE
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

import itertools

def split_by_keyword(text, keyword):
    """
    Tujuan  : Memecah teks WHERE menjadi beberapa bagian berdasarkan kata kunci AND/OR.
    Input   : text (contoh: "n1.category='tvSeries' OR n2.category='movie'"), keyword ("AND" atau "OR")
    Output  : list bagian teks yang sudah terpisah
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
    Input   : s (contoh: "(n1.category='tvSeries')")
    Output  : teks tanpa kurung luar
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


def classify_conditions_label(conditions):
    """
    Tujuan  : Memilah daftar kondisi WHERE ke dalam 2 kelompok: yang bisa direfaktor
              menjadi label baru, dan yang harus tetap di klausa WHERE.
    Input   : conditions (list kondisi, contoh: ["n1.category='tvSeries'", "n3.name='Budi'"])
    Output  : extra_labels (dict label baru per variabel node), remaining (list kondisi yang tetap di WHERE)
    """
    cond_pattern = re.compile(r'(\w+)\.(\w+)\s*=\s*["\']?(\w+)["\']?')
    extra_labels = {}
    remaining = []

    for cond in conditions:
        m = cond_pattern.match(cond)
        if not m:
            remaining.append(cond)
            continue

        var_name, prop_name, prop_val = m.group(1), m.group(2).lower(), m.group(3)

        if prop_name not in PROPERTY_LABEL_MAP:
            remaining.append(cond)
            continue

        mapping = PROPERTY_LABEL_MAP[prop_name]
        new_label = mapping["label_format"].format(val=prop_val)

        extra_labels.setdefault(var_name, [])
        if new_label not in extra_labels[var_name]:
            extra_labels[var_name].append(new_label)

    return extra_labels, remaining


def merge_label_clusters(clusters, indices):
    """
    Tujuan  : Menggabungkan hasil klasifikasi dari beberapa klaster OR sekaligus,
              dipakai untuk menghitung irisan antar klaster (rumus inclusion-exclusion).
    Input   : clusters (list semua klaster hasil classify_conditions_label),
              indices (index klaster mana saja yang mau digabung, contoh: (0, 1))
    Output  : extra_labels & remaining_conditions gabungan dari klaster-klaster tersebut
    """    
    merged_labels = {}
    merged_remaining = []
    for idx in indices:
        el, rem = clusters[idx]
        for var, labels in el.items():
            merged_labels.setdefault(var, [])
            for lbl in labels:
                if lbl not in merged_labels[var]:
                    merged_labels[var].append(lbl)
        for cond in rem:
            if cond not in merged_remaining:
                merged_remaining.append(cond)
    return merged_labels, merged_remaining


def build_match_label(base_match_part, extra_labels, remaining_conditions):
    """
    Tujuan  : Menempelkan label tambahan ke node yang sudah ada di MATCH (tanpa
              menambah relasi/node baru), lalu menyusun sisa kondisi ke WHERE.
    Input   : base_match_part (teks pola MATCH asli tanpa kata "MATCH"),
              extra_labels & remaining_conditions (hasil dari classify_conditions_label/merge_label_clusters)
    Output  : match_part (teks MATCH baru dengan label tambahan), where_clause (teks WHERE baru, bisa kosong)
    """
    match_part = base_match_part

    for var_name, labels in extra_labels.items():
        def replace_node(match, labels=labels):
            existing = match.group(0)
            inner = existing[1:-1]
            suffix = ":" + ":".join(labels)
            return f"({inner}{suffix})"

        node_pattern = re.compile(rf'\({re.escape(var_name)}(?::\w+)*\)')
        match_part = node_pattern.sub(replace_node, match_part)

    where_clause = ""
    if remaining_conditions:
        where_clause = "WHERE " + " AND ".join(remaining_conditions)

    return match_part, where_clause


def refactor_label_or_query(query):
    """
    Tujuan  : Merekonstruksi kueri yang klausa WHERE-nya mengandung OR di level teratas,
              menggunakan pendekatan inclusion-exclusion via banyak blok CALL(), khusus
              untuk teknik label specification (tanpa relasi/node baru).
    Input   : query (kueri Cypher lengkap, contoh: "MATCH (...) WHERE (A) OR (B) RETURN count(n1)")
    Output  : kueri baru berupa rangkaian CALL(){} + satu klausa RETURN penjumlahan/pengurangan
    """
    m = re.match(r'^MATCH\s+(.+?)\s*WHERE\s*(.+?)\s*RETURN\s*(.+)$',
                 query, re.IGNORECASE | re.DOTALL)
    if not m:
        return query

    base_match = m.group(1).strip()   # tanpa kata "MATCH"
    where_content = m.group(2).strip()

    or_parts = split_by_keyword(where_content, 'OR')

    # Kalau tidak ada OR di level teratas -> pola AND murni, pakai fungsi lama
    if len(or_parts) <= 1:
        return refactor_label_specification(query)

    clusters = []
    for part in or_parts:
        stripped = strip_outer_parens(part)
        conditions = split_by_keyword(stripped, 'AND')
        conditions = [c.strip() for c in conditions if c.strip()]
        el, rem = classify_conditions_label(conditions)
        clusters.append((el, rem))

    n = len(clusters)
    call_blocks = []
    terms = []

    for r in range(1, n + 1):
        for combo in itertools.combinations(range(n), r):
            merged_labels, merged_remaining = merge_label_clusters(clusters, combo)
            match_part, where_clause = build_match_label(
                base_match, merged_labels, merged_remaining
            )
            var_name = "t" + "".join(str(i + 1) for i in combo)
            lines = [f"CALL () {{", f"  MATCH {match_part}"]
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

def refactor_label_query_full(query):
    """
    Tujuan  : Titik masuk utama proses rekonstruksi label specification. Menentukan
              otomatis apakah kueri perlu ditangani lewat jalur OR (inclusion-exclusion)
              atau jalur AND biasa.
    Input   : query (kueri Cypher lengkap)
    Output  : kueri hasil rekonstruksi
    """
    m = re.search(r'WHERE\s*(.+?)\s*RETURN', query, re.IGNORECASE | re.DOTALL)
    if not m:
        return query
    where_content = m.group(1).strip()
    or_parts = split_by_keyword(where_content, 'OR')
    if len(or_parts) > 1:
        return refactor_label_or_query(query)
    return refactor_label_specification(query)

def run_reconstruction_label_specification():
    input_file  = "data/queries/Query_Where.txt"
    output_csv  = "data/queries/Query_LS.csv"

    queries = read_queries_from_file(input_file)
    print(f"Berhasil membaca {len(queries)} query dari {input_file}\n")

    refactored_queries = []
    csv_data = []

    for i, query in enumerate(queries, 1):
        result = refactor_label_query_full(query)              
        count_before = count_where_properties_full(query)
        count_after  = count_where_properties_full(result) 

        if count_before > 0:
            penurunan  = (count_before - count_after) / count_before * 100
            persentase = f"{penurunan:.0f}%"
        else:
            persentase = "0%"

        refactored_queries.append(result)
        csv_data.append({
            'Kueri Baseline'                : query,
            'Kueri Refactored'                    : result,
            'Jumlah Properti WHERE Baseline'    : count_before,
            'Jumlah Properti WHERE Refactored' : count_after,
            'Persentase Penurunan'          : persentase
        })

        print(f"Query {i} Input      : {query}")
        print(f"Query {i} Output     : {result}")
        print(f"         WHERE Baseline  : {count_before} properti")
        print(f"         WHERE Refactored  : {count_after} properti")
        print(f"         Penurunan   : {persentase}")
        print()

    save_queries_to_csv(csv_data, output_csv)
    print(f"Hasil disimpan ke {output_csv}")
