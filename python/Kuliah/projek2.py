print('===========================================================================')
print("=                          SELAMAT DATANG DI                              =")
print("=                  PROGRAM PERHITUNGAN DASAR MATEMATIKA                   =")
print('===========================================================================')
#pilihan
print('Silahkan Anda Pilih operasi yang ingin anda coba :')
print(" 1.Penjumlahan(+)\n 2.Pengurangan(-)\n 3.Perkalian(x)\n 4.Pembagian(:)\n 5.Sisa bagi\n 6.Pemangkatan")
print("---------------------------------------------------------------------------")
tanya = 'y'
while tanya :
    pilihan = float(input("masukan Operasi yang anda inginkan:"))



#operator

    if pilihan == 1 :
        print("Operasi yang kamu pilih adalah Penjumlahan")
        print("--------------------------------------")
        a = float(input("Masukan Bilangan Ke-1 :"))
        b = float(input("Masukan Bilangan Ke-2 :"))
        c = "penjumlahan"
        sum = a + b

    elif pilihan == 2:
        print("---------------------------------------")
        print("Operasi yang kamu pilih adalah Pengurangan")
        a = float(input("Masukan Bilangan Ke-1 :"))
        b = float(input("Masukan Bilangan Ke-2 :"))
        c = "pengurangan"
        sum = a - b

    elif pilihan == 3:
        print("---------------------------------------")
        print("Operasi yang kamu pilih adalah Perkalian")
        a = float(input("Masukan Bilangan Ke-1 :"))
        b = float(input("Masukan Bilangan Ke-2 :"))
        c = "perkalian"
        sum = a * b

    elif pilihan == 4 :
        print("---------------------------------------")
        print("Operasi yang kamu pilih adalah Pembagian")
        a = float(input("Masukan Bilangan Ke-1 :"))
        b = float(input("Masukan Bilangan Ke-2 :"))
        c = "pembagian"
        sum = a / b

    elif pilihan == 5:
        print("---------------------------------------")
        print("Operasi yang kamu pilih adalah Sisa hasil bagi")
        a = float(input("Masukan Bilangan Ke-1 :"))
        b = float(input("Masukan Bilangan Ke-2 :"))
        c = "sisa hasil bagi"
        sum = a % b

    elif pilihan == 6:
        print("---------------------------------------")
        print("Operasi yang kamu pilih adalah Pemangkatan.")
        a = float(input("Masukan Bilangan Ke-1 :"))
        b = float(input("Masukan Bilangan Ke-2 :"))
        c = "pemangkatan"
        sum = a ** b

    else:
        print("Anda ngaco!!!!")
    print("jadi hasil",c,"dari",a,"dengan",b,"adalah =",sum,"\u2713")
    print("----------------------------------------")
    print("apakah anda ingin mengulang program ini?\nInput (y) untuk lanjut,input (t) untuk berhenti.")
    tanya = input("masukan pilihan kamu: ")
    if tanya == 't':
        break
    elif tanya == 'y':
        continue
    else:
        print("Anda Ngaco!!!!!")


def perhitungandasar():
    print("Program perhitungan")



