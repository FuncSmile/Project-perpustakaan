# Model untuk buku
import os
import csv

DATA_DIR = "src/data"
BUKU_FILE = os.path.join(DATA_DIR, "buku.csv")



def load_buku():
    if not os.path.exists(BUKU_FILE):
        return []
    with open(BUKU_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_buku(data):
    fieldnames = ["id", "judul", "penulis"]
    with open(BUKU_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
