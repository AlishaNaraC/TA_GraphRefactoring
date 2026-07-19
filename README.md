# TA_GraphRefactoring

Aplikasi Pendukung Eksperimen (APE) untuk menganalisis pengaruh teknik refaktorisasi skema data _directed multigraph_ (**Property Becoming a Node** dan **Label Specification**) terhadap beban kerja logis (_DBHits_) dan waktu eksekusi (_running time_) kueri Cypher pada Neo4j, menggunakan dataset IMDb.

## Daftar Isi

- [Prasyarat](#prasyarat)
- [Instalasi](#instalasi)
- [Konfigurasi](#konfigurasi)
- [Struktur Proyek](#struktur-proyek)
- [Alur Penggunaan](#alur-penggunaan)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Penjelasan Tiap Menu](#penjelasan-tiap-menu)
- [Catatan Penting](#catatan-penting)

## Prasyarat

Sebelum menjalankan aplikasi ini, pastikan hal-hal berikut sudah tersedia:

1. **Python** sudah terinstal (disarankan versi 3.10 ke atas, karena kode menggunakan `match-case`).
2. **Neo4j** sudah terinstal (Neo4j Desktop atau Neo4j Server) dan sudah dibuat satu _instance_/database yang akan digunakan untuk menyimpan data.
3. **Plugin APOC** sudah terpasang pada instance Neo4j tersebut (dibutuhkan untuk operasi refaktorisasi seperti `apoc.merge.node`, `apoc.merge.relationship`, `apoc.create.addLabels`).
4. Dataset IMDb (`Peoples.csv`, `Movies.csv`, `Edges.csv`) serta file kueri (`Query_Where.txt`) sudah tersedia di lokasi yang sesuai dengan path yang dipakai di kode.

## Instalasi

1. Clone repository ini:

   ```bash
   git clone https://github.com/AlishaNaraC/TA_GraphRefactoring.git
   cd TA_GraphRefactoring
   ```

2. (Disarankan) Buat virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependency yang dibutuhkan, minimal:
   ```bash
   pip install neo4j
   ```
   > Jika repo ini punya file `requirements.txt`, gunakan `pip install -r requirements.txt` sebagai gantinya.

## Konfigurasi

Sebelum menjalankan aplikasi, buka file **`config.py`** dan sesuaikan `NEO4J_CONFIG` dengan pengaturan instance Neo4j yang kamu gunakan, misalnya:

- URI koneksi (contoh: `bolt://localhost:7687`)
- Username & password
- Nama database yang dipakai

Pastikan juga nilai `DB` yang diimpor dari `config.py` sudah mengarah ke database yang benar sebelum menjalankan proses import maupun eksperimen.

> **Catatan:** sesuaikan isi `config.py` ini dengan struktur konfigurasi yang ada di file kamu sendiri — nama variabel/field bisa saja sedikit berbeda tergantung implementasi terakhir.

## Struktur Proyek

```
config.py                     # Konfigurasi koneksi Neo4j
main.py                       # Entry point aplikasi (menu interaktif)
delete_db_content.py          # Utility untuk membersihkan isi database
test_db_connection.py         # Utility untuk mengecek koneksi ke Neo4j
data/
    queries/                  # File kueri baseline & hasil rekonstruksi
    report/                   # Hasil eksperimen (statistik, validasi, eksekusi)
execution/
    db.py                     # Koneksi & eksekusi PROFILE ke Neo4j
    runner.py                 # Menjalankan kueri baseline/refactored & mencatat DBHits, running time
importer/
    neo4j_importer.py         # Import data IMDb (nodes & edges) ke Neo4j
    schema_initializer.py     # Pembuatan index
    label_manager.py          # Pengelolaan label sementara saat import
query/
    query_loader.py           # Membaca daftar kueri dari file
reconstruction/
    pbn_query_reconstructor.py # Rekonstruksi kueri teknik Property Becoming a Node
    ls_query_reconstructor.py  # Rekonstruksi kueri teknik Label Specification
refactor/
    refactor_manager.py        # Orkestrasi proses refaktorisasi skema data
    property_becoming_node.py  # Implementasi refaktorisasi PBN
    label_specification.py     # Implementasi refaktorisasi LS
    identify_candidate_property.py # Identifikasi kandidat properti (DVR)
validation/
    validation_baseline.py                 # Pencatatan statistik skema baseline
    validation_property_becoming_a_node.py # Validasi hasil refaktorisasi PBN
    validation_label_specification.py      # Validasi hasil refaktorisasi LS
```

## Alur Penggunaan

Karena refaktorisasi mengubah skema data secara langsung (mengubah/menghapus properti, menambah label atau relasi), **urutan menjalankan menu sangat penting**. Alur yang direkomendasikan:

```
1 → Import data IMDb ke Neo4j
6 → Catat statistik baseline (WAJIB sebelum refaktorisasi, karena
     properti akan dihapus/berubah setelah refaktorisasi dijalankan)
9 → Jalankan kueri baseline (catat DBHits & running time sebelum refaktorisasi)

--- pilih salah satu teknik ---

2 → Refaktor database (Property Becoming a Node)
3 → Rekonstruksi kueri (Property Becoming a Node)
7 → Validasi hasil refaktorisasi PBN
10 → Jalankan kueri hasil rekonstruksi PBN

  ATAU

4 → Refaktor database (Label Specification)
5 → Rekonstruksi kueri (Label Specification)
8 → Validasi hasil refaktorisasi LS
11 → Jalankan kueri hasil rekonstruksi LS
```

> **Penting:** karena refaktorisasi PBN dan LS sama-sama mengubah skema data yang sama di database yang sama, kamu tidak bisa menjalankan eksperimen kedua teknik ini secara berurutan pada database yang sama tanpa mengembalikan data ke kondisi baseline terlebih dahulu (misalnya dengan membersihkan isi database menggunakan `delete_db_content.py` lalu mengimpor ulang data dari awal, atau menyiapkan instance/database terpisah untuk tiap teknik).

## Menjalankan Aplikasi

1. Buka terminal pada VS Code (atau terminal lain) di root folder proyek.
2. Jalankan:
   ```bash
   py main.py
   ```
   atau, tergantung sistem operasi/alias Python yang terpasang:
   ```bash
   python main.py
   ```
3. Aplikasi akan menampilkan menu berikut:
   ```
   Pilih mode eksekusi:
   1. Import skema data
   -------------------------------
   2. Refaktor database (property becoming a node)
   3. Rekonstruksi kueri (property becoming a node)
   4. Refaktor database (label specification)
   5. Rekonstruksi kueri (label specification)
   -------------------------------
   6. Baca statistik baseline (sebelum refaktorisasi)
   7. Validasi refaktorisasi (property becoming a node)
   8. Validasi refaktorisasi (label specification)
   -------------------------------
   9. Jalankan kueri baseline
   10. Jalankan kueri refactored (property becoming a node)
   11. Jalankan kueri refactored (label specification)
   ```
4. Masukkan angka sesuai menu yang ingin dijalankan, lalu tekan Enter.
5. Ulangi langkah 2–4 untuk menjalankan tahapan berikutnya sesuai alur pada bagian [Alur Penggunaan](#alur-penggunaan).

## Penjelasan Tiap Menu

| No  | Menu                            | Fungsi                                                                                                                                                                            | Output                                                         |
| --- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 1   | Import skema data               | Mengimpor `Movies.csv`, `Peoples.csv`, dan `Edges.csv` ke Neo4j, membuat index, lalu menghapus label sementara (`TMP_PEOPLES`, `TMP_MOVIES`) yang dipakai saat proses import edge | Data tersimpan di database Neo4j                               |
| 2   | Refaktor database (PBN)         | Menjalankan `RefactorManager(technique="pbn")` untuk mentransformasikan properti kandidat (`category`, `year`, `birth`, `death`) menjadi node dan relasi baru                     | Skema database berubah                                         |
| 3   | Rekonstruksi kueri (PBN)        | Membaca kueri dari `data/queries/Query_Where.txt`, merekonstruksi klausa WHERE menjadi pola traversal MATCH sesuai skema PBN                                                      | `data/queries/Query_PBN.csv`                                   |
| 4   | Refaktor database (LS)          | Menjalankan `RefactorManager(technique="ls")` untuk menambahkan label baru pada node berdasarkan nilai properti kandidat                                                          | Skema database berubah                                         |
| 5   | Rekonstruksi kueri (LS)         | Merekonstruksi kueri sesuai skema hasil Label Specification                                                                                                                       | `data/queries/Query_LS.csv`                                    |
| 6   | Baca statistik baseline         | Mencatat jumlah node, nilai unik, dan distribusi tiap properti kandidat **sebelum** refaktorisasi dilakukan                                                                       | `data/report/validation/baseline_property_stats.csv` / `.json` |
| 7   | Validasi refaktorisasi (PBN)    | Membandingkan statistik baseline dengan hasil refaktorisasi PBN untuk memastikan tidak ada data yang hilang                                                                       | `data/report/validation/validasi_property_becoming_node.csv`   |
| 8   | Validasi refaktorisasi (LS)     | Membandingkan statistik baseline dengan hasil refaktorisasi LS                                                                                                                    | `data/report/validation/validasi_label_specification.csv`      |
| 9   | Jalankan kueri baseline         | Menjalankan seluruh kueri pada `Query_Where.txt` ke skema baseline (belum direfaktor), mencatat DBHits & running time                                                             | `data/report/baseline/executed_190_baseline.csv`               |
| 10  | Jalankan kueri refactored (PBN) | Menjalankan kueri hasil rekonstruksi dari `Query_PBN.csv` ke skema hasil PBN                                                                                                      | `data/report/property_becoming_node/executed_190_PBN.csv`      |
| 11  | Jalankan kueri refactored (LS)  | Menjalankan kueri hasil rekonstruksi dari `Query_LS.csv` ke skema hasil LS                                                                                                        | `data/report/label_specification/hasil_refactored_LS.csv`      |

## Catatan Penting

- **Path file bersifat statis di dalam kode.** Nama dan lokasi file input/output untuk tahap rekonstruksi kueri (menu 3, 5, 9, 10, 11) sudah ditulis langsung (_hardcoded_) di `main.py` dan file-file terkait di folder `reconstruction/` serta `execution/runner.py`. Periksa kembali apakah path tersebut (misalnya `data/queries/Query_Where.txt`, `data/queries/Query_PBN.csv`) sudah sesuai dengan file yang kamu miliki sebelum menjalankan menu terkait.
- **Siapkan database untuk menyimpan hasil backup refaktorisasi** Backup disipakan dalam satu instance saja, jadi dalam satu instance sudah dibuat beberapa data baseline yang tujuannya untuk di refaktorisasi, karena refaktorisasi memerlukan waktu yang sangat panjang
- **Proses refaktorisasi bisa dilanjutkan jika berhenti** Kalau baterai habis, atau laptop mau dimatikan dulu, tenang saja, proses refaktorisasi bisa dilanjutin lagi kok
- **Urutan menjalankan menu berpengaruh terhadap hasil.** Statistik baseline (menu 6) dan eksekusi kueri baseline (menu 9) harus dilakukan **sebelum** menjalankan refaktorisasi (menu 2 atau 4), karena setelah refaktorisasi properti kandidat akan dihapus/berubah dari skema.
- **Satu database untuk satu teknik dalam satu waktu.** Jangan menjalankan refaktorisasi PBN dan LS secara bergantian pada database yang sama tanpa mengembalikan data ke kondisi awal (baseline) terlebih dahulu.
- **Cek koneksi terlebih dahulu.** Gunakan `test_db_connection.py` untuk memastikan koneksi ke Neo4j sudah berhasil sebelum menjalankan `main.py`.
- **Membersihkan database.** Gunakan `delete_db_content.py` apabila perlu mengosongkan database sebelum mengulang proses import/eksperimen dari awal — periksa isi file tersebut untuk memastikan cakupan penghapusannya (seluruh data atau sebagian) sebelum dijalankan.
