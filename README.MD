
# BUDAYAKAN MEMBACA README ‼️‼️‼️
# 📚 Project Perpustakaan Kasir – Struktur Data (Python + CSV)

## 🧾 Deskripsi  
Aplikasi sederhana untuk pengelolaan data buku dan peminjaman di perpustakaan, menggunakan bahasa **Python** dan menyimpan data di file **CSV**. Program ini memiliki fitur CRUD buku, pencatatan peminjaman, serta tanggal otomatis pinjam dan pengembalian (7 hari kemudian).

## 📁 Struktur Folder & File

```
projectPerpustakaan/
│
├── main.py          # Program utama (menu & alur aplikasi)
├── crud.py          # Fungsi CRUD buku (tambah, lihat, ubah, hapus)
├── utils.py         # Fungsi bantu: load/save CSV, auto ID, peminjaman
├── data.csv         # File penyimpanan data buku (otomatis dibuat)
├── peminjaman.csv   # File data peminjaman buku (otomatis dibuat)
└── README.md        # Dokumentasi project
```

## ⚙️ Kebutuhan

- Python versi 3.x  
-  `csv` dan `datetime` dari Python standar library dan tabulate dari pip

## cara install 
```bash
pip install -r requirements.txt

````

## ▶️ Cara Menjalankan

1. **Clone/download** project ini ke komputer kamu.
2. Buka terminal/command prompt, arahkan ke folder project:

```bash
cd path/to/projectPerpustakaan
```

3. Jalankan program utama:

```bash
source venv/Scripts/activate
python main.py
```

> Kalau pakai IDLE atau VSCode, cukup buka dan jalankan `main.py`.

## 📌 Fitur Program

### ✅ CRUD Buku
- Tambah buku baru (dengan ID otomatis seperti `B001`, `B002`)
- Lihat semua data buku
- Ubah informasi buku
- Hapus buku dari perpustakaan

### 📖 Peminjaman Buku
- Pinjam buku dengan memasukkan ID buku
- Tanggal peminjaman dicatat otomatis
- Tanggal pengembalian otomatis dihitung 7 hari setelah tanggal pinjam
- Lihat semua daftar peminjaman

## 📝 Format File CSV

### `data.csv`
| id   | judul           | penulis    |
|------|------------------|------------|
| B001 | Laskar Pelangi  | Andrea Hirata |

### `peminjaman.csv`
| id_pinjam | id_buku | judul           | penulis        | tanggal_pinjam | tanggal_kembali |
|-----------|---------|------------------|----------------|----------------|-----------------|
| P001      | B001    | Laskar Pelangi  | Andrea Hirata | 2025-05-28     | 2025-06-04      |

## 🧠 Catatan

- Semua data disimpan di file `.csv`, jadi program bisa langsung dijalankan tanpa database.
- ID untuk buku dan peminjaman dibuat otomatis agar tidak duplikat.
- File `.csv` akan dibuat otomatis saat pertama kali program dijalankan jika belum ada.
