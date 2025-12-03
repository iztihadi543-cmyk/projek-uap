# Buat program yang mencetak bilangan genap dari 1 hingga 30
# # menggunakan for loop. (Tips: gunakan if i % 2 == 0)
for i in range(1, 31):
    if i % 2 == 0:
        print(i)
# Buat program tebak angka sederhana. Program memilih angka acak
# antara 1–10, lalu pengguna harus menebaknya. Program terus
# meminta input hingga jawaban benar.

angka = 2
tebak = 0
while tebak != angka:
    tebak = int(input("Tebak angka antara 1-10: "))
    if tebak == angka:
        print("Tebakan Anda benar!")
    else:
        print("Tebakan Anda salah, coba lagi.")

# Buat program yang menampilkan setiap huruf dalam kata 'Universitas'.
# Jika huruf 's' ditemukan, hentikan perulangan dengan break.

kata = "Universitas"
for i in kata :
    if i == 's':
        break
    print(i)

# Buat program yang menghitung jumlah huruf vokal dalam sebuah
# kata menggunakan for loop. ""

kata = input("Masukkan sebuah kata: ")
vokal = "aiueoAIUEO"
jumlah_vokal = 0
for i in kata :
    if i in vokal:
        jumlah_vokal += 1
print("Jumlah huruf vokal dalam kata tersebut adalah:", jumlah_vokal)