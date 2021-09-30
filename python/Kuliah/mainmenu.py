class mainmenu():
    print()
#mainmenu

def menu () :
    print(" \t\t\t\t\t\t\t\t\t" '========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t""=                               HELLO GUYS WEOLCOME TO                                  =")
    print(" \t\t\t\t\t\t\t\t\t""=                       PROGRAM PEMBELAJARAN DASAR MATEMATIKA                           =")
    print(" \t\t\t\t\t\t\t\t\t" '========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t" 'Ketentuan Penggunaan Program :')
    print(" \t\t\t\t\t\t\t\t\t" '========================================================================================')
    print(" \t\t\t\t\t\t\t\t\t" '>>  ketikan angka A jika anda ingin memilih program matematka dasar                   <<')
    print(" \t\t\t\t\t\t\t\t\t" '>>  ketikan angka B jika anda ingin memilih program mencari perhitungan bangun data   <<')
    print(" \t\t\t\t\t\t\t\t\t" '>>  ketikan angka C jika anda ingin EXIT                                              <<')
    print(" \t\t\t\t\t\t\t\t\t"'=========================================================================================')
    print('\n\n')


menu()
def pilihan () :
    print()
while True :
    print(" \t\t\t\t\t\t\t\t\t" "MAIN MENU PROGRAM MATEMATIKA DASAR")
    print(" \t\t\t\t\t\t\t\t\t" '========================================')
    print(" \t\t\t\t\t\t\t\t\t" ">>  PILIHAN PROGRAM MATEMATIKA DASAR   <<")
    print(" \t\t\t\t\t\t\t\t\t" '========================================')
    print(" \t\t\t\t\t\t\t\t\t" 'A. Program Perhitungan Matematika Dasar')
    print(" \t\t\t\t\t\t\t\t\t" 'B. program Perhitungan Bangun Datar')
    print(" \t\t\t\t\t\t\t\t\t" 'C. exit program')
    print(" \t\t\t\t\t\t\t\t\t" '========================================')
    pilihan = input(" \t\t\t\t\t\t\t\t\t" "Masukan Program Yang Kamu Inginkan  : ")


    if pilihan == 'B' :
        import bangundatar as bd
        bd.rumusbangundatar
    elif pilihan == 'A':
        import perhitungandasar as pd
        pd.perhitungandasar
    elif pilihan == 'C' :
        print(" TERIMAKASIH ")
    else :
        print("coba anda baca keterangan di atas")
    break


























