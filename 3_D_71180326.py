inputan = input("Masukan daftar belanja anda : ")
temp = inputan.lower()
daftarBelanja =list(temp.split(", "))
daftarBelanja[0] = daftarBelanja[0].title()
daftarBelanja[1] = daftarBelanja[1].title()
daftarBelanja[2] = daftarBelanja[2].title()
print("Daftar belanja : " + str(daftarBelanja))
tambahinput = input("Masukan barang yang ingin ditambahkan : ")
temp = tambahinput.lower()
temp = temp.title()
if temp in daftarBelanja:
    temp = tambahinput.upper()
    print("Barang "+temp+" sudah berada dalam daftar belanja.")
else:
    temp = tambahinput.upper()
    daftarBelanja.append(temp)
    print("Hasil penambahan pada daftar belanja : "+str(daftarBelanja))

