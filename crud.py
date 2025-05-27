from utils import load_data, save_data, tampilkan_buku, auto_id

def menu_gudang():
    while True:
        data = load_data()  # Load data setiap awal loop

        print("\n=== Menu Gudang Buku ===")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Ubah Buku")
        print("4. Hapus Buku")
        print("5. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            id_baru = auto_id(data, prefix="B", key="id")
            judul = input("Masukkan Judul Buku: ")
            penulis = input("Masukkan Penulis Buku: ")
            data.append({"id": id_baru, "judul": judul, "penulis": penulis})
            save_data(data)
            print("✅ Buku berhasil ditambahkan.")
        elif pilihan == '2':
            tampilkan_buku(data)
        elif pilihan == '3':
            id_buku = input("Masukkan ID Buku yang ingin diubah: ")
            for buku in data:
                if buku['id'] == id_buku:
                    buku['judul'] = input("Masukkan judul baru: ")
                    buku['penulis'] = input("Masukkan penulis baru: ")
                    save_data(data)
                    print("✅ Data buku berhasil diubah.")
                    break
            else:
                print("❌ Buku tidak ditemukan.")
        elif pilihan == '4':
            id_buku = input("Masukkan ID Buku yang ingin dihapus: ")
            data = [buku for buku in data if buku['id'] != id_buku]
            save_data(data)
            print("✅ Buku berhasil dihapus.")
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")
        