print("########################################################")
print("                TUGAS PERTEMUAN 4")
nim =  input("Nim Mahasiswa   : ")
nama = input("Nama Mahasiswa  : ")
mata_kul = input("Mata Kuliah     : ")
nilai_a = input("Nilai Absensi   : ")
nilai_t = input ("Nilai Tugas     : ")
nilai_u = input("Nilai UTS       : ")
nilai_s = input("Nilai UAS       : ")
nilai_a = 20/100 * int(nilai_a)
nilai_t = 25/100 * int(nilai_t)
nilai_u = 25/100 * int(nilai_u)
nilai_s = 30/100 * int(nilai_s)
nilai_akhir = nilai_a + nilai_t + nilai_u + nilai_s
print("===================================================")
print("              HASIL LAPORAN")
print("NIM                           = ",nim)
print("Nama                          = ",nama)
print("Mata Kuliah                   = ",mata_kul)
print("Nilai Akhir                   = ",nilai_akhir)
if (nilai_akhir > 81)     and (nilai_akhir < 100):
    print(" GRADE                        =  A ")
    print(" Keterangan                   =  Anda Lulus ")
elif (nilai_akhir >= 75)    and (nilai_akhir < 80 ):
    print(" GRADE                        =   B ")
    print(" Keterangan                   =  Anda Lulus ")
elif int(nilai_akhir >= 60)    and (nilai_akhir < 74):
    print(" GRADE                        =  C ")
    print(" Keterangan                   =  Anda Lulus ")
elif (nilai_akhir >= 41)     and (nilai_akhir < 59):
    print (" GRADE                       =  D ")
    print(" Keterangan                   =  Anda Lulus ")
elif (nilai_akhir >= 0)       and (nilai_akhir < 40 ):
    print(" GRADE                        =  E ")
    print(" Keterangan                   =  Anda Lulus ")
print("              *SELAMAT ANDA LULUS* ")
print("       Tingkatkan Lagi Semangat Belajarnya")