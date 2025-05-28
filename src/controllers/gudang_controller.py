# Controller untuk menu gudang (CRUD buku)
from src.models.buku_model import load_buku, save_buku
from src.views.buku_view import tampilkan_buku
from src.models.member_model import auto_id


def menu_gudang():
    while True:
        data = load_buku()  # Load data setiap awal loop
        print("\n=== Menu Gudang Buku ===")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Ubah Buku")
        print("4. Hapus Buku")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            id_baru = auto_id(data, prefix="B", key="id")
            judul = input("Masukkan Judul Buku: ").upper()
            penulis = input("Masukkan Penulis Buku: ").upper()
            if not judul or not penulis:
                print("❌ Judul dan penulis tidak boleh kosong.")
                continue
            data.append({"id": id_baru, "judul": judul, "penulis": penulis})
            save_buku(data)
            print("✅ Buku berhasil ditambahkan.")
        elif pilihan == '2':
            tampilkan_buku(data)
        elif pilihan == '3':
            id_buku = input("Masukkan ID Buku yang ingin diubah: ").upper()
            for buku in data:
                if buku['id'] == id_buku:
                    buku['judul'] = input("Masukkan judul baru: ").upper()
                    buku['penulis'] = input("Masukkan penulis baru: ").upper()
                    if not buku['judul'] or not buku['penulis']:
                        print("❌ Judul dan penulis tidak boleh kosong.")
                        continue
                    save_buku(data)
                    print("✅ Data buku berhasil diubah.")
                    break
            else:
                print("❌ Buku tidak ditemukan.")
        elif pilihan == '4':
            id_buku = input("Masukkan ID Buku yang ingin dihapus: ").upper()
            if not any(buku['id'] == id_buku for buku in data):
                print("❌ Buku tidak ditemukan.")
                continue
            data = [buku for buku in data if buku['id'] != id_buku]
            save_buku(data)
            print("✅ Buku berhasil dihapus.")
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")
