import csv
import os
from datetime import datetime, timedelta
from tabulate import tabulate

DATA_DIR = "data"
BUKU_FILE = os.path.join(DATA_DIR, "buku.csv")
MEMBER_FILE = os.path.join(DATA_DIR, "member.csv")
PEMINJAMAN_FILE = os.path.join(DATA_DIR, "peminjaman.csv")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ====== UTILITAS ======
def auto_id(data, prefix, key):
    """Generate auto-increment ID dengan prefix tertentu."""
    nomor = 1
    existing_ids = {d[key] for d in data}
    while True:
        id_baru = f"{prefix}{str(nomor).zfill(3)}"
        if id_baru not in existing_ids:
            return id_baru
        nomor += 1

def read_csv(filepath, fieldnames=None):
    if not os.path.exists(filepath):
        return []
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(filepath, data, fieldnames):
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# ====== BUKU ======
def load_buku():
    return read_csv(BUKU_FILE)

def save_buku(data):
    fieldnames = ["id", "judul", "penulis"]
    write_csv(BUKU_FILE, data, fieldnames)

def tampilkan_buku(data_buku=None):
    if data_buku is None:
        data_buku = load_buku()
    if not data_buku:
        print("Tidak ada data buku.")
    else:
        print(tabulate(data_buku, headers="keys", tablefmt="grid"))

# ====== MEMBER ======
def load_member():
    return read_csv(MEMBER_FILE)

def save_member(data):
    fieldnames = ["id_member", "nama", "email", "no_hp"]
    write_csv(MEMBER_FILE, data, fieldnames)

def tampilkan_member():
    data_member = load_member()
    if not data_member:
        print("Tidak ada member terdaftar.")
    else:
        print(tabulate(data_member, headers="keys", tablefmt="grid"))

def register_member():
    data_member = load_member()
    tampilkan_member()
    if not data_member:
        print("Tidak ada member terdaftar. Silakan daftar member baru.")
    id_member = auto_id(data_member, prefix="M", key="id_member")
    nama = input("Masukkan Nama Member: ").upper()
    email = input("Masukkan Email Member: ").lower()
    no_hp = input("Masukkan Nomor HP Member: ")
    data_member.append({
        "id_member": id_member,
        "nama": nama,
        "email": email,
        "no_hp": no_hp
    })
    save_member(data_member)
    print(f"✅ Member berhasil terdaftar dengan ID: {id_member}")

# ====== PEMINJAMAN ======
def load_peminjaman():
    return read_csv(PEMINJAMAN_FILE)

def save_peminjaman(data):
    fieldnames = ["id_pinjam", "id_buku", "judul", "penulis", "tanggal_pinjam", "tanggal_kembali"]
    write_csv(PEMINJAMAN_FILE, data, fieldnames)

def tampilkan_peminjaman():
    data = load_peminjaman()
    if not data:
        print("Tidak ada data peminjaman.")
    else:
        print(tabulate(data, headers="keys", tablefmt="grid"))

def pinjam_buku():
    data_buku = load_buku()
    if not data_buku:
        print("Tidak ada buku tersedia.")
        return
    tampilkan_buku(data_buku)
    id_buku = input("Masukkan ID Buku yang ingin dipinjam: ").upper()
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
        print("1. Daftar Member")
        print("2. Pinjam Buku")
        print("3. Lihat Semua Peminjaman")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == '1':
            register_member()
        elif pilihan == '2':
            pinjam_buku()
        elif pilihan == '3':
            tampilkan_peminjaman()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")
