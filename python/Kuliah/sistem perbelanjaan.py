nilai = input("Nilai anda : ")
if nilai >= str(90):
    grade = "A"
elif nilai >= str(85):
    grade ="B+"
elif nilai >= str(80):
    grade = "B"
elif nilai >= str(75):
    grade = "C"
else:
    grade = "d"
print("Grade : " + grade)