print("="*40)
print("Nama : Rohim Kurniawan")
print("Nim  : 10200041")
print("                 Quis A")
print("="*40)
print("PEMESANAN TIKET KERETA ANTAR KOTA")
print("         OKTOBEER 2020")
print("="*40)
print("Kode Kereta    Nama Kereta   Haraga")
print("-"*40)
print("     1         Argo Bromo    150000 ")
print("     2         Parahiyangan  100000 ")
print("     3         Sembrani       95000 ")
print("     4         Argo Lawu      80000 ")
print("_"*40)
print("*                             *")
list_data = []
list_np = []
list_kode = []
list_harga = []
list_nama = []
list_beli = []
list_jb = []
list_total = []
jumlah_pesanan = (int(input("Masukan jumlah Pesanan : ")))
print("="*40)
for i in range(jumlah_pesanan):
    print("Data Pemesanan ke               : " , i + 1)
    data = i+1
    np = str(input("Nama Pemesan                    : "))
    kode = int(input("Masukan Kode Kereta [ 1,2,3,4 ] : "))
    nama = ""
    if kode == 1:
        nama = 'Argo Bromo'
    elif kode == 2:
        nama = 'Parahiyangan'
    elif kode == 3:
        nama = "Sembrani"
    elif kode == 4:
        nama = "Argo Lawu"
    print("Nama Kereta                     : ",nama)
    beli = 0
    if kode == 1:
        beli = 150000
    elif kode == 2:
        beli = 100000
    elif kode == 3:
        beli = 95000
    elif kode == 4:
        beli = 80000
    print("Haraga                          : ",(beli))
    harga = beli
    jumlah_beli = (input("Masukan Jumlah Beli             : "))
    print("="*40)
    total = beli * (int(jumlah_beli))

    list_data.append(i+1)
    list_np.append(np)
    list_kode.append(kode)
    list_nama.append(nama)
    list_harga.append(harga)
    list_jb.append(jumlah_beli)
    list_total.append(total)
print("*                                                    *")
print("="*70)

total_pemasukan = 0


print("="*70)
print("                    STASIUN KERETA API JAKARTA KOTA ")
print("                         LAPORAN PENJUALAN TIKET ")
print("="*70)
print("No.  Nama     Kode     Nama          Jumlah   Haraga     Total")
print("     Pemesan  Kereta   Kereta        Beli                   ")
print("="*70)
for i in range (len(list_data)):
    total_pemasukan = total_pemasukan + list_total[i]
    print("\n ", list_data[i],"   ",list_np[i],"   ", list_kode[i] ,"   ",list_nama[i] ,"      ",
          list_jb[i] ,"      ",list_harga[i] ,"      ",list_total[i] ,"         ")
print("="*70)
print("total Pemasukan                                            : ",total_pemasukan)





