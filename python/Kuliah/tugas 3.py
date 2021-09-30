#contoh operator penugasan
R=int(input("Masukan nilai : "))
R%=2
print("Sisa bagi nilai R jika di bagi 2 adalah = ",R)

#operator logika
a=False
b=True
c=a and b
d=a or b
e=not a
print("===================================")
print(a,"and",b,"=",c)
print(a,"or",b,"=",d)
print("not",a,"=",a)
#oprator bitwise
print("#####################")
a=9
b=5
c=a|b
print("nilai : ",a,"binary : ",format(a,"08b"))
print("nilai : ",b,"binary : ",format(b,"08b"))
print("###################################")
print("nilai : ",c,"binary : ",format(c,"08b"))
#oprator identitas
print("+++++++++++++++++")
A=("hp","laptop")
B=("hp","laptop")
print(A is B)
print("true karena objeknya sama")
#0prator keanggotaan
print("==========================")
R=("kipas","baling baling")

print("kipas" not in R)
print("false karena kipas berada di list R")
