print("Nama : Rohim Kurniawan")
print("NIM  : 10200041")
print("Kelas: 10.1A.07")
print("*                             *")
print("-"*40)
print("          DAFTAR HARGA HANDPONE BULAN")
print("                 NOVEMBER           ")
print("               TOKO AIM_BIH         ")
print("-"*40)
print("Kode Barang    Nama Hendpone    Harga Handpone")
print("-"*40)
print("     A         OPPO A3s         Rp.1.450.000")
print("     B         Redmi Note 4X    Rp.1.200.000")
print("     C         Realme 3         Rp.2.175.000")
print("     D         Zenfone M2       Rp.2.800.000")
print("     E         Galaxy A50       Rp.3.300.000")
print("-"*40)
list_data = []

list_kode = []
list_nama = []
list_harga= []
list_beli = []



jumlah_pesanan = int(input("Jumlah Pesanan : "))
print("="*40)
for i in range(jumlah_pesanan):
    print("Data Pesanan KE                   : ", i + 1 )
    data = i + 1

    kode =input("Masukan Kode Handpone [A,B,C,D,E] : ")
    nama = ""
    beli = 0
    if kode == 'A' or kode == 'a' :
        nama = 'OPPO A3s'
        beli = 1450000
    elif kode == 'B' or kode == 'b':
        nama = 'Redmi Note 4X'
        beli = 1200000
    elif kode == 'C' or kode =='c':
        nama = 'Realme 3'
        beli = 2175000
    elif kode == 'D' or kode =='d':
        nama = 'Zenfone M2'
        beli = 2800000
    elif kode == 'E' or kode =='e':
        nama = 'Galaxy A50'
        beli = 3300000
    print("Nama Handpone                     : ",nama)
    print("Harga Handpone                    : ",beli)
    harga = beli
    print("="*40)
    list_data.append(data)

    list_kode.append(kode)
    list_nama.append(nama)
    list_harga.append(harga)
def total():
    print ("Total Harga yang harus di bayar")

print("=" * 45)
total_pemasukan = 0
print("                  TOKO AIM_BIH  ")
print("=" * 45)
print("NO.    Kode       Nama          Harga ")
print("       Handpone   Handpone            ")
print("-" * 45)
jumlah_bayar = 0
pajak = 0
for i in range(len(list_data)):
    jumlah_bayar = jumlah_bayar + list_harga[i]
    pajak = jumlah_bayar * 5/100
    print("\n",list_data[i],"   ","    ",list_kode[i],"   ",
          list_nama[i],"     ",list_harga[i],"   ")
print("-" * 45)
print("Jumlah Bayar                  : ",jumlah_bayar)
print("Pajak                         : ",(pajak))

total()
hadiah = ""
akhir = jumlah_bayar + (pajak)
if akhir >= 4000000 :
    hadiah = ("Selamat Anda Mendapatkan kaos Toko Aim_bih")
print("Rp.",akhir)
print("#",hadiah,"#")
print("               TERIMAKASIH TELAH MEMBELI HANDPONE")
print("                       DI TOKO AIM_BIH")




