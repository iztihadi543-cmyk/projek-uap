# #Program Python untuk membuka file data txt
# with open("tugas.txt", "r")as myFile:
#     isi = myFile.read()
# if len(isi) > 0 :
#     print ("File ada isi")
# else :
#     print("File nggak ada isi")

    
# # #Buatlah program Python untuk tulis ulang file (write) tambah catatan baru (append)
# # pilihan = input("Pilih mode (write/append): ")

# if pilihan == "write":
# #     teks = input("Tulis ulang file: ")
# #     with open("tugas.txt", "w") as file:
# #         file.write(teks + "\n")
# #     print("File telah ditulis ulang.")
# # elif pilihan == "append":
# #     teks = input("Tambah catatan baru: ")
# #     with open("tugas.txt", "a") as file:
# #         file.write(teks + "\n")
# #     print("Catatan baru telah ditambahkan.")
# # else:
# #     print("Pilihan tidak valid.")

# #Program yang meminta pengguna menginput beberapa data
# with open("absensi.txt", "a") as file:
#     while True:
#         nama = input("Masukkan nama mahasiswa :")
#         if nama == "selesai":
#             break
#         file.write(nama + "\n")
#         print("Data tersimpan.\n")

# print("Input selesai data sudaah disimpan di absensi.txt.")

class Kucing:

    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        return f' Hewan ini bernama {self.nama} merupakan seekor {self.jenis} '
    


kucing1 = Kucing('miko', 'anj')
kucing2 = Kucing('ranu', 'kurcaci')
print(kucing1.makan())
print(kucing2.makan())