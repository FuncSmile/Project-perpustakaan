# View untuk member
from tabulate import tabulate
from src.models.member_model import load_member

def tampilkan_member():
    data_member = load_member()
    if not data_member:
        print("Tidak ada member terdaftar. Silakan daftar member terlebih dahulu.")
    else:
        print(tabulate(data_member, headers="keys", tablefmt="grid"))
