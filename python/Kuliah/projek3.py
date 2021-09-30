def borer1 () :
    print(":"*75)
def border2 () :
    print("="*75)
def jarak() :
    print("")

    # rumus bangun datar
def persegi():
    while True:
        try:
            border2()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN PEREGI  <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            border2()
            print("1. Persegi\n"
                  "Persegi adalalah bangun datar yang terbentuk dari empat buah sisi yang sama\n"
                  "panjang dan empat sudut yang sama besar 90°. Sifat-sifat Persegi:\n"
                  "\u2713 Memiliki dua pasang sisi yang sejajar dan sama panjang.\n"
                  "\u2713 Memiliki empat simetri lipat.\n"
                  "\u2713 Memiliki simetri putar tingkat empat.")
            print("\nRumus Persegi:\n"
                  "L = S x S untuk mencari luas persegi\n"
                  "K = 4 x S untuk mencari keliling persegi\n"
                  "Ket: S = nilai sisi/rusuk persegi")
            s = int(input("Masukkan nilai Sisi Persegi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = s * s
            keliling = 4 * s
            hasil = [luas, keliling]
        break
    return hasil

def persegiPanjang():
    while True:
        try:
            p = int(input("Masukkan Panjang : "))
            l = int(input("Masukkan Lebar   : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = p * l
            keliling = 2 * (p + l)
            hasil = [luas, keliling]
        break
    return hasil

def segitiga():
    while True:
        try:
            a = int(input("Masukkan Alas   : "))
            t = int(input("Masukkan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas = 0.5 * a * t
            keliling = a + t + t
            hasil = [luas, keliling]
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

    jarak()
    jarak()
    print("B. BANGUN DATAR")
    print("\n Bangun datar adalah suatu bidang datar yang tersusun oleh titik\n"
          "atau garis-garis yang menyatu membentuk bangun 2 dimensi yang mempunyai\n"
          "keliling dan luas.Bangun datar tebagi menjadi delpan bagian yaitu persegi,\n"
          "persegi panjang,segitiga,lingkaran,trapesium,jajargenjnag,belah ketupat,\n"
          "dan layang layang.Kali ini saya membahas 5 bangun datar,Lihat di tabel")
    jarak()
    borer1()
    print("::                           PILIH BANGUN DATAR                 "
          "         ::")
    print("::=======================================================================::")
    print("::           NO                           JENIS BANGUN DATAR             ::")
    print("::=======================================================================::")
    print("::           1.                              Persegi                     ::")
    print("::           2.                              Persegi Panjang             ::")
    print("::           3.                              Segitiga                    ::")
    print("::           4.                              Lingkaran                   ::")
    print("::           5.                              Jajargenjang                ::")
    borer1()
    jarak()
    # input / output
    pilihan = input("Masukkan nomer materi yang ingin anda coba (1/2/3/4/5) : ")
    jarak()
    if pilihan == "1":
        hasil = persegi()
        jarak()

        print("Luas Persegi                       : {}".format(hasil[0]))
        print("Keliling Persegi                   : {}".format(hasil[1]))
        print("Jadi Hasil dari L=")

    elif pilihan == "2":
        hasil = persegiPanjang()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN PEREGI PANJANG  <<<<<<<<<<<<<<<<<<<<<<<<")
        border2()
        print("Luas Dan Keliling Persegi Panjang Adalah Sebagai Berikut")
        print("--------------------------------------------------------")
        print("Luas Persegi Panjang                : {}".format(hasil[0]))
        print("Keliling Persegi Panjang            : {}".format(hasil[1]))
    elif pilihan == "3":
        hasil = segitiga()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN SEGITIGA  <<<<<<<<<<<<<<<<<<<<<<<<<<<")
        border2()
        print("Luas Dan Keliling Segitiga Adalah Sebagai Berikut")
        print("-------------------------------------------------")
        print("Luas Segitiga                       : {}".format(hasil[0]))
        print("Keliling Segitiga                   : {}".format(hasil[1]))
    elif pilihan == "4":
        hasil = lingkaran()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN LINGKARAN  <<<<<<<<<<<<<<<<<<<<<<<<<<<")
        border2()
        print("Luas Dan Keliling Lingkaran Adalah Sebagai Berikut")
        print("--------------------------------------------------")
        print("Luas Lingkaran                      : {}".format(hasil[0]))
        print("Keliling Lingkaran                  : {}".format(hasil[1]))
    elif pilihan == "5":
        hasil = jajargenjang()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN JAJARGENJANG  <<<<<<<<<<<<<<<<<<<<<<<<<<")
        border2()
        print("Luas Dan Keliling Jajar Genjang Adalah Sebagai Berikut")
        print("------------------------------------------------")
        print("Luas Jajargenjang                   : {}".format(hasil[0]))
        print("Keliling Jajargenjang               : {}".format(hasil[1]))
    else:
        print("Input Tidak Valid")
    border2()
    jarak()
    jarak()
    jarak()
    confirm = input("             Apakah Anda Ingin Mencoba Lagi? (y/t) : ")
    jarak()
    if confirm == "t":
        break
    elif confirm == "y":
        continue
    else:
        print("BERANG-BERANG NYOLONG KEDONDONG, PILIHAN CUMA ADA DUA DONG")

print("Terimakasih Telah  mencoba      :D   :D  :D")
print("\U0001f600","u'\u2713")
print("                                       "         "Terimakasih Telah  mencoba 🐣 🐣 🐣 ")
        print('-'*800)
        print("\n\n")
        break
    elif confirm == "y":
