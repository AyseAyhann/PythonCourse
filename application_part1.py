# 1
name, surname,gender,id,birthYear,address,age=("Ayse","Ayhan",True,"101058",2002,"Denmark/KOPENHAG",21)
ns=(name+" "+surname)
print("Name: "+ns+" Gender: "+str(gender)+" ID: "+id+" Birth Year: "+str(birthYear)+" Address: "+address+" Age: "+str(age))


# 2
order1=110
order2=1100.5
order3=356.95

sum=order1+order2+order3
print("Total: "+str(sum))


# 3
r_str = input("Enter radius: ")  # Kullanıcıdan bir metin girişi al
r = float(r_str)  # Metin girişini ondalık bir sayıya dönüştür

pi = 3.14

area = pi * r * r  # Dairenin alanını hesapla
circumference = 2 * pi * r  # Dairenin çevresini hesapla

print("Area: " + str(area) + "  Circumference: " + str(circumference))

