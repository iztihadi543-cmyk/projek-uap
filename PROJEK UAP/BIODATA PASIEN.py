data_pasien = []

def simpan_data():
    try:
        with open("data_pasien.txt", "w") as file:
            for pasien in data_pasien:
                file.write(f"{pasien['nama']},{pasien['tanggal_lahir']},{pasien['alamat']},{pasien['diagnosa']}\n")
        print("Data pasien berhasil disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")


def validasi_tanggal_lahir(tanggal_lahir):
    if len(tanggal_lahir) != 10 or tanggal_lahir[2] != '-' or tanggal_lahir[5] != '-':
        return False, "⚠️ Format harus DD-MM-YYYY"

    try:
        hari, bulan, tahun = map(int, tanggal_lahir.split('-'))
        if not (1 <= hari <= 31 and 1 <= bulan <= 12 and tahun <= 2025):
            return False, "⚠️ Tanggal tidak valid"
        return True, ""
    except ValueError:
        return False, "⚠️ Tanggal harus berupa angka!"


def tambah_data():
    print("\n=== Tambah Data Pasien ===")
    try:
        nama = input("Masukkan Nama Pasien: ")
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong.")

        while True:
            tanggal_lahir = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
            valid, pesan = validasi_tanggal_lahir(tanggal_lahir)
            if valid:
                break
            print(pesan)

        alamat = input("Masukkan Alamat Pasien: ")
        if alamat.strip() == "":
            raise ValueError("Alamat tidak boleh kosong.")

        diagnosa = input("Masukkan Diagnosa Pasien: ")
        if diagnosa.strip() == "":
            raise ValueError("Diagnosa tidak boleh kosong.")

        pasien = {
            "nama": nama,
            "tanggal_lahir": tanggal_lahir,
            "alamat": alamat,
            "diagnosa": diagnosa
        }

        data_pasien.append(pasien)
        simpan_data()
        print("Data pasien berhasil ditambahkan.")

    except ValueError as ve:
        print("⚠️ Error input:", ve)
    except Exception as e:
        print("⚠️ Terjadi kesalahan:", e)


def tampilkan_data():
    print("\n==== Data Pasien ====")
    
    if not data_pasien:
        print("Tidak ada data pasien.")
        return

    print("-" * 50)
    for i, pasien in enumerate(data_pasien, 1):
        print(f"{i}. Nama: {pasien['nama']}")
        print(f"   Tanggal Lahir: {pasien['tanggal_lahir']}")
        print(f"   Diagnosa: {pasien['diagnosa']}")
        print("-" * 50)


def edit():
    print("\n=== Edit Data Pasien ===")
    nama_cari = input("Masukkan Nama Pasien yang akan diedit: ")
    
    for pasien in data_pasien:
        if pasien['nama'].lower() == nama_cari.lower():
            print("Data ditemukan. Silakan masukkan data baru.")
            pasien['nama'] = input("Nama baru: ")
            pasien['tanggal_lahir'] = input("Tanggal lahir baru (DD-MM-YYYY): ")
            pasien['alamat'] = input("Alamat baru: ")
            pasien['diagnosa'] = input("Diagnosa baru: ")
            simpan_data()
            print("Data berhasil diupdate.")
            return
    
    print("⚠️ Data tidak ditemukan.")


def hapus():
    print("\n=== Hapus Data Pasien ===")
    nama_cari = input("Masukkan Nama Pasien: ")

    for i, pasien in enumerate(data_pasien):
        if pasien['nama'].lower() == nama_cari.lower():
            del data_pasien[i]
            simpan_data()
            print("Data pasien berhasil dihapus.")
            return

    print("⚠️ Data pasien tidak ditemukan.")


def menu():
    while True:
        print("\n=== Menu Manajemen Data Pasien ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            edit()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("⚠️ Pilihan tidak valid.")


menu()
