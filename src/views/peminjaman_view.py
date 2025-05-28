# View untuk peminjaman
from tabulate import tabulate
from src.models.peminjaman_model import load_peminjaman

def tampilkan_peminjaman():
    data = load_peminjaman()
    if not data:
        print("Tidak ada data peminjaman.")
    else:
        print(tabulate(data, headers="keys", tablefmt="grid"))
