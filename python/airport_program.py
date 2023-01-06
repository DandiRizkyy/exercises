class Flight():
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
       # Menggunakan list
        self.penumpang = []

# Fungsi menambahkan penumpang
    def tambah_penumpang(self, nama_penumpang):
        if not self.kursi_kosong():
         return False
                    #append berguna untuk menambahkan sesuatu ke list yang kosong
        self.penumpang.append(nama_penumpang)
        return True
    def kursi_kosong(self):
        return self.kapasitas - len(self.penumpang)

# Kapasitas Penumpang
penerbangan = Flight(3)
penumpang = ["Budi", "Andi", "Mike", "Ron"]
for orang in penumpang:
    sukses = penerbangan.tambah_penumpang(orang)
    if sukses:
     print(f"Penumpang {orang} telah ditambahkan dengan sukses.")
    else:
     print(f"Tidak cukup tempat duduk untuk {orang}")