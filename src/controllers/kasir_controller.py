# Controller untuk menu kasir dan transaksi member/peminjaman
from src.models.buku_model import load_buku
from src.models.member_model import load_member, save_member, auto_id
from src.models.peminjaman_model import load_peminjaman, save_peminjaman
from src.views.buku_view import tampilkan_buku
from src.views.member_view import tampilkan_member
from src.views.peminjaman_view import tampilkan_peminjaman
from datetime import datetime, timedelta


def register_member():
    data_member = load_member()
    tampilkan_member()
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


def pinjam_buku():
    data_buku = load_buku()
    if not data_buku:
        print("Tidak ada buku tersedia.")
        return
    tampilkan_buku(data_buku)
    id_buku = input("Masukkan ID Buku yang ingin dipinjam: ").upper()
    id_member = input("Masukkan ID Member yang meminjam: ").upper()
    data_member = load_member()
    buku_dipilih = next((b for b in data_buku if b["id"] == id_buku), None)
    if not buku_dipilih:
        print("❌ Buku tidak ditemukan.")
        return
    if not any(m["id_member"] == id_member for m in data_member):
        print("❌ Member tidak ditemukan.")
        return
    data_pinjam = load_peminjaman()
    id_pinjam = auto_id(data_pinjam, prefix="P", key="id_pinjam")
    tanggal_pinjam = datetime.today().strftime("%Y-%m-%d")
    tanggal_kembali = (datetime.today() + timedelta(days=7)).strftime("%Y-%m-%d")
    data_pinjam.append({
        "id_pinjam": id_pinjam,
        "id_buku": buku_dipilih["id"],
        "id_member": id_member,
        "judul": buku_dipilih["judul"],
        "penulis": buku_dipilih["penulis"],
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali
    })
    save_peminjaman(data_pinjam)
    print(f"✅ Buku berhasil dipinjam. Tanggal kembali: {tanggal_kembali}")


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
