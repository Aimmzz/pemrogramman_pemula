print("-"*60)
print("Nama : Rohim kurniawan")
print("NIM  : 10200041")
print("Kelas: 10.1A.07")
print("-"*60)
print("*                             *")
print("-"*63)
print("                 RINCIAN PENDAFTARAN")
print("                   *AGEN FASHION*  ")
print("                      AIM_BIH     ")
print("-"*63)
print("Kode Agen    Nama Agen      Kelas     Tingkatan      Harga")
print("                            Agen        Agen        Daftar")
print("-"*63)
print("   P        Agen Pakaian      1        Reguler      Rp.100.000")
print("                              2        Spesial      Rp.150.000")
print("   A        Agen Aksesoris    1        Reguler      Rp. 90.000")
print("                              2        Spesial      Rp. 95.000")
print("   E        Agen Elektronik   1        Reguler      Rp.500.000")
print("                              2        Spesial      Rp.750.000")
print("-"*63)
list_data = []
list_nama = []
list_kode = []
list_na   = []
list_ka   = []
list_tingkat = []
list_harga = []


jumlah_pendaftar = int(input("Junmlah Pendaftar : "))
print("="*40)
for i in range(jumlah_pendaftar) :
    print("Data Pendaftar           : ", i + 1)
    data = i + 1
    nama = input("Nama Pendaftar           : ")
    kode = input("Masukan Kode Agen [P,A,E]: ")
    na = ""
    ka = int(input("Kelas Agen [1,2]         : "))
    tingkat = ""
    harga = 0
    if kode == 'P':
        na = 'Agen Pakaian'
        if ka == 1 :
            tingkat = 'Reguler'
            harga = 100000
        elif ka == 2 :
            tingkat = 'Spesial'
            harga = 150000
    elif kode == 'A' :
        na = 'Agen Aksesoris'
        if ka == 1 :
            tingkat = 'Reguler'
            harga = 90000
        elif ka == 2 :
            tingkat = 'Spesial'
            harga = 95000
    elif kode == 'E' :
        na = 'Agen Eleklronik'
        if ka == 1 :
            tingkat = 'Reguler'
            harga = 500000
        elif ka == 2 :
            tingkat = 'Spesial'
            harga = 750000
    print("Nama Agen Ynag Di pilih  : ",na)
    print("Tingkatan Agen           : ",tingkat)
    print("Harga Pendaftaran        : ",int(harga))
    print("-"*40)
    list_data.append(data)
    list_nama.append(nama)
    list_kode.append(kode)
    list_na.append(na)
    list_ka.append(ka)
    list_tingkat.append(tingkat)
    list_harga.append(harga)

print("-"*63)
print("              DATA PENDAFTAR AGEN FASHION")
print("                     BULAN NOVEMBER      ")
print("-"*40)
print(" NO       Nama Pendaftar      Agen Yang di Pilih     Tingkatan    Harga Daftar")
print("-"*40)
for i in range(len(list_data)):
    print("\n", list_data[i],"          ",list_nama[i],"     ",list_na[i]
          ,"         ",list_tingkat[i],"         ",list_harga[i],"         ")
print("-"*60)
print("Biaya Admin")



def biru():
    print("Penjualan Tiket pt biru")








