data_pasien = []

def simpan_data():
    try:
        with open("data_pasien.txt", "w", encoding="utf-8") as file:
            for pasien in data_pasien:
                file.write(f"{pasien['nama']},{pasien['tanggal_lahir']},{pasien['alamat']},{pasien['diagnosa']}\n")
        print("Data pasien berhasil disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")

def validasi_tanggal_lahir(tanggal_lahir):
    if len(tanggal_lahir) != 10 or tanggal_lahir[2] != '-' or tanggal_lahir[5] != '-':
        return False, "Format tanggal lahir harus DD-MM-YYYY"
    
    try:
        hari, bulan, tahun = map(int, tanggal_lahir.split('-'))
        if not (1 <= hari <= 31 and 1 <= bulan <= 12 and tahun <= 2025 and tahun >= 1900):
            return False, "Tanggal lahir tidak valid"

        bulan30 = {4, 6, 9, 11}
        if bulan in bulan30 and hari > 30:
            return False, "Tanggal lahir tidak valid untuk bulan tersebut"

        if bulan == 2:
            if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
                if hari > 29:
                    return False, "Tanggal lahir tidak valid untuk Februari (kabisat)"
            else:
                if hari > 28:
                    return False, "Tanggal lahir tidak valid untuk Februari"

        return True, ""
    except ValueError:
        return False, "Tanggal lahir harus berupa angka dalam format DD-MM-YYYY"

def tambah_data():
    print("=== Tambah Data Pasien ===")
    try:
        nama = input("Masukkan Nama Pasien: ")
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong.")

        while True:
            tanggal_lahir = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
            valid, pesan = validasi_tanggal_lahir(tanggal_lahir)
            if valid:
                break
            else:
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
        print("Error input:", ve)
    except Exception as e:
        print("Terjadi kesalahan:", e)

def tampilkan_data():
    print("\n==== Data Pasien ====")
    try:
        list_pasien = data_pasien

        if not list_pasien:
            print("Tidak ada data pasien untuk ditampilkan.")
            return
        
        print("-" * 50)
        for i, pasien in enumerate(list_pasien, 1):
            print(f"{i}. Nama: {pasien['nama']}")
            print(f"   Tgl Lahir: {pasien['tanggal_lahir']}")
            print(f"   Alamat: {pasien['alamat']}")
            print(f"   Diagnosa: {pasien['diagnosa']}")
            print("-" * 50)

    except Exception as e:
        print(f"⚠️ Terjadi error saat menampilkan data: {e}")

def edit():
    print("=== Edit Data Pasien ===")
    try:
        nama_cari = input("Masukkan Nama Pasien yang akan diedit: ")
        for pasien in data_pasien:
            if pasien['nama'].lower() == nama_cari.lower():
                print("Data ditemukan. Silakan masukkan data baru.")
                pasien['nama'] = input("Masukkan Nama Pasien: ")
                pasien['tanggal_lahir'] = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
                pasien['alamat'] = input("Masukkan Alamat Pasien: ")
                pasien['diagnosa'] = input("Masukkan Diagnosa Pasien: ")
                simpan_data()
                print("Data pasien berhasil diupdate.")
                return
        print("Data pasien tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengedit data: {e}")

def hapus():
    print("=== Hapus Data Pasien ===")
    try:
        nama_cari = input("Masukkan Nama Pasien yang akan dihapus: ")
        for i, pasien in enumerate(data_pasien):
            if pasien['nama'].lower() == nama_cari.lower():
                del data_pasien[i]
                simpan_data()
                print("Data pasien berhasil dihapus.")
                return
        print("Data pasien tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus data: {e}")

def menu():
    while True:
        print("\n=== Menu Manajemen Data Pasien ===")
        print("1. Tambah Data Pasien")
        print("2. Tampilkan Data Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
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
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
