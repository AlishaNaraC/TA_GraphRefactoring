# import csv
# import os
# from query.query_loader import QueryLoader
# from execution.db import DBConnection
# from reconstruction.query_reconstructor import get_where_pattern

# def run_baseline(input_file, output_csv):
#     loader  = QueryLoader(input_file)
#     queries = loader.load_queries()

#     db = DBConnection()

#     results = []
#     for i, q in enumerate(queries, 1):
#         query = q["query"]
#         print(f"Menjalankan query {i}/{len(queries)}...")

#         try:
#             result = db.run_profile(query)
#             results.append({
#                 "Kueri"         : query,
#                 "Jumlah Hasil"  : result["jumlah_hasil"],
#                 "DBHits"        : result["db_hits"],
#                 "Running Time"  : result["run_time"]
#             })
#             print(f"  Jumlah Hasil : {result['jumlah_hasil']}")
#             print(f"  DBHits       : {result['db_hits']}")
#             print(f"  Running Time : {result['run_time']} ms")

#         except TimeoutError as e:
#             print(f"  TIMEOUT pada query {i}: {e}")
#             results.append({
#                 "Kueri"        : query,
#                 "Jumlah Hasil" : "TIMEOUT",
#                 "DBHits"       : "TIMEOUT",
#                 "Running Time" : "TIMEOUT"
#             })
#         except Exception as e:
#             print(f"  ERROR pada query {i}: {e}")
#             results.append({
#                 "Kueri"        : query,
#                 "Jumlah Hasil" : "ERROR",
#                 "DBHits"       : "ERROR",
#                 "Running Time" : "ERROR"
#             })

#     db.close()

#     # Simpan ke CSV
#     os.makedirs(os.path.dirname(output_csv), exist_ok=True)
#     with open(output_csv, 'w', newline='', encoding='utf-8') as f:
#         fieldnames = ["Kueri", "Jumlah Hasil", "DBHits", "Running Time"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
#         # writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
#         writer.writeheader()
#         writer.writerows(results)

#     print(f"\nHasil disimpan ke {output_csv}")

# def run_refactored(input_csv, output_csv):
#     import csv
#     import os
#     from execution.db import DBConnection

#     # Baca CSV hasil refactoring
#     # PENTING: pakai delimiter ';' dan quoting QUOTE_ALL sesuai format CSV kita
#     rows = []
#     with open(input_csv, 'r', encoding='utf-8') as f:
#         reader = csv.DictReader(f, delimiter=';')
#         for row in reader:
#             rows.append(row)

#     db = DBConnection()
#     results = []

#     for i, row in enumerate(rows, 1):
#         kueri_asal       = row["Kueri Awal"]
#         kueri_refactored = row["Kueri Baru"]
#         jumlah_awal      = int(row["Jumlah Properti WHERE Awal"])
#         jumlah_baru      = int(row["Jumlah Properti WHERE Sesudah"])
#         persentase       = row["Persentase Penurunan"]

#         # Hitung pola
#         pola_awal = get_where_pattern(jumlah_awal)
#         pola_baru = get_where_pattern(jumlah_baru)

#         print(f"Menjalankan query {i}/{len(rows)}...")
#         print(f"  Pola: {pola_awal} -> {pola_baru}")

#         try:
#             result = db.run_profile(kueri_refactored, timeout_sec=300)
#             results.append({
#                 "Kueri Asal"             : kueri_asal,
#                 "Kueri Refactored"       : kueri_refactored,
#                 "Pola Properti Awal"     : pola_awal,
#                 "Pola Properti Baru"     : pola_baru,
#                 "Persentase Pengurangan" : persentase,
#                 "Jumlah Hasil"           : result["jumlah_hasil"],  # tambah ini
#                 "DBHits"                 : result["db_hits"],
#                 "Running Time"           : result["run_time"]
#             })
#             print(f"  Jumlah Hasil : {result['jumlah_hasil']}")
#             print(f"  DBHits       : {result['db_hits']}")
#             print(f"  Running Time : {result['run_time']} ms")

#         except TimeoutError as e:
#             print(f"  TIMEOUT pada query {i}: {e}")
#             results.append({
#                 "Kueri Asal"              : kueri_asal,
#                 "Kueri Refactored"        : kueri_refactored,
#                 "Pola Properti Awal"      : pola_awal,
#                 "Pola Properti Baru"      : pola_baru,
#                 "Persentase Pengurangan"  : persentase,
#                 "Jumlah Hasil"           : "TIMEOUT",
#                 "DBHits"                  : "TIMEOUT",
#                 "Running Time"            : "TIMEOUT"
#             })
#         except Exception as e:
#             print(f"  ERROR pada query {i}: {e}")
#             results.append({
#                 "Kueri Asal"              : kueri_asal,
#                 "Kueri Refactored"        : kueri_refactored,
#                 "Pola Properti Awal"      : pola_awal,
#                 "Pola Properti Baru"      : pola_baru,
#                 "Persentase Pengurangan"  : persentase,
#                 "Jumlah Hasil"            : "ERROR",
#                 "DBHits"                  : "ERROR",
#                 "Running Time"            : "ERROR"
#             })

#     db.close()

#     # Simpan ke CSV
#     os.makedirs(os.path.dirname(output_csv), exist_ok=True)
#     with open(output_csv, 'w', newline='', encoding='utf-8') as f:
#         fieldnames = [
#             "Kueri Asal", "Kueri Refactored", "Pola Properti Awal",
#             "Pola Properti Baru", "Persentase Pengurangan",
#             "Jumlah Hasil", "DBHits", "Running Time"  # tambah Jumlah Hasil
#         ]
#         writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
#         writer.writeheader()
#         writer.writerows(results)

#     print(f"\nHasil disimpan ke {output_csv}")

import csv
import os
from query.query_loader import QueryLoader
from execution.db import DBConnection
from reconstruction.pbn_query_reconstructor import get_where_pattern

REPEAT = 10  # Jumlah pengulangan eksekusi per kueri


def run_baseline(input_file, output_csv):
    loader  = QueryLoader(input_file)
    queries = loader.load_queries()

    db = DBConnection()

    results = []
    for i, q in enumerate(queries, 1):
        query = q["query"]
        print(f"Menjalankan query {i}/{len(queries)}...")

        db_hits      = None
        run_times    = []
        jumlah_hasil = None
        error_flag   = None

        for run in range(REPEAT):
            try:
                result = db.run_profile(query)
                print(f"  yang ke {run + 1}/{REPEAT}")
                if run == 0:
                    db_hits      = result["db_hits"]
                    jumlah_hasil = result["jumlah_hasil"]
                run_times.append(result["run_time"])

            except TimeoutError as e:
                print(f"  TIMEOUT: {e}")
                error_flag = "TIMEOUT"
                break
            except Exception as e:
                print(f"  ERROR: {e}")
                error_flag = "ERROR"
                break

        if error_flag:
            results.append({
                "Kueri"        : query,
                "Jumlah Hasil" : error_flag,
                "DBHits"       : error_flag,
                "Running Time" : error_flag,
            })
        else:
            avg_run_time = sum(run_times) / len(run_times)
            print(f"  Jumlah Hasil : {jumlah_hasil}")
            print(f"  DBHits       : {db_hits}")
            print(f"  Running Time : {round(avg_run_time, 4)} ms")
            results.append({
                "Kueri"        : query,
                "Jumlah Hasil" : jumlah_hasil,
                "DBHits"       : db_hits,
                "Running Time" : round(avg_run_time, 4),
            })

    db.close()

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Kueri", "Jumlah Hasil", "DBHits", "Running Time"]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nHasil disimpan ke {output_csv}")


def run_refactored(input_csv, output_csv):
    rows = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            rows.append(row)

    db = DBConnection()
    results = []

    for i, row in enumerate(rows, 1):
        kueri_asal       = row["Kueri Baseline"]
        kueri_refactored = row["Kueri Baru"]
        jumlah_awal      = int(row["Jumlah Properti WHERE Baseline"])
        jumlah_baru      = int(row["Jumlah Properti WHERE Refactored"])
        persentase       = row["Persentase Penurunan"]

        pola_awal = get_where_pattern(jumlah_awal)
        pola_baru = get_where_pattern(jumlah_baru)

        print(f"Menjalankan query {i}/{len(rows)}...")
        print(f"  Pola: {pola_awal} -> {pola_baru}")

        db_hits      = None
        run_times    = []
        jumlah_hasil = None
        error_flag   = None

        for run in range(REPEAT):
            try:
                result = db.run_profile(kueri_refactored, timeout_sec=300)
                print(f"  yang ke {run + 1}/{REPEAT}")
                if run == 0:
                    db_hits      = result["db_hits"]
                    jumlah_hasil = result["jumlah_hasil"]
                run_times.append(result["run_time"])

            except TimeoutError as e:
                print(f"  TIMEOUT: {e}")
                error_flag = "TIMEOUT"
                break
            except Exception as e:
                print(f"  ERROR: {e}")
                error_flag = "ERROR"
                break

        if error_flag:
            results.append({
                "Kueri Baseline"             : kueri_asal,
                "Kueri Refactored"       : kueri_refactored,
                "Pola Properti Awal"     : pola_awal,
                "Pola Properti Baru"     : pola_baru,
                "Persentase Pengurangan" : persentase,
                "Jumlah Hasil"           : error_flag,
                "DBHits"                 : error_flag,
                "Running Time"           : error_flag,
            })
        else:
            avg_run_time = sum(run_times) / len(run_times)
            print(f"  Jumlah Hasil : {jumlah_hasil}")
            print(f"  DBHits       : {db_hits}")
            print(f"  Running Time : {round(avg_run_time, 4)} ms")
            results.append({
                "Kueri Baseline"             : kueri_asal,
                "Kueri Refactored"       : kueri_refactored,
                "Pola Properti Awal"     : pola_awal,
                "Pola Properti Baru"     : pola_baru,
                "Persentase Pengurangan" : persentase,
                "Jumlah Hasil"           : jumlah_hasil,
                "DBHits"                 : db_hits,
                "Running Time"           : round(avg_run_time, 4),
            })

    db.close()

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            "Kueri Baseline", "Kueri Refactored", "Pola Properti Awal",
            "Pola Properti Baru", "Persentase Pengurangan",
            "Jumlah Hasil", "DBHits", "Running Time"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nHasil disimpan ke {output_csv}")