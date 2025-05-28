# View untuk buku
from tabulate import tabulate
from src.models.buku_model import load_buku

def tampilkan_buku(data_buku=None):
    if data_buku is None:
        data_buku = load_buku()
    if not data_buku:
        print("Tidak ada data buku.")
    else:
        print(tabulate(data_buku, headers="keys", tablefmt="grid"))
