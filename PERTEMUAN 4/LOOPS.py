# Loops (perulangan) di Python adalah cara untuk menjalankan kode berulang kali tanpa harus menulisnya berkali-kali
#  Perulangan sangat berguna untuk mengolah data, menghitung, atau mengulang tindakan tertentu sampai kondisi terpenuhi.

# for loop — Perulangan berdasarkan koleksi (list, range, string, dll)
# Digunakan ketika jumlah perulangan sudah diketahui atau kita ingin mengiterasi elemen-elemen suatu objek.

for i in range(5):
    print(i)

buah = ["apel", "mangga", "jeruk"]
for item in buah:
    print(item)

for huruf in "python":
    print(huruf)

x = 1
while x <= 5:
    print(x)
    x += 1
