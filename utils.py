import csv
import os
from datetime import datetime, timedelta
from tabulate import tabulate

if not os.path.exists("data"):
    os.makedirs("data")

# ====== BUKU ======
def load_data():
    if not os.path.exists("data/buku.csv"):
        return []
    with open("data/buku.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_data(data):
    with open("data/buku.csv", mode='w', newline='') as file:
        fieldnames = ["id", "judul", "penulis"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def tampilkan_buku(data_buku):
    if not data_buku:
        print("Tidak ada data buku.")
    else:
        print(tabulate(data_buku, headers="keys", tablefmt="grid"))

def auto_id(data, prefix, key):
    nomor = 1
    existing_ids = {d[key] for d in data}
    while True:
        id_baru = f"{prefix}{str(nomor).zfill(3)}"
        if id_baru not in existing_ids:
            return id_baru
        nomor += 1

# ====== PEMINJAMAN ======

if not os.path.exists("data"):
    os.makedirs("data")

def load_peminjaman():
    if not os.path.exists("data/peminjaman.csv"):
        return []
    with open("data/peminjaman.csv", mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_peminjaman(data):
    with open("data/peminjaman.csv", mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["id_pinjam", "id_buku", "judul", "penulis", "tanggal_pinjam", "tanggal_kembali"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def tampilkan_peminjaman():
    data = load_peminjaman()
    if not data:
        print("Tidak ada data peminjaman.")
    else:
        print(tabulate(data, headers="keys", tablefmt="grid"))

def pinjam_buku():
    data_buku = load_data()
    if not data_buku:
        print("Tidak ada buku tersedia.")
        return

    tampilkan_buku(data_buku)
    id_buku = input("Masukkan ID Buku yang ingin dipinjam: ")

    buku_dipilih = next((b for b in data_buku if b["id"] == id_buku), None)
    if not buku_dipilih:
        print("❌ Buku tidak ditemukan.")
        return

    data_pinjam = load_peminjaman()
    id_pinjam = auto_id(data_pinjam, prefix="P", key="id_pinjam")
    tanggal_pinjam = datetime.today().strftime("%Y-%m-%d")
    tanggal_kembali = (datetime.today() + timedelta(days=7)).strftime("%Y-%m-%d")

    data_pinjam.append({
        "id_pinjam": id_pinjam,
        "id_buku": buku_dipilih["id"],
        "judul": buku_dipilih["judul"],
        "penulis": buku_dipilih["penulis"],
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali
    })

    save_peminjaman(data_pinjam)
    print(f"✅ Buku berhasil dipinjam. Tanggal kembali: {tanggal_kembali}")

# ====== MENU KASIR ======

def menu_kasir():
    while True:
        print("\n=== Menu Kasir Perpustakaan ===")
        print("1. Pinjam Buku")
        print("2. Lihat Semua Peminjaman")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            pinjam_buku()
        elif pilihan == '2':
            tampilkan_peminjaman()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")
