class rumusbangundatar() :
    print()

def jarak() :
    print("")

#rumus bangun datar
def persegi():
    while True:
        print(        "                                       " "π  Penjelasan Singkat Tentang Bangun Datar Persegi \n"                                      
              "                                       " "------------------------------------------------------------\n"
              "                                       " " Persegi adalah bangun datar 2 dimensi yang dibentuk oleh empat sisi yang sama panjang \n "
              "                                       " "dan keempat titik sudutnya membentuk sudut siku-siku (90ΒΊ) \n")
        print("                                       " '=============================================================\n'
              "                                       " '>>  π Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
              "                                       " '>>    β Luas      = sisi x sisi x sisi (SXSXS)            <<\n'
              "                                       " '>>    β Keliling  = 4 x sisi                              <<\n'
              "                                       " '============================================================\n')
        try:
            s = int(input("                                       " "Masukkan Sisi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = s * s
            keliling    = 4 * s
            hasil       = [luas, keliling]
        break
    return hasil

def persegiPanjang():
    while True:
        # rumus bangun datar
        print("                                       " " π  Penjelasan Singkat Tentang Bangun Datar Persegi Panjang \n"
              "                                       " "------------------------------------------------------------\n"
              "                                       " " Persegi Panjang adalah bangun datar 2 dimensi yang mempunyai 2 pasang sisi sejajar \n "
              "                                       " "yang sama Panjang dan mempunyai 4 titik sudut siku-siku \n")
        print(
            "                                       " '=============================================================\n'
            "                                       " '>>  π Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                       " '>>    β Luas      = Panjang x Lebar                       <<\n'
            "                                       " '>>    β Keliling  = 2 x (Panjang + Lebar)                 <<\n'
            "                                       " '============================================================\n')
        try:
            p = int(input("                                       " "Masukkan Panjang : "))
            l = int(input("                                       " "Masukkan Lebar   : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = p * l
            keliling    = 2 * (p + l)
            hasil       = [luas, keliling]
        break
    return hasil

def segitiga():
    while True:
        # rumus bangun datar
        print("                                      " "  π  Penjelasan Singkat Tentang Bangun Datar Segitiga \n"
              "                                      " "----------------------------------------------------\n"
              "                                      " "  Segitiga adalah bangun datar yang terdiri dari 3 sisi garis lurus \n "
              "                                      " " dengan 3 titik sudut yang berjumlah 180ΒΊ \n")
        print(
            "                                       " '=============================================================\n'
            "                                       " '>>  π Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                       " '>>    β Luas      = 1/2 x Alas x Tinggi                   <<\n'
            "                                       " '>>    β Keliling  = a + b + c                             <<\n'
            "                                       " '============================================================\n')
        try:
            a = int(input("                                       " "Masukkan Alas   : "))
            t = int(input("                                       " "Masukkan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = 0.5 * a * t
            keliling    = a + t + t
            hasil       = [luas, keliling]
        break
    return hasil

def lingkaran():
    while True:
        # rumus bangun datar
        print("                                     " "  π  Penjelasan Singkat Tentang Bangun Datar Lingkaran \n"
            "                                     " "-------------------------------------------------------\n"
            "                                     " "  Lingkaran adalah bangun datar dua dimensi dibentuk oleh himpunan semua titik  \n "
            "                                     " " yang mempunyai jarak sama dari suatu titik tetap \n"
            "                                     " "πΉ Pusat lingkaran (P): Titik tetap pada lingkaran disebut sebagai pusat lingkaran\n"
            "                                     " "πΉ Jari-jari (r): jarak titik lainnya pada pusat lingkaran disebut sebagai jari-jari lingkaran\n"
            "                                     " "πΉ Garis lengkung: Himpunan seluruh titik lingkaran lalu membentuk garis lengkung yang menjadi keliling lingkaran\n"
            "                                     " "πΉ Diameter (d): garis yang ditarik oleh dari dua titik pada garis lengkung dan melewati titik pusat disebut sebagai \n"
            "                                     " "  diameter (d) .Diameter lingkaran memiliki panjang 2 Γ r \n"
            "                                     " "πΉ phi (Ο): nilai perbandingan antara keliling serta diameter lingkaran selalu konstan yakni 3,14159 (dibulatkan menjadi 3,14) \n"
            "                                     " "  atau 22/7. Nilai ini didapatkan dari Keliling Γ· Diameter = phi\n")
        print("                                   " '=============================================================\n'
            "                                     " '>>  π Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                     " '>>    β Luas      =  Ο x r x r                            <<\n'
            "                                     " '>>    β Keliling  =  Ο x d                                <<\n'
            "                                     " '============================================================\n')
        try:
            r = int(input("                                       " "Masukkan Jari-Jari : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            if r % 7 == 0:
                luas        = 22 / 7 * r * r
                keliling    = 2 * (22 / 7 * r)
                hasil       = [luas, keliling]
            else:
                luas        = 3.14 * r * r
                keliling    = 2 * 3.14 * r
                hasil       = [luas, keliling]
        break
    return hasil

def jajargenjang():
    while True:
        print("                                     " "  π  Penjelasan Singkat Tentang Bangun Datar JajarGenjang \n"
              "                                     " "-------------------------------------------------------\n"
              "                                     " "  Pengertian dari jajar genjang sendiri merupakan suatu bangun datar 2 dimensi yang dibentuk atas 2  \n "
              "                                     " " buah pasang rusuk yang di mana pada masing β masing nya memiliki ukuran sama panjang serta sejajar dengan pasangan nya \n"
              "                                     " " Kemudian jajar genjang memiliki 2 buah pasang sudut siku β siku yang di mana pada masing β \n"
              "                                     " " masing sudutnya sama besar dengan sudut di depan nya.\n")
        print(
            "                                       " '=============================================================\n'
            "                                       " '>>  π Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                       " '>>    β Luas      = 2    x  (a + b)                       <<\n'
            "                                       " '>>    β Keliling  = ALas x  Tinggi                        <<\n'
            "                                       " '=============================================================\n')
        try:
            a = int(input("                                       " "Masukkan Alas   : "))
            t = int(input("                                       " "Masukkan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = a * t
            keliling    = 2 * (a + t)
            hasil       = [luas, keliling]
        break
    return hasil

confirm = "YES"
while confirm == "YES":
    print('\n')
    print(" \t\t\t\t\t\t\t\t\t" "=========================================================================================")
    print(" \t\t\t\t\t\t\t\t\t" ">>                                     SELAMAT DATANG                                  <<")
    print(" \t\t\t\t\t\t\t\t\t" ">>                                 DI PROGRAM  BANGUN DATAR                            <<")
    print(" \t\t\t\t\t\t\t\t\t" "=========================================================================================")
    print(" \t\t\t\t\t\t\t\t\t" "π            JENIS BANGUN DATAR                                KODE                   π")
    print(" \t\t\t\t\t\t\t\t\t" "=========================================================================================")
    print(" \t\t\t\t\t\t\t\t\t" "π              β PERSEGI                          βοΈ       KODE [P]                   π")
    print(" \t\t\t\t\t\t\t\t\t" "π              β PPERSEGI PANJANG                 βοΈ       KODE [PP]                  π")
    print(" \t\t\t\t\t\t\t\t\t" "π              β SEGITIGA                         βοΈ       KODE [SGT]                 π")
    print(" \t\t\t\t\t\t\t\t\t" "π              β LINGKARAN                        βοΈ       KODE [LING]                π")
    print(" \t\t\t\t\t\t\t\t\t" "π              β JAJARGENJANG                     βοΈ       KODE [JJG]                 π")
    print(" \t\t\t\t\t\t\t\t\t" "=========================================================================================\n")
    print(" \t\t\t\t\t\t\t\t\t" "Silahkan Pilih Salah Satu Program Yang Kamu ingin Kan :) :) :) \n "
          " \t\t\t\t\t\t\t\t\t" " β‘  Contoh  ketikan KODE [ P ] Untuk Memilih Persegi \n" )

    #input / output
    pilihan = input("                                       " "Masukkan Pilihan Kamu π π βΊοΈ  \n\n"
                    "                                       " "[P]-[PP]-[SGT]-[LING]-[JJG] :  ")
    if pilihan == "P":
        hasil = persegi()
        jarak()
        print("                                       " ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN PEREGI  <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("                                       " "Luas Dan Keliling Persegi Adalah Sebagai Berikut")
        print("                                       " "------------------------------------------------")
        print("                                       " "Luas Persegi                       : {}".format(hasil[0]))
        print("                                       " "Keliling Persegi                   : {}".format(hasil[1]))

    elif pilihan == "PP":
        hasil = persegiPanjang()
        print("                                       " ">>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN PEREGI PANJANG  <<<<<<<<<<<<<<<<<<<<<<<<")
        print("                                       " "Luas Dan Keliling Persegi Panjang Adalah Sebagai Berikut")
        print("                                       " "--------------------------------------------------------")
        print("                                       " "Luas Persegi Panjang                : {}".format(hasil[0]))
        print("                                       " "Keliling Persegi Panjang            : {}".format(hasil[1]))
    elif pilihan == "SGT":
        hasil = segitiga()
        print("                                       " ">>>>>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN SEGITIGA  <<<<<<<<<<<<<<<<<<<<<<<<<<<")

        print("                                       " "Luas Dan Keliling Segitiga Adalah Sebagai Berikut")
        print("                                       ""-------------------------------------------------")
        print("                                       " "Luas Segitiga                       : {}".format(hasil[0]))
        print("                                       " "Keliling Segitiga                   : {}".format(hasil[1]))
    elif pilihan == "LING":
        hasil = lingkaran()
        print("                                       " ">>>>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN LINGKARAN  <<<<<<<<<<<<<<<<<<<<<<<<<<<")

        print("                                       " "Luas Dan Keliling Lingkaran Adalah Sebagai Berikut")
        print("                                       ""--------------------------------------------------")
        print("                                       " "Luas Lingkaran                      : {}".format(hasil[0]))
        print("                                       " "Keliling Lingkaran                  : {}".format(hasil[1]))
    elif pilihan == "JJG":
        hasil = jajargenjang()
        print("                                       " ">>>>>>>>>>>>>>>>>>>>>>>>>  BANGUN JAJARGENJANG  <<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("                                       " "Luas Dan Keliling Jajar Genjang Adalah Sebagai Berikut")
        print("                                       ""------------------------------------------------")
        print("                                       " "Luas Jajargenjang                   : {}".format(hasil[0]))
        print("                                       " "Keliling Jajargenjang               : {}".format(hasil[1]))
    else:
        print("                                       " "Input Tidak Valid")
    jarak(),jarak()



    confirm = input("                                       " "Apakah Kamu Ingin Mengulangi Program ini Lagi YES OR NO : ")
    print("                                       " "______________________________________________________________\n\n\n\n")
    jarak()
    if confirm ==  "NO":
        print("                                       "         "Terimakasih Telah  mencoba π£ π£ π£ ")
        print('-'*800)
        print("\n\n")
        break
    elif confirm == "YES":
        continue
    else:
        print('-' * 800)
        print("                                       " "β οΈ\t\t\t\t\t   Upsss.... Input Tidak Valid  Terimakasih Telah  mencoba π£ π£ π£  βββ")
        print('-' * 800)
        print("\n\n\n")


