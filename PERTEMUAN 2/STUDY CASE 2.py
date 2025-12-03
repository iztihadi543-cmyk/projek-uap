# #1. Buatkan program sederhana yang menampilkan biodata
# menggunakan variabel, program harus meminta input dari
# pengguna seperti: Nama , Kelas, NPM, Prodi lalu tampilkan kembali
# biodata tersebut.
nama = input("Masukan nama:")
kelas = input("Masukan kelas anda:")
npm = int(input("Masukan npm anda:"))
prodi = input("Masukan prodi anda:")

print("=====Data Mahasiswa=====")
print("Nama :",(nama))
print("Kelas :",(kelas))
print("NPM :",(npm))
print("Prodi :",(prodi))

print(f'Nama saya adalah {nama}, saya dari kelas {kelas}, NPM saya {npm}, dan prodi saya {prodi}')