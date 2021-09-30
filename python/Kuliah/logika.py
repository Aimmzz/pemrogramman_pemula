print("Nama : Nelfa Rizki Aulia")
print("NIM  : 10200100")
print("                            Hotel Liburan Yuk         ")
print("="*70)
print("Kode Kamar         Nama Kamar      Kode Kelas    Nama Kelas      Harga        ")
print("    A              Anyelir              1           VIP          350000       ")
print("                                        2         Kelas 1        250000       ")
print("                                        3         Kelas 2        150000       ")
print("    C              Cempaka              1           VIP          500000       ")
print("                                        2         Kelas 1        400000       ")
print("                                        3         Kelas 2        300000       ")
print("    M              Melati               1           VIP         1000000       ")
print("                                        2         Kelas 1        750000       ")
print("                                        3         Kelas 2        650000       ")
print("="*70)
nama = input("Nama Penyewa : ")
kamar = input("Kode Kawar [A/C/M] : ")
kode_kelas = int(input("Kode Kelas [1/2/3] : "))
harga_kamar = 0
nama_kelas = ""
nama_kamar = ""
if kamar == 'A':
    nama_kamar = 'Anyelir'

    if kode_kelas == 1 :
        nama_kelas = 'VIP'
        harga_kamar = 35000
    elif kode_kelas == 2 :
        nama_kelas = 'Kelas 1'
        harga_kamar = 250000
    elif kode_kelas == 3 :
        nama_kelas = 'Kelas 2'
        harga_kamar = 150000
elif kamar == 'C':
    nama_kamar = 'Cemapaka'

    if kode_kelas == 1 :
        nama_kelas = 'VIP'
        harga_kamar = 500000
    elif kode_kelas == 2 :
        nama_kelas = 'Kelas 1'
        harga_kamar = 400000
    elif kode_kelas == 3 :
        nama_kelas = 'Kelas 2'
        harag_kamar = 300000
elif kamar == 'M' :
    nama_kamar = 'Melati'

    if kode_kelas == '1':
        nama_kelas = 'VIP'
        harga_kamar = 1000000
    elif kode_kelas == '2':
        nama_kelas = 'Kelas 1'
        harga_kelas = 750000
    elif kode_kelas == '3':
        nama_kelas = 'Kelas 2'
        harga_kamar = 650000
menginap = int(input("Lama Menginap : "))
free =""
if menginap >= 7 :
    free=("Souvenir          = Free Lunch")
total = int(harga_kamar) * menginap
print("="*40)
print("Data Pemesan Hotel Liburan Yuk  ")
print("        Oktober                 ")
print("="*40)
print("Nama Penyewa       = ",nama)
print("Nama Kamar         = ",nama_kamar)
print("Kelas              = ",nama_kelas)
print("Lama Menginap      = ",menginap,("Hari"))
print("Biaya Sewa         = Rp. ",harga_kamar)
print("Biaya Administrasi = Rp. 75000")
print("Total Biaya Sewa   = Rp. ",total)
print("="*40)
print("",free)






