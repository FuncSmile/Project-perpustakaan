# Model untuk member
import os
import csv

DATA_DIR = "src/data"
MEMBER_FILE = os.path.join(DATA_DIR, "member.csv")

def load_member():
    if not os.path.exists(MEMBER_FILE):
        return []
    with open(MEMBER_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_member(data):
    fieldnames = ["id_member", "nama", "email", "no_hp"]
    with open(MEMBER_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def auto_id(data, prefix, key):
    nomor = 1
    existing_ids = {d[key] for d in data}
    while True:
        id_baru = f"{prefix}{str(nomor).zfill(3)}"
        if id_baru not in existing_ids:
            return id_baru
        nomor += 1
