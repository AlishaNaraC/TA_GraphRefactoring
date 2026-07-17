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

# Simpan hasil ke CSV beserta statistik penurunan properti WHERE
def save_queries_to_csv(data, file_path):
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

# ============================================================
# BAGIAN BARU: Parsing OR untuk Label Specification
# ============================================================

def split_by_keyword(text, keyword):
    """Split teks berdasarkan keyword (OR/AND) HANYA di level kurung terluar (depth==0)."""
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
    """Buang kurung pembungkus terluar jika memang membungkus seluruh string."""
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
    Sama seperti logika di refactor_label_specification(), dipisah supaya
    reusable per klaster OR. Return: (extra_labels: {var: [label, ...]}, remaining: [str])
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
    """Gabungkan extra_labels & remaining_conditions dari beberapa klaster OR (untuk hitung irisan)."""
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
    Tempelkan label tambahan ke node yang sudah ada di match_part (tanpa
    menambah relasi baru), lalu susun WHERE untuk kondisi yang tersisa.
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
    Menangani WHERE dengan OR di level teratas untuk teknik label specification,
    via inclusion-exclusion CALL(){}.
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
    """Versi count_where_properties() yang paham OR: total kondisi dijumlah lintas klaster."""
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
    """Dispatcher utama: deteksi OR di level teratas, arahkan ke fungsi yang sesuai."""
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


# # ── Quick test tanpa file ──────────────────────────────────────────────────────
# if __name__ == "__main__":
#     test_queries = [
#         "MATCH (a:adventure) WHERE (a.category = 'tvMovie') RETURN a",
#         "MATCH (a:drama) WHERE (a.year = 1999) RETURN a",
#         "MATCH (a:actor) WHERE (a.death = 2000) RETURN a",
#         "MATCH (a:director) WHERE (a.birth = 1995) RETURN a",
#         "MATCH (a:drama) WHERE (a.year = 1999 AND a.category = 'movie') RETURN a",
#     ]

#     print("=" * 70)
#     print("QUICK TEST - Label Specification Refactoring")
#     print("=" * 70 + "\n")

#     for i, q in enumerate(test_queries, 1):
#         result = refactor_label_specification(q)
#         before = count_where_properties(q)
#         after  = count_where_properties(result)
#         pct    = f"{(before - after) / before * 100:.0f}%" if before > 0 else "0%"

#         print(f"[{i}] Input  : {q}")
#         print(f"    Output : {result}")
#         print(f"    WHERE  : {before} → {after} properti ({pct} turun)")
#         print()