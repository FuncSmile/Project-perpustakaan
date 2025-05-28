from crud import menu_gudang
from utils import menu_kasir

def menu_utama():
    while True:
        print("\n=== Sistem Perpustakaan ===")
        print("1. Gudang Perpustakaan ")
        print("2. Kasir Perpustakaan")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            menu_gudang()
        elif pilihan == '2':
            menu_kasir()
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu_utama()
