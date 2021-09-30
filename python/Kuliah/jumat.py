print("                         PROGRAM HITUNG GAJI KARYAWAN")

nama = input("Nama Karyawan:")
golongan = input("Golongan Jabatan:")
pendidikan = input("Golongan Pendidikan :")
jam = input("Jumlah Jam Kerja:")
tunjangan_jabatan = 0
tunjangan_pendidikan = 0
jam_lembur = 0
honor_lembur = 0
total_gaji = 0
gaji_pokok = 300000
if int(golongan) == 1:
    tunjangan_jabatan = 5/100*300000
elif int(golongan)== 2:
    tunjangan_jabatan = 10/100*300000
elif int(golongan)== 3:
    tunjangan_jabatan = 15/100*300000
print("=====================")
print("Karyawan yang bernama",nama)
print("Honor yang diterima:")
print("Tunjangan jabatan   Rp.",tunjangan_jabatan)
if str(pendidikan) ==  "sma":
    tunjangan_pendidikan = 2.5/100*300000
elif str(pendidikan) == "D1":
    tunjangan_pendidikan = 5/100*300000
elif str(pendidikan) == "D3":
    tunjangan_pendidikan = 20/100*300000
elif str(pendidikan) == "S1":
    tunjangan_pendidikan = 30/100*300000
print("Tunjangan Pendidkan Rp.",tunjangan_pendidikan)
if int(jam) > 8:
    jam_lembur = int(jam) - 8
    honor_lembur = jam_lembur * 3500
else:
    honor_lembur = 0
print("Honor lembur        Rp.",honor_lembur)
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur
print("Total gaji          Rp.",total_gaji)



