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
    with open(file_path, 'r') as f:
        lines = f.readlines()
    queries = [line.strip() for line in lines if line.strip()]
    return queries

# Hitung jumlah properti dalam klausa WHERE (sebelum dan sesudah refaktorisasi)
def count_where_properties(query):
    """Hitung jumlah properti dalam klausa WHERE"""
    where_block = re.search(r'WHERE\s*\((.+?)\)\s*RETURN', query, re.IGNORECASE)
    if not where_block:
        return 0

    where_content = where_block.group(1)
    conditions = [c.strip() for c in re.split(r'\s+AND\s+', where_content, flags=re.IGNORECASE)]
    return len([c for c in conditions if c])

def refactor_label_specification(query):
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

# Simpan hasil query ke file txt
def save_queries_to_file(queries, file_path):
    with open(file_path, 'w') as f:
        for query in queries:
            f.write(query + '\n')

# Simpan hasil ke CSV beserta statistik penurunan properti WHERE
def save_queries_to_csv(data, file_path):
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

def run_reconstruction_label_specification():
    input_file  = "data/queries/Query_Where_80.txt"
    output_txt  = "data/queries/Query_LabelSpec_Refactored.txt"
    output_csv  = "data/queries/Query_LabelSpec_Refactored.csv"

    queries = read_queries_from_file(input_file)
    print(f"Berhasil membaca {len(queries)} query dari {input_file}\n")

    refactored_queries = []
    csv_data = []

    for i, query in enumerate(queries, 1):
        result = refactor_label_specification(query)

        count_before = count_where_properties(query)
        count_after  = count_where_properties(result)

        if count_before > 0:
            penurunan  = (count_before - count_after) / count_before * 100
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


# ── Quick test tanpa file ──────────────────────────────────────────────────────
if __name__ == "__main__":
    test_queries = [
        "MATCH (a:adventure) WHERE (a.category = 'tvMovie') RETURN a",
        "MATCH (a:drama) WHERE (a.year = 1999) RETURN a",
        "MATCH (a:actor) WHERE (a.death = 2000) RETURN a",
        "MATCH (a:director) WHERE (a.birth = 1995) RETURN a",
        "MATCH (a:drama) WHERE (a.year = 1999 AND a.category = 'movie') RETURN a",
    ]

    print("=" * 70)
    print("QUICK TEST - Label Specification Refactoring")
    print("=" * 70 + "\n")

    for i, q in enumerate(test_queries, 1):
        result = refactor_label_specification(q)
        before = count_where_properties(q)
        after  = count_where_properties(result)
        pct    = f"{(before - after) / before * 100:.0f}%" if before > 0 else "0%"

        print(f"[{i}] Input  : {q}")
        print(f"    Output : {result}")
        print(f"    WHERE  : {before} → {after} properti ({pct} turun)")
        print()