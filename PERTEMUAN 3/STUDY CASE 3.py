# 1. Buatlah sebuah program sederhana yang meminta input pengguna
# 3 angka, lalu cek angka yang terbesar dari ketiga angka tersebut
# menggunakan percabangan dan tampilkan.

# angka1 = int(input(""))
# angka2 = int(input(""))
# angka3 = int(input(""))

# if angka1 >= angka2 and angka1 >= angka3 :
#     print(f'{angka1} adalah angka terbesar')
# elif angka2 >= angka1 and angka2 >= angka3 :
#     print(f'{angka2} adalah angka terbesar')
# else :
#     print(f'{angka3} adalah angka terbesar')

# Buatlah sebuah program kalkulator sederhana menggunakan
# match-case. Input terdiri dari ‘A’, ‘operator’, dan ‘B’, dimana A adalah
# bilangan pertama, B adalah bilangan kedua, dan operator adalah
# operator aritmatika (+ dan -).

a = int(input("Masukan bilangan pertama :"))
b = int(input("Masukan bilangan kedua :"))
operator = input("Pilih opsi (+ - : x)")

if operator == "+" :
    print(a + b)
elif operator == "-" :
    print(a - b)
elif operator == ":" :
    print(a / b)
else :
    print(a * b )