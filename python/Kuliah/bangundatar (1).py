class rumusbangundatar() :
    print()

def jarak() :
    print("")

#rumus bangun datar
def persegi():
    while True:
        print(        "                                       " "📊  Penjelasan Singkat Tentang Bangun Datar Persegi \n"                                      
              "                                       " "------------------------------------------------------------\n"
              "                                       " " Persegi adalah bangun datar 2 dimensi yang dibentuk oleh empat sisi yang sama panjang \n "
              "                                       " "dan keempat titik sudutnya membentuk sudut siku-siku (90º) \n")
        print("                                       " '=============================================================\n'
              "                                       " '>>  📈 Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
              "                                       " '>>    ✅ Luas      = sisi x sisi x sisi (SXSXS)            <<\n'
              "                                       " '>>    ✅ Keliling  = 4 x sisi                              <<\n'
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
        print("                                       " " 📊  Penjelasan Singkat Tentang Bangun Datar Persegi Panjang \n"
              "                                       " "------------------------------------------------------------\n"
              "                                       " " Persegi Panjang adalah bangun datar 2 dimensi yang mempunyai 2 pasang sisi sejajar \n "
              "                                       " "yang sama Panjang dan mempunyai 4 titik sudut siku-siku \n")
        print(
            "                                       " '=============================================================\n'
            "                                       " '>>  📈 Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                       " '>>    ✅ Luas      = Panjang x Lebar                       <<\n'
            "                                       " '>>    ✅ Keliling  = 2 x (Panjang + Lebar)                 <<\n'
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
        print("                                      " "  📊  Penjelasan Singkat Tentang Bangun Datar Segitiga \n"
              "                                      " "----------------------------------------------------\n"
              "                                      " "  Segitiga adalah bangun datar yang terdiri dari 3 sisi garis lurus \n "
              "                                      " " dengan 3 titik sudut yang berjumlah 180º \n")
        print(
            "                                       " '=============================================================\n'
            "                                       " '>>  📈 Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                       " '>>    ✅ Luas      = 1/2 x Alas x Tinggi                   <<\n'
            "                                       " '>>    ✅ Keliling  = a + b + c                             <<\n'
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
        print("                                     " "  📊  Penjelasan Singkat Tentang Bangun Datar Lingkaran \n"
            "                                     " "-------------------------------------------------------\n"
            "                                     " "  Lingkaran adalah bangun datar dua dimensi dibentuk oleh himpunan semua titik  \n "
            "                                     " " yang mempunyai jarak sama dari suatu titik tetap \n"
            "                                     " "🔹 Pusat lingkaran (P): Titik tetap pada lingkaran disebut sebagai pusat lingkaran\n"
            "                                     " "🔹 Jari-jari (r): jarak titik lainnya pada pusat lingkaran disebut sebagai jari-jari lingkaran\n"
            "                                     " "🔹 Garis lengkung: Himpunan seluruh titik lingkaran lalu membentuk garis lengkung yang menjadi keliling lingkaran\n"
            "                                     " "🔹 Diameter (d): garis yang ditarik oleh dari dua titik pada garis lengkung dan melewati titik pusat disebut sebagai \n"
            "                                     " "  diameter (d) .Diameter lingkaran memiliki panjang 2 × r \n"
            "                                     " "🔹 phi (π): nilai perbandingan antara keliling serta diameter lingkaran selalu konstan yakni 3,14159 (dibulatkan menjadi 3,14) \n"
            "                                     " "  atau 22/7. Nilai ini didapatkan dari Keliling ÷ Diameter = phi\n")
        print("                                   " '=============================================================\n'
            "                                     " '>>  📈 Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                     " '>>    ✅ Luas      =  π x r x r                            <<\n'
            "                                     " '>>    ✅ Keliling  =  π x d                                <<\n'
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
        print("                                     " "  📊  Penjelasan Singkat Tentang Bangun Datar JajarGenjang \n"
              "                                     " "-------------------------------------------------------\n"
              "                                     " "  Pengertian dari jajar genjang sendiri merupakan suatu bangun datar 2 dimensi yang dibentuk atas 2  \n "
              "                                     " " buah pasang rusuk yang di mana pada masing – masing nya memiliki ukuran sama panjang serta sejajar dengan pasangan nya \n"
              "                                     " " Kemudian jajar genjang memiliki 2 buah pasang sudut siku – siku yang di mana pada masing – \n"
              "                                     " " masing sudutnya sama besar dengan sudut di depan nya.\n")
        print(
            "                                       " '=============================================================\n'
            "                                       " '>>  📈 Rumus Bangun Datar Persegi Adalah Sebai berikut :   <<\n'
            "                                       " '>>    ✅ Luas      = 2    x  (a + b)                       <<\n'
            "                                       " '>>    ✅ Keliling  = ALas x  Tinggi                        <<\n'
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
    print(" \t\t\t\t\t\t\t\t\t" "📘            JENIS BANGUN DATAR                                KODE                   📘")
    print(" \t\t\t\t\t\t\t\t\t" "=========================================================================================")
    print(" \t\t\t\t\t\t\t\t\t" "📘              ✅ PERSEGI                          ⚙️       KODE [P]                   📘")
    print(" \t\t\t\t\t\t\t\t\t" "📘              ✅ PPERSEGI PANJANG                 ⚙️       KODE [PP]                  📘")
    print(" \t\t\t\t\t\t\t\t\t" "📘              ✅ SEGITIGA                         ⚙️       KODE [SGT]                 📘")
    print(" \t\t\t\t\t\t\t\t\t" "📘              ✅ LINGKARAN                        ⚙️       KODE [LING]                📘")
    print(" \t\t\t\t\t\t\t\t\t" "📘              ✅ JAJARGENJANG                     ⚙️       KODE [JJG]                 📘")
    print(" \t\t\t\t\t\t\t\t\t" "=========================================================================================\n")
    print(" \t\t\t\t\t\t\t\t\t" "Silahkan Pilih Salah Satu Program Yang Kamu ingin Kan :) :) :) \n "
          " \t\t\t\t\t\t\t\t\t" " ➡  Contoh  ketikan KODE [ P ] Untuk Memilih Persegi \n" )

    #input / output
    pilihan = input("                                       " "Masukkan Pilihan Kamu 😁 😉 ☺️  \n\n"
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
        print("                                       "         "Terimakasih Telah  mencoba 🐣 🐣 🐣 ")
        print('-'*800)
        print("\n\n")
        break
    elif confirm == "YES":
        continue
    else:
        print('-' * 800)
        print("                                       " "⚠️\t\t\t\t\t   Upsss.... Input Tidak Valid  Terimakasih Telah  mencoba 🐣 🐣 🐣  ❗❗❗")
        print('-' * 800)
        print("\n\n\n")


