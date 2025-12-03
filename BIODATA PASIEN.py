data_pasien = []

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

        nama_cari = input("Masukkan Nama Pasien yang Ingin Diedit: ")

        pasien_ditemukan = None
        for pasien in data_pasien:
            if pasien["nama"] == nama_cari:
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

        nama_cari = input("Masukkan Nama Pasien yang Ingin Dihapus: ")
        
        dihapus = False
        # Iterasi terbalik untuk menghapus elemen dari list saat iterasi
        for i in range(len(data_pasien) - 1, -1, -1):
            if data_pasien[i]["nama"] == nama_cari:
                del data_pasien[i] # Hapus item dari list global
                dihapus = True
                break 

        if dihapus:
            print("✅ Data pasien berhasil dihapus.")
        else:
             print("❌ Data pasien tidak ditemukan.")

    except Exception as e:
        print(f"⚠️ Terjadi kesalahan saat menghapus data: {e}")

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
        print("5. Keluar")
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
                print("👋 Keluar dari program. Sampai jumpa!")
                break
            else:
                print("⚠️ Pilihan menu tidak valid! Silakan masukkan angka antara 1-5.")
        
        except Exception as e:
            print(f"⚠️ Terjadi error yang tidak diketahui: {e}")


# --- MENJALANKAN PROGRAM ---
if __name__ == "__main__":
    menu()