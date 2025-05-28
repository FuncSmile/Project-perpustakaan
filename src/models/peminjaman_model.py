# Model untuk peminjaman
import os
import csv

DATA_DIR = "src/data"
PEMINJAMAN_FILE = os.path.join(DATA_DIR, "peminjaman.csv")

def load_peminjaman():
    if not os.path.exists(PEMINJAMAN_FILE):
        return []
    with open(PEMINJAMAN_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_peminjaman(data):
    fieldnames = ["id_pinjam", "id_buku", "id_member","judul", "penulis", "tanggal_pinjam", "tanggal_kembali"]
    with open(PEMINJAMAN_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
