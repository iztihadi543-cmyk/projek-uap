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

def validasi_tanggal_lahir(tanggal_lahir):
    """
    Memvalidasi format tanggal lahir DD-MM-YYYY secara manual 
    dan nilai hari (1-31) serta bulan (1-12).
    """
    
    # 1. Cek Panjang dan Karakter Pemisah
    if len(tanggal_lahir) != 10 or tanggal_lahir[2] != '-' or tanggal_lahir[5] != '-':
        return False, "Format tanggal lahir harus DD-MM-YYYY (contoh: 01-12-2000)."

    try:
        # 2. Pisahkan dan Cek Apakah Semuanya Angka
        bagian = tanggal_lahir.split('-')
        if len(bagian) != 3:
            return False, "Format tanggal lahir harus DD-MM-YYYY."

        hari = int(bagian[0])
        bulan = int(bagian[1])
        tahun = int(bagian[2])

        # 3. Validasi Nilai Hari (DD) dan Bulan (MM)
        
        # Cek Hari (1-31)
        if not (1 <= hari <= 31):
            return False, f"Tanggal (DD) harus antara 01 sampai 31. Ditemukan: {hari:02d}"

        # Cek Bulan (1-12)
        if not (1 <= bulan <= 12):
            return False, f"Bulan (MM) harus antara 01 sampai 12. Ditemukan: {bulan:02d}"
        
        # Tambahan: Cek Tahun (YYYY) harus 4 digit
        if not (1000 <= tahun <= 9999):
             return False, "Tahun (YYYY) harus 4 digit."

        return True, ""
        
    except ValueError:
        # Jika salah satu bagian (hari, bulan, atau tahun) bukan angka
        return False, "Hari, bulan, atau tahun harus berupa angka."

# --- FUNGSI TAMBAH DATA ---
def tambah_data():
    print("\n==== Tambah Data Pasien ====")
    try:
        nama = input("Masukkan Nama Pasien: ")
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong!")

        while True:
            # Menggunakan format DD-MM-YYYY untuk konsistensi
            tanggal_lahir = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
            if tanggal_lahir.strip() == "":
                raise ValueError("Tanggal lahir tidak boleh kosong!")
                
            valid, pesan = validasi_tanggal_lahir(tanggal_lahir)
            if valid:
                break
            else:
                print(f"⚠️ Error Tanggal Lahir: {pesan} Mohon coba lagi.")


        diagnosis = input("Masukkan Diagnosa: ")
        if diagnosis.strip() == "":
            raise ValueError("Diagnosa tidak boleh kosong!")

        pasien = {
            "nama": nama,
            "tanggal_lahir": tanggal_lahir,
            "diagnosis": diagnosis
        }
        data_pasien.append(pasien)
        save_data()
        print("✅ Data pasien berhasil ditambahkan.")

    except ValueError as e:
        print(f"⚠️ Error Input: {e}")
    except Exception as e:
        print(f"⚠️ Terjadi error yang tidak diketahui: {e}")

# --- FUNGSI TAMPILKAN DATA ---
def tampilkan_data():
    print("\n==== Data Pasien ====")
    try:
        if not data_pasien:
            print("Belum ada data pasien.")
            return
        
        print("-" * 50)
        for i, pasien in enumerate(data_pasien, 1):
            print(f"{i}. Nama: {pasien['nama']}")
            print(f"   Tgl Lahir: {pasien['tanggal_lahir']}")
            print(f"   Diagnosa: {pasien['diagnosis']}")
            print("-" * 50)

    except Exception as e:
        print(f"⚠️ Terjadi error saat menampilkan data: {e}")

# --- FUNGSI EDIT DATA ---
def edit():
    print("\n==== Edit Data Pasien ====")
    try:
        tampilkan_data()
        if not data_pasien:
            return

        nama_cari = input("Masukkan Nama Pasien yang Ingin Diedit: ").strip().lower()

        pasien_ditemukan = None
        for pasien in data_pasien:
            if pasien["nama"].lower() == nama_cari:
                pasien_ditemukan = pasien
                break
        
        if pasien_ditemukan:
            print(f"\n--- Data yang ditemukan: {pasien_ditemukan['nama']} ---")
            
            # --- Edit Nama ---
            nama_baru = input(f"Masukkan Nama Pasien Baru (Kosongkan jika tetap: {pasien_ditemukan['nama']}): ")
            if nama_baru.strip() != "":
                 pasien_ditemukan["nama"] = nama_baru


            # --- Edit Tanggal Lahir dengan Validasi ---
            while True:
                tgl_lahir_baru = input(f"Masukkan Tanggal Lahir Baru (Kosongkan jika tetap: {pasien_ditemukan['tanggal_lahir']}) (DD-MM-YYYY): ")
                
                if tgl_lahir_baru.strip() == "":
                    # Jika input kosong, pertahankan nilai lama dan keluar dari loop
                    tgl_lahir_baru = pasien_ditemukan["tanggal_lahir"]
                    break
                
                valid, pesan = validasi_tanggal_lahir(tgl_lahir_baru)
                if valid:
                    break
                else:
                    print(f"⚠️ Error Tanggal Lahir: {pesan} Mohon coba lagi.")
            
            pasien_ditemukan["tanggal_lahir"] = tgl_lahir_baru

            # --- Edit Diagnosa ---
            diagnosa_baru = input(f"Masukkan Diagnosa Baru (Kosongkan jika tetap: {pasien_ditemukan['diagnosis']}): ")
            if diagnosa_baru.strip() != "":
                pasien_ditemukan["diagnosis"] = diagnosa_baru

            save_data()
            print("✅ Data pasien berhasil diupdate.")
            return
        
        print("❌ Data pasien tidak ditemukan.")

    except Exception as e:
        print(f"⚠️ Terjadi kesalahan saat mengedit data: {e}")

# --- FUNGSI HAPUS DATA ---
def hapus():
    print("\n==== Hapus Data Pasien ====")
    try:
        tampilkan_data()
        if not data_pasien:
            return

        nama_cari = input("Masukkan Nama Pasien yang Ingin Dihapus: ").strip().lower()
        
        dihapus = False
        # Iterasi terbalik untuk menghapus elemen dari list saat iterasi
        for i in range(len(data_pasien) - 1, -1, -1):
            if data_pasien[i]["nama"].lower() == nama_cari:
                del data_pasien[i] # Hapus item dari list global
                dihapus = True
                break 

        if dihapus:
            save_data()
            print("✅ Data pasien berhasil dihapus.")
        else:
             print("❌ Data pasien tidak ditemukan.")


    except Exception as e:
        print(f"⚠️ Terjadi kesalahan saat menghapus data: {e}")


def cari_data():
    print("\n==== Cari Data Pasien ====")
    if not data_pasien:
        print("Belum ada data pasien untuk dicari.")
        return

    keyword = input("Masukkan Nama/Diagnosa pasien yang dicari: ").strip().lower()
    
    # Pencarian tanpa keyword akan menampilkan semua
    if not keyword:
        print("Masukkan keyword yang valid.")
        return

    hasil_cari = []
    # Menggunakan for dan if untuk filter data
    for pasien in data_pasien:
        nama_lower = pasien["nama"].lower()
        diagnosis_lower = pasien["diagnosis"].lower()
        
        # Percabangan yang menentukan filter (wajib ada)
        if keyword in nama_lower or keyword in diagnosis_lower:
            hasil_cari.append(pasien)

    if hasil_cari:
        print(f"\n✅ Ditemukan {len(hasil_cari)} data pasien yang cocok:")
        # Menggunakan fungsi tampilkan_data (atau fungsi tampilan yang baru)
        tampilkan_hasil(hasil_cari) 
    else:
        print("❌ Data pasien tidak ditemukan dengan keyword tersebut.")

# Catatan: Perlu fungsi bantu baru untuk menampilkan hasil pencarian
def tampilkan_hasil(list_data):
    # Logika untuk menampilkan data dari list yang difilter
    for i, pasien in enumerate(list_data, 1):
        print(f"{i}. Nama: {pasien['nama']}")
        print(f"   Tgl Lahir: {pasien['tanggal_lahir']}")
        print(f"   Diagnosa: {pasien['diagnosis']}")
        print("-" * 50)


# --- FUNGSI MENU UTAMA ---
def menu():
    while True:
        print("\n===================================")
        print("🏥 Menu Manajemen Data Pasien 🏥")
        print("===================================")
        print("1. Tambah Data Pasien")
        print("2. Tampilkan Data Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Cari Atau Filter Data Pasien")
        print("6. Keluar")
        print("===================================")

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
                cari_data()
            elif pilihan == '6':
                print("👋 Keluar dari program. Sampai jumpa!")
                break
            else:
                print("⚠️ Pilihan menu tidak valid! Silakan masukkan angka antara 1-5.")
        
        except Exception as e:
            print(f"⚠️ Terjadi error yang tidak diketahui: {e}")


# --- MENJALANKAN PROGRAM ---
if __name__ == "__main__":
    muat_data()
    menu()
    #TES MAU COMMIT
