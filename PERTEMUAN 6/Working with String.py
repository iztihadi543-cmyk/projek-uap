# Materi Praktikum
# Indexing
# Karakter dalam sebuah string dapat diakses menggunakan indeks, di
# mana indeks dimulai dari 0 untuk karakter pertama. Dengan cara ini, kita
# bisa mengambil satu karakter tertentu dari string sesuai posisinya.

# Contoh:
word = 'asah linggis'
print(word[1])

# Selain itu, Python juga memungkinkan untuk mengambil potongan string
# (substring) menggunakan format [start:stop:step], mirip seperti fungsi
# range(). String juga bisa menggunakan metode slicing untuk membalik
# string, formatnya adalah [:: -1]. Parameter start menentukan posisi awal,
# stop menentukan posisi akhir (tidak termasuk), dan step menentukan
# jarak antar karakter (opsional).

# Contoh:
# name = 'Justice Gang'
# print(name[1:5])
# print(name[1:8:2])
# print(name[:: -1])

# String Methods
# Casing Methods
# Metode ini digunakan untuk mengatur case (huruf besar atau kecil) dalam
# string. Beberapa metode umum yang digunakan adalah:
# ● lower() → Mengubah semua karakter menjadi huruf kecil.
# ● upper() → Mengubah semua karakter menjadi huruf besar (kapital).
# ● capitalize() → Mengubah huruf pertama string menjadi kapital.
# ● title() → Mengubah huruf pertama dari setiap kata menjadi kapital.
# ● swapcase() → Menukar case (huruf besar menjadi kecil, dan huruf
# kecil menjadi besar).

# Contoh:
# word = 'Stay Young, Black, and Unique'
# print(word.lower()) stay young, black, and unique
# print(word.upper()) STAY YOUNG, BLACK, AND UNIQUE
# print(word.capitalize()) Stay young, black, and unique
# print(word.title()) Stay Young, Black, And Unique
# print(word.swapcase()) sTAY yOUNG, bLACK, AND uNIQUE

# Searching & Replacing Methods
# Kelompok metode ini digunakan untuk mencari, menghitung, atau
# mengganti bagian tertentu dari string. Berikut metode yang umum
# digunakan:
# ● find(), untuk mengembalikan posisi indeks pertama dari substring
# tertentu, atau -1 jika tidak ditemukan.
# ● index(), sama seperti find(), tetapi akan menghasilkan error jika
# substring tidak ditemukan.
# ● len(), untuk menghitung panjang dari string.
# ● count(), untuk menghitung berapa kali substring muncul.
# ● replace(), untuk mengganti substring lama dengan substring baru.
# ● startswith(), untuk mengecek apakah string diawali dengan
# substring tertentu (menghasilkan boolean).
# ● endswith(), untuk mengecek apakah string diakhiri dengan substring
# tertentu (menghasilkan boolean).

# Contoh:
# fileName = 'main.cpp'
# print(fileName.find('y'))
# print(fileName.index('.'))
# print(fileName.count('p'))
# print(fileName.replace('cpp', 'py'))
# print(fileName.startswith('main'))
# print(fileName.endswith('py'))

# 4

# Format Methods
# Metode format digunakan untuk membersihkan, membagi, atau
# menggabungkan string. Beberapa metode yang sering digunakan antara
# lain:
# ● strip(), untuk menghapus spasi atau karakter tertentu di awal dan
# akhir string.
# ● split(), untuk memecah string menjadi elemen-elemen list
# berdasarkan pemisah tertentu.

# Contoh:
# data = " Python Programming "
# print(data.strip())
# kalimat = "Belajar Python Dasar"
# print(kalimat.split())

# String Validation Methods
# Metode validasi digunakan untuk memeriksa isi string — apakah hanya
# terdiri dari huruf, angka, kombinasi huruf-angka, atau spasi.
# Berikut metode validasi yang umum digunakan:
# ● isalpha() → Mengembalikan True jika hanya berisi huruf alfabet
# ● isdigit() → Mengembalikan True jika hanya berisi angka (0–9).
# ● isalnum() → Mengembalikan True jika hanya berisi huruf dan angka.
# ● isspace() → Mengembalikan True jika hanya berisi karakter spasi.

# Contoh:
# print("Python".isalpha()) # True, karena hanya huruf
# print("1234".isdigit()) # True, karena hanya angka
# print("abc123".isalnum()) # True, karena huruf dan angka
# print(" ".isspace()) # True, karena hanya spasi
# print("Data 1".isalnum())

# 5

# Pemformatan String
# Pemformatan string digunakan untuk menyusun teks yang mengandung
# variabel atau data dinamis. Ada tiga cara utama untuk melakukan
# format string:
# 1. f-string (direkomendasikan)
# Metode ini paling mudah dan efisien karena variabel dapat langsung
# disisipkan ke dalam string.
# nama = "Andi"
# umur = 19
# print(f"Halo, nama saya {nama}, umur saya {umur} tahun.")

# 2. Metode .format()
# Menempatkan placeholder {} di dalam string, kemudian mengisinya
# dengan nilai melalui fungsi .format().
# nama = "Budi"
# umur = 20
# print("Halo, nama saya {}, umur saya {} tahun.".format(nama,
# umur))

# 3. Operator % (gaya lama)
# Metode lama yang masih didukung, tapi tidak direkomendasikan lagi.
# Dalam format ini, %s untuk string, dan %d untuk bilangan.
# nama = "Citra"
# umur = 21
# print("Halo, nama saya %s, umur saya %d tahun." % (nama, umur))