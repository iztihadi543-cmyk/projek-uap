data_pasien = []

def tambah_data():
    print("==== Tambah Data Pasien ====")
    try:
        nama = input("Masukkan Nama Pasien: ")
        if nama.strip() == "":
            raise ValueError("Input tidak boleh kosong!")
        tanggal_lahir = input("Masukkan Tanggal Lahir (DD MM YYYY): ")
        if tanggal_lahir.strip() == "":
            raise ValueError("Input tidak boleh kosong!")
        diagnosis = input("Masukkan Diagnosa: ")
        if diagnosis.strip() == "":
            raise ValueError("Input tidak boleh kosong!")

        pasien = {
            "nama": nama,
            "tanggal_lahir": tanggal_lahir,
            "diagnosis": diagnosis
        }
        data_pasien.append(pasien)
        print("Data pasien berhasil ditambahkan.")

    except ValueError as e:
        print(f"⚠️ Error: {e}")
    except Exception:
        print("⚠️ Terjadi error yang tidak diketahui.")


def tampilkan_data():
    print("==== Data Pasien ====")
    try:
        if not data_pasien:
            print("Belum ada data pasien.")
            return
        
        for i in data_pasien:
            print(f"Nama: {i['nama']}, Tanggal Lahir: {i['tanggal_lahir']}, Diagnosa: {i['diagnosis']}")

    except Exception:
        print("⚠️ Terjadi error saat menampilkan data.")


def edit():
    try:
        tampilkan_data()
        nama_cari = input("Masukkan Nama Pasien yang Ingin Diedit: ")

        for pasien in data_pasien:
            if pasien["nama"] == nama_cari:
                print("Data ditemukan. Masukkan data baru:")

                pasien["nama"] = input("Masukkan Nama Pasien: ")
                pasien["tanggal_lahir"] = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
                pasien["diagnosis"] = input("Masukkan Diagnosa: ")

                print("Data pasien berhasil diupdate.")
                return
        
        print("❌ Data pasien tidak ditemukan.")

    except Exception:
        print("⚠️ Terjadi kesalahan saat mengedit data.")


def hapus():
    try:
        tampilkan_data()
        nama_cari = input("Masukkan Nama Pasien yang Ingin Dihapus: ")

        for pasien in data_pasien:
            if pasien["nama"] == nama_cari:
                data_pasien.remove(pasien)
                print("Data pasien berhasil dihapus.")
                return

        print("❌ Data pasien tidak ditemukan.")

    except Exception:
        print("⚠️ Terjadi kesalahan saat menghapus data.")


def menu():
    while True:
        print("\n==== Menu Manajemen Data Pasien ====")
        print("1. Tambah Data Pasien")
        print("2. Tampilkan Data Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        try:
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
                raise ValueError("Pilihan menu tidak valid!")
        
        except ValueError as e:
            print(f"⚠️ Error: {e}")
        except Exception:
            print("⚠️ Terjadi error yang tidak diketahui.")


menu()
