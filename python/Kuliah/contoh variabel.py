print(30*"#")
print("Nama : Qurrota ayun")
print("NIM  : 10200094")
print(30*"-")
list_nim = []
list_uts = []
list_uas = []
list_total = []
list_hasil = []
list_grade = []
prulangan = 2
for i in range(prulangan):
    print("Data ke-1",i+1)
    nim = input("Masukan NIM Anda : ")
    list_nim.append(nim)
    uts = int(input("masukan Nilai UTS : "))
    list_uts.append(uts)
    uas = int(input("Masukan Nilai UAS : "))
    list_uas.append(uas)
    total = (list_uts[i]+list_uas[i])/2
    list_total.append(total)
    if total >= 80 and total <= 100:
        list_grade.append('A')
    elif total >= 70 and total >= 79:
        list_grade.append('B')
    elif total >= 60 and total <=69:
        list_grade.append('C')
    elif total >=45 and total >=53:
        list_grade.append('D')
    elif total < 45:
        list_grade.append('E')

def garis():
    print(50*"-")
garis()
print("NIM", '\t\t',  "Nilai UTS", '\t', "Nilai UAS",'\t', "Total Nilai",'\t', "Grade",'\t', "Nilai Akhir",'\t')
garis()
for i in range(prulangan):
    hasil_akhir = ''
    if list_grade[i] == 'A' or list_grade[i] == 'B':
        hasil_akhir = 'Lulus Memuaskan'
    elif list_grade[i] == 'C':
        hasil_akhir = 'Lulus'
    else:
        hasil_akhir = 'Gagal'

    print(list_nim[i], '\t\t',list_uts[i], '\t\t',list_uas[i], '\t',format(round(list_total[i])), '\t\t',list_grade[i], '\t\t',hasil_akhir)




