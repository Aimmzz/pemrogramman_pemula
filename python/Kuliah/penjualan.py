print("===================================")
print("Nama : Rohim Kurniawan")
print("NIM  : 10200041")

print("===================================")
print("*                               *")
print("     GEROBAK FRIED CHICKEN ")
print("     ----------------------")
print("     Kode JenisPotong Harga")
print("     ----------------------")
print("     D   Dada     Rp. 2500")
print("     P   Paha     Rp. 2000")
print("     S   Sayap    Rp. 1500")
print("     --------------------- ")
print("*                              *")
list_jenis = []
list_kode = []
list_banyak = []
list_harga = []
list_harga_satuan = []
banyakje = str(input("     Banyak Jenis      : "))
for i in range (int(banyakje)):
    jenis = print("     Jenis Ke          : ",i+1)
    kode = str(input("     KodePotong[D/P/S] : ")).upper()
    banyak = int(input("     Banyak Potong     : "))
    harga_je = 0
    if kode == "D":
        harga_je = 2500
    elif kode == "P":
        harga_je = 2000
    elif kode == "S":
        harga_je = 1500
    harga = banyak * int(harga_je)
    list_jenis.append(i+1)
    list_kode.append(kode)
    list_banyak.append(banyak)
    list_harga.append(harga)
    list_harga_satuan.append(harga_je)
    print("     -------------------------")
print("     GEROBAK FRIED CHICKEN ")
print("     ----------------------")
print("     No. Jenis     Harga     Banyak  Jumlah")
print("         Potong    Satuan    Beli    Harga")
print("     ----------------------")
jumlah_bayar = 0
for i in range(len(list_jenis)):
    print("\n     ",list_jenis[i] ,". ",list_kode[i],"     ",list_harga_satuan[i] ,"    " ,list_banyak[i],"   " ,"Rp", list_harga[i])
    jumlah_bayar = jumlah_bayar + list_harga[i]
print("     ---------------------")
print("                   Jumlah Bayar Rp.",jumlah_bayar)
pajak = jumlah_bayar * 10/100
print("                   Pajak 10%    Rp.",pajak)
total = jumlah_bayar + pajak
print("                   Total bayar  Rp.",total)