
#mainmenu
def menu () :
    print(" \t\t\t\t\t\t\t\t\t" '========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t""=                               HELLO GUYS WEOLCOME TO                                  =")
    print(" \t\t\t\t\t\t\t\t\t""=                       PROGRAM PEMBELAJARAN DASAR MATEMATIKA                           =")
    print(" \t\t\t\t\t\t\t\t\t" '========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t" 'Ketentuan Penggunaan Program :')
    print(" \t\t\t\t\t\t\t\t\t" '========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t" '>>  ketikan angka A jika anda ingin memilih program matematika dasar                   <<')
    print(" \t\t\t\t\t\t\t\t\t" '>>  ketikan angka B jika anda ingin memilih program mencari perhitungan bangun datar   <<')
    print(" \t\t\t\t\t\t\t\t\t" '>>  ketikan angka C jika anda ingin EXIT                                              <<')
    print(" \t\t\t\t\t\t\t\t\t"'=========================================================================================')
    print('\n\n')

menu()
def ulang():
    print()
konfir="Y"
while konfir :

    print(" \t\t\t\t\t\t\t\t\t" "MAIN MENU PROGRAM MATEMATIKA DASAR")
    print(" \t\t\t\t\t\t\t\t\t" '========================================')
    print(" \t\t\t\t\t\t\t\t\t" ">>  PILIHAN PROGRAM MATEMATIKA DASAR   <<")
    print(" \t\t\t\t\t\t\t\t\t" '========================================')
    print(" \t\t\t\t\t\t\t\t\t" 'A. Program Perhitungan Matematika Dasar')
    print(" \t\t\t\t\t\t\t\t\t" 'B. program Perhitungan Bangun Datar')
    print(" \t\t\t\t\t\t\t\t\t" 'C. exit program')
    print(" \t\t\t\t\t\t\t\t\t" '========================================')

    pilihan = input(" \t\t\t\t\t\t\t\t\t" "Masukan Program Yang Kamu Inginkan  : ")
    if pilihan == 'A' :
        import perhitungandasar as pd
        pd.perhitungandasar

    elif pilihan == 'B' :
        import bangundatar as bd
        bd.rumusbangundatar

    elif pilihan == 'C' :
        exit()

    print("\n\n")
    print( " APAKAH KAMU MAU MENGULANG PROGRAM MATEMATIKA DASAR LAGI \n"
           " JIKA INGIN MENGULANG LAGI KETIKAN [ Y ] TAPI JIKA TIDAK KETIKAN [ T ]\n"
           " ____________________________________________________________________")
    X = input(" Masukan Pilihanmu [ Y OR T ] : ")
    print('\n\n')
    if X=='Y' :
        import bangundatar as bd
        bd.rumusbangundatar

    else:
        exit()






























