hargaMakan = input("Harga makanan sebesar Rp ")
hargaSnack = input("Harga snack sebesar Rp ")
hargaMinum = input("Harga minuman sebesar Rp ")
uang = input("Uang yang anda bawa sebesar Rp ")

totalHarga = int(hargaMakan)+int(hargaSnack)+int(hargaMinum)
print("Total yang harus anda bayar sebesar Rp " + str(totalHarga))
totalSemua = int(uang) - int(totalHarga)
if(totalSemua > 0):
    print("Anda memiliki kembalian sebesar Rp "+str(totalSemua))
elif(totalSemua == 0):
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
else:
    print("Uang anda kurang! Anda memiliki utang sebesar Rp " + str(abs(totalSemua)))