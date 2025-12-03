#DATA PENYIMPANAN BIODATA PASIEN
data_pasien = []  

# ==========================================
# SIMPAN DATA KE FILE
# ==========================================
def save_data():
    try:
        with open("data_pasien.txt", "w", encoding="utf-8") as file:
            for pasien in data_pasien:
                baris = f"{pasien['nama']},{pasien['tanggal_lahir']},{pasien['diagnosis']}\n"
                file.write(baris)
        print("Data berhasil disimpan ke data_pasien.txt\n")
    except Exception as e:
        print(f"Error saat menyimpan data: {e}")

# ==========================================
# MUAT DATA DARI FILE
# ==========================================
def muat_data():
    try:
        with open("data_pasien.txt", "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split(",")
                if len(data) == 3:
                    pasien = {
                        "nama": data[0],
                        "tanggal_lahir": data[1],
                        "diagnosis": data[2]
                    }
                    data_pasien.append(pasien)
        print("Data berhasil dimuat dari file!\n")
    except FileNotFoundError:
        print("File belum ada, akan dibuat saat menyimpan...\n")

# ==========================================
# TAMBAH DATA
# ==========================================
def tambah_data():
    nama = input("Nama pasien: ")
    tgl = input("Tanggal lahir: ")
    diag = input("Diagnosis: ")

    pasien = {
        "nama": nama,
        "tanggal_lahir": tgl,
        "diagnosis": diag
    }
    data_pasien.append(pasien)

    save_data()   # <=== auto save
    print("Data pasien berhasil ditambahkan!\n")

# ==========================================
# TAMPILKAN DATA
# ==========================================
def tampilkan_data():
    if not data_pasien:
        print("Belum ada data pasien.\n")
        return

    print("\n=== DATA PASIEN ===")
    for i, pasien in enumerate(data_pasien, start=1):
        print(f"{i}. Nama: {pasien['nama']}")
        print(f"   Tanggal Lahir: {pasien['tanggal_lahir']}")
        print(f"   Diagnosis: {pasien['diagnosis']}")
        print("-------------------------")
    print("====================\n")

# ==========================================
# MENU UTAMA
# ==========================================
def menu():
    muat_data()  # otomatis load file ketika program mulai

    while True:
        print("========== MENU ==========")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Simpan Data")
        print("4. Keluar")
        print("==========================")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            save_data()
        elif pilih == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")

# Jalankan program
menu()
