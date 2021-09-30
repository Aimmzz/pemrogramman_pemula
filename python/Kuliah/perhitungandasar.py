
class perhitungandasar():
    print("Program Perhitungan")

#SAMBUTAN
lanjut = "y"
while lanjut == "y" :
    print(" \t\t\t\t\t\t\t\t\t" '=========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t" ">>                                 SELAMAT DATANG DI                                   <<")
    print(" \t\t\t\t\t\t\t\t\t" ">>                     PROGRAM PERHITUNGAN DASAR MATEMATIKA                            <<")
    print(" \t\t\t\t\t\t\t\t\t" '=========================================================================================')

    #PIIHANAN
    print(" \t\t\t\t\t\t\t\t\t" "📘                  1.Penjumlahan                   4.Pembagian                         📘")
    print(" \t\t\t\t\t\t\t\t\t" "📘                  2.Pengurangan                   5.Modulus                           📘")
    print(" \t\t\t\t\t\t\t\t\t" "📘                  3.Perkalian                     6.Pemangkatan                       📘")
    print(" \t\t\t\t\t\t\t\t\t" '=========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t" "Silahkan kamu Pilih Oerasi apaka yang inin kamu coba ... :-) :-) : \n")
    pilihan = float(input("Masukan Operasi yang kamu inginkan : "))
    print("")
    #OPERATOR

    if pilihan == 1 :
        print(" \t\t\t\t\t\t\t\t\t" "Operasi yang kamu pilih adalah Penjumlahan ")
        print("------------------------------------------")
        a = int(input(" \t\t\t\t\t\t\t\t\t" "Masukan  Bilangan Ke-1 : "))
        b = int(input(" \t\t\t\t\t\t\t\t\t" "Masukan Bilangan  Ke-2 : "))
        sum=a+b

    elif pilihan == 2 :
        print(" \t\t\t\t\t\t\t\t\t" "Operasi yang kamu pilih adalah Pengurangan " )
        print(" \t\t\t\t\t\t\t\t\t" "------------------------------------------")
        a = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan  Bilangan Ke-1 : "))
        b = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan Bilangan  Ke-2 : "))
        sum = a - b

    elif pilihan == 3 :
        a = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan  Bilangan Ke-1 : "))
        b = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan Bilangan  Ke-2 : "))
        sum = a * b
        print(" \t\t\t\t\t\t\t\t\t" "------------------------------------------")

    elif pilihan == 4 :
        print(" \t\t\t\t\t\t\t\t\t" "Operasi yang kamu pilih adalah Pembagian " )
        print("------------------------------------------")
        a = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan  Bilangan Ke-1 : "))
        b = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan Bilangan  Ke-2 : "))
        sum = a / b
    elif pilihan == 5 :
        print(" \t\t\t\t\t\t\t\t\t" "Operasi yang kamu pilih adalah Modulus " )
        print("------------------------------------------")
        a = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan  Bilangan Ke-1 : "))
        b = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan Bilangan  Ke-2 : "))
        sum = a % b
    elif pilihan == 6 :
        print(" \t\t\t\t\t\t\t\t\t" "Operasi yang kamu pilih adalah Pemangkatan " )
        print("------------------------------------------")
        a = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan  Bilangan Ke-1 : "))
        b = float(input(" \t\t\t\t\t\t\t\t\t" "Masukan Bilangan  Ke-2 : "))
        sum = a ** b
    else:
        print(" \t\t\t\t\t\t\t\t\t" "Ups Sorry !!! , Piihan kamu tidak terdaftar pada Program \n")
    print("\n")
    print(" \t\t\t\t\t\t\t\t\t" '     HASIL OPREASI YANG KAMU PILIH ADALAH     ')
    print(" \t\t\t\t\t\t\t\t\t" "==============================================")
    print(" \t\t\t\t\t\t\t\t\t" "=    >>  ",sum,"  <<")
    print(" \t\t\t\t\t\t\t\t\t" "    ----------------")
    print('\n\n\n')

    lanjut = input("Masukan (y) lanjut,(t) berhenti :")
    if lanjut == "y":
        continue
    elif lanjut == "t":
        print(" APAKAH KAMU MAU MENGEULANG PROGRAM MATEMATIKA DASAR LAGI \n"
              " JIKA INGIN MENGULANG LAGI KETIKAN [ y ] TAPI JIKA TIDAK KETIKAN [  ]\n"
              " ____________________________________________________________________")
        lanjut = input(" Masukan Pilihanmu [ y OR t ] : ")
        print('\n\n')
        if lanjut == 'y':
            import mainmenu as ac
            ac.pilihan

        elif lanjut == "t":
            print("----------------  TER5IMAKASIH ------------------")

    else:
        print("\t\t\t\t\t\t\t\t-------------- BAKA ----------------")



#tanya = 'y'
#while tanya :
    #print("Hey .... Apakah Kamu Ingin Mengulangi Program ini \n Jika Ya Silahkan Kamu Ketikan [y] \n Jika Tidak ingin Menulang Program maka Ketika [t] \n" )
    #tanya = input("Masukan Piihan Kamu : ")

















