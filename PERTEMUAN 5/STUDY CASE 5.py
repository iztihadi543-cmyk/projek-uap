# Buat fungsi ongkir(jarak, tarif_per_km = 5000) yang akan
# mengembalikan total biaya ongkir berdasarkan jarak tempuh. Ingat,
# parameter tarif_per_km harus punya nilai default 5000.
def ongkir(jarak, tarif_perkm = 5000):
    return jarak * tarif_perkm
print(ongkir(10, 8000))

# Buat fungsi notifikasi(nama, jumlah = 1) yang akan mengembalikan
# string notifikasi dengan beberapa kondisi, pastikan parameter
# jumlah punya nilai default 1.
def notifikasi(nama, jumlah = 1):
    if jumlah > 1:
        return f"Hallo {nama}, kamu punya {jumlah} pesan baru."
    else:
        return f"Hallo {nama}, pesanan Anda sedang diproses."
print(notifikasi("Andi"))