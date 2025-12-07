# ==========================================
# PROJEK AKHIR DASAR PEMROGRAMAN (KELOMPOK UJANG-4)
#Data Pasien Rumah Sakit
# Anggota:
# 1. Iztihadi - 2517052006
# 2. Ramadian Pasesa - 2517052034
# 3. Arifah Kamilah Aulia - 2517052041
# ==========================================




data_pasien = []


# ======== SIMPAN DATA ========
def simpan_data():
    try:
        with open("data_pasien.txt", "w") as file:  # overwrite agar format rapi
            for pasien in data_pasien:
                file.write(f"{pasien['nama']},{pasien['tanggal_lahir']},{pasien['alamat']},{pasien['diagnosa']}\n")
        print("💾 Data pasien berhasil disimpan.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menyimpan data: {e}")


# ======== MUAT DATA ========
def muat_data():
    try:
        with open("data_pasien.txt", "r") as file:
            for baris in file:
                data = baris.strip().split(",")
                if len(data) == 4:
                    data_pasien.append({
                        "nama": data[0],
                        "tanggal_lahir": data[1],
                        "alamat": data[2],
                        "diagnosa": data[3]
                    })
        print("📂 Data berhasil dimuat dari file.")
    except FileNotFoundError:
        print("📄 File belum ditemukan, akan dibuat setelah menyimpan.")


# ====== VALIDASI ======
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


# ======== TAMBAH DATA ========
def tambah_data():
    print("\n=== ➕ Tambah Data Pasien ===")
    try:
        nama = input("Masukkan Nama Pasien: ")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong.")

        while True:
            tanggal_lahir = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
            valid, pesan = validasi_tanggal_lahir(tanggal_lahir)
            if valid:
                break
            print(pesan)

        alamat = input("Masukkan Alamat Pasien: ")
        if not alamat.strip():
            raise ValueError("Alamat tidak boleh kosong.")

        diagnosa = input("Masukkan Diagnosa Pasien: ")
        if not diagnosa.strip():
            raise ValueError("Diagnosa tidak boleh kosong.")

        data_pasien.append({
            "nama": nama,
            "tanggal_lahir": tanggal_lahir,
            "alamat": alamat,
            "diagnosa": diagnosa
        })

        simpan_data()
        print("✅ Data pasien berhasil ditambahkan.")

    except ValueError as ve:
        print("⚠️ Error input:", ve)
    except Exception as e:
        print("⚠️ Terjadi kesalahan:", e)


# ======== TAMPILKAN DATA ========
def tampilkan_data():
    print("\n=== 📋 Daftar Data Pasien ===")

    if not data_pasien:
        print("⚠️ Belum ada data pasien.")
        return

    print("-" * 50)
    for i, pasien in enumerate(data_pasien, 1):
        print(f"{i}. {pasien['nama']}")
        print(f"   📅 Tanggal Lahir: {pasien['tanggal_lahir']}")
        print(f"   📍 Alamat: {pasien['alamat']}")
        print(f"   🏥 Diagnosa: {pasien['diagnosa']}")
        print("-" * 50)


# ======== EDIT DATA ========
def edit():
    print("\n=== 📝 Edit Data Pasien ===")
    nama_cari = input("Masukkan Nama Pasien yang akan diedit: ")

    for pasien in data_pasien:
        if pasien['nama'].lower() == nama_cari.lower():
            print("✔️ Data ditemukan!")

            pasien['nama'] = input("Nama baru:(kosongkan jika tidak berubah) ") or pasien['nama']
            pasien['tanggal_lahir'] = input("Tanggal lahir baru (DD-MM-YYYY):(Kosongkan jika tidak berubah) ") or pasien['tanggal_lahir']
            pasien['alamat'] = input("Alamat baru:(Kosongkan jika tidak berubah) ") or pasien['alamat']
            pasien['diagnosa'] = input("Diagnosa baru:(Kosongkan jika tidak berubah) ") or pasien['diagnosa']

            simpan_data()
            print("✔️ Data berhasil diperbarui.")
            return

    print("❌ Data tidak ditemukan.")


# ======== HAPUS DATA ========
def hapus():
    print("\n=== 🗑️ Hapus Data Pasien ===")
    nama_cari = input("Masukkan Nama Pasien: ")

    for i, pasien in enumerate(data_pasien):
        if pasien['nama'].lower() == nama_cari.lower():
            del data_pasien[i]
            simpan_data()
            print("🗑️ Data berhasil dihapus.")
            return

    print("❌ Data tidak ditemukan.")


# ======== CARI DATA ========
def cari():
    print("\n🔍 Cari Data Pasien")
    keyword = input("Masukkan nama atau diagnosa: ").lower()

    hasil = [p for p in data_pasien if keyword in p['nama'].lower() or keyword in p['diagnosa'].lower()]

    if hasil:
        print(f"\n✔️ Ditemukan {len(hasil)} data:")
        
        print("-" * 50)
        for i, pasien in enumerate(hasil, 1):
            print(f"{i}. {pasien['nama']}")
            print(f" Tanggal Lahir: {pasien['tanggal_lahir']}")
            print(f" Alamat: {pasien['alamat']}")
            print(f" Diagnosa: {pasien['diagnosa']}")
            print("-" * 50)
    else:
        print("❌ Tidak ada data yang cocok.")

# ======== MENU ========
def menu():
    while True:
        print("\n==========================================")
        print("Selamat Datang Disistem Manajemen RS Ujang")
        print("==========================================")
        print("=== 🏥 Menu Manajemen Data Pasien ===")
        print("1. Tambah Data Pasien")
        print("2. Tampilkan Data Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Cari Data Pasien")
        print("6. Keluar Sistem")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1': tambah_data()
        elif pilihan == '2': tampilkan_data()
        elif pilihan == '3': edit()
        elif pilihan == '4': hapus()
        elif pilihan == '5': cari()
        elif pilihan == '6':
            print("\n👋 Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("⚠️ Pilihan tidak valid.")



# ======== JALANKAN ========
muat_data()
menu()