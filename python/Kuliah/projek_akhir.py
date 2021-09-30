print("="*50)
print("                 PROJECK AKHIR KELOMPOK 3 ")
print("                         10.1A.07         ")
print("Angota Kelompok : Qurrota Ayun H.P    - 10200043")
print("                  Gloria Wiradika Zai - 10200072 ")
print("                  Rohim Kurniawan     - 10200041")
print("Tema            : Aplikasi Pembelajaran Matematika Dasar")
print("                  Bangun Datar ")
print("="*50)
print("            APLIKASI PEMBELAJARAN MATEMATIKA DASAR BANGUN DATAR")
print("A. Pengertian Bagun Datar :")
print("Bangun Datar adalah  suatu bidang datar yang tersusun  oleh titik")
print("atau garis-garis yang menyatu membentuk bangun 2 Dimensi")
print("yang mempunyai keliling dan luas.")
print("-")
print("B. Bangun datar kebagi menjadi 7 macam tetapi kelompok saya akan")
print("akan membahas 5 jenis saja yaitu:")

def persegi():
    while True:
        try:
            s = int(input("Masukan Sisi : "))
        except ValueError:
            print("Input Tidak Valid ")
            continue
        else:
            luas = s * s
            keliling = 4 * s
            hasil = [luas , keliling]
        break
    return

def persegipanjang():
    while True:
        try:
            p = int(input("Masukkan Panjang : "))
            l = int(input("Masukkan Lebar : "))
        except ValueError:
            print("input tidak valid")
            continue
        else:
            luas = p * l
            keliling = 2 * (p + l)
            hasil = [luas,keliling]
        break
    return hasil

def segitiga():
    while True:
        try:
            a = int(input("Masukan alas : "))
            t = int(input("Masukan Tinggi :"))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = 0.5 * a * t
            keliling = a + t + t
            hasil = [luas,keliling]
        break
    return hasil
def lingkaran():
    while True:
        try:
            r = int(input("Masukan Jari-Jari : "))
        except ValueError:
            print("Input Tidak valid")
            continue
        else:
            if r % 7 == 0 :
                luas = 22 / 7 * r * r
                keliling = 2 * (22 / 7 * r)
                hasil = [luas,keliling]
            else:
                luas = 3.14 * r * r
                keliling = 2 * 3.14 * r
                hasil = [luas,keliling]
        break
    return hasil
def jajargenjang():
    while True:
        try:
            a = int(input("Masukan Alas : "))
            t = int(input("Masukan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = a * t
            keliling = 2 * (a + t)
            hasil = [luas,keliling]
        break
    return hasil

confirm = "y"
while confirm == "y":

    print("1. Persegi")
    print("2. Persegipanjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. jajargenjang")

    pilihan = input("Masukan Nomer Bangun Datar Yang Anda Pilih(1,2,3,4,5) : ")
    if pilihan == "1":
        hasil = persegi()
        print("Luas Pesegi : {}".format(hasil[0]))
        print("Keliling Persegi : {}".format(hasil[1]))
    elif pilihan == "2":
        hasil = persegipanjang()
        print("Luas Persegi Panjang : {}".format(hasil[0]))
        print("Keliling Persegi Panajng : {}".format(hasil[1]))
    elif pilihan == "3":
        hasil = segitiga()
        print("Luas Segitiga : {}".format(hasil[0]))
        print("Keliling Segitiga : {}".format(hasil[1]))
    elif pilihan == "4":
        hasil = lingkaran()
        print("Luas Lingkaran : {}".format(hasil[0]))
        print("Keliling Lingkaran : {}".format(hasil[1]))
    elif pilihan == "5":
        hasil = jajargenjang()
        print("Luas Jajargenjang : {}".format(hasil[0]))
        print("Keliling Jajargenjang : {}".format(hasil[1]))
    else:
        print("Input Tidak Valid")
    confirm = input("Apakah  Anda Ingin Mencoba Lagi ? (y,t) : ")
    if confirm == "t":
        break
    elif confirm == "y":
        continue
    else:
        print("COBA ANDA BACA ARAHAN YANG MUNCUL !!!")
print("Terimakasih Telah Mencoba")







