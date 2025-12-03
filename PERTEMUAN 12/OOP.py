# class Produk:
#     def __init__(self, nama, harga):
#         self.nama = nama
#         self.harga = harga

# class Keranjang:
#     def __init__(self):
#         self.barang = []

#     def tambah(self, produk):
#         self.barang.append(produk)

#     def total(self):
#         return sum(p.harga for p in self.barang)

# p1 = Produk("Roti", 15000)
# p2 = Produk("Susu", 12000)

# keranjang = Keranjang()
# keranjang.tambah(p1)
# keranjang.tambah(p2)

# # print("Total belanja:", keranjang.total())

# class Mahasiswa:
#     def __init__(self, nama, nim, jurusan):
#         self.nama = nama
#         self.nim = nim
#         self.jurusan = jurusan

#     def info(self):
#         return f"{self.nama} ({self.nim}) - {self.jurusan}"

# m1 = Mahasiswa("Ayu", "220101", "Informatika")
# print(m1.info())

# class Kucing:
#     kaki = 4

#     def __init__(self, nama, warna):
#         self.nama = nama
#         self.warna = warna

#     def makan(self):
#         return f'{self.nama} memakan whiskas'


# kucing1 = Kucing('meo', 'putih')

# print(f'{kucing1.nama} berwarna {kucing1.warna}')
# print(kucing1.makan())

# class Mahasiswa:
#     def __init__(self, nama, nim, jurusan, kelas):
#         self.nama = nama
#         self.nim = nim
#         self.jurusan = jurusan
#         self.kelas = kelas

#     def info(self):
#         return f"{self.nama} ({self.nim}) - {self.jurusan} {self.kelas}"

# m = Mahasiswa("Ranu", "2527052006", "Sistem Informasi", "A")
# print(f"saya adalah {m.nama} NIM saya {m.nim} jurusan saya {m.jurusan} dan saya dari kelas {m.kelas} ")
# print(m.info())

class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama        # atribut public
        self.__saldo = saldo    # atribut private

    # method public untuk melihat saldo
    def lihat_saldo(self):
        return f"Saldo {self.nama}: Rp{self.__saldo}"

    # method public untuk menambah saldo
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setoran Rp{jumlah} berhasil!")
        else:
            print("Jumlah setoran tidak valid.")

    # method public untuk menarik saldo
    def tarik(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan Rp{jumlah} berhasil!")
        else:
            print("Saldo tidak mencukupi.")
            

# Membuat objek
akun1 = AkunBank("Raid", 500000)

# Akses via method (benar)
print(akun1.lihat_saldo())

akun1.setor(200000)
print(akun1.lihat_saldo())

akun1.tarik(300000)
print(akun1.lihat_saldo())

