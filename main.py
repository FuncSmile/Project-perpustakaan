from src.controllers.gudang_controller import menu_gudang
from src.controllers.kasir_controller import menu_kasir
import os

DATA_DIR = "src/data"

# Pastikan folder data ada
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def menu_utama():
    ensure_data_dir()
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
