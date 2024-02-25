# lists

# 1
myList=["Bmw","Mercedes","Opel","Mazda"]

# 2
length=myList.__len__()
print(length)

# 3
first=myList[0]
print(first)

last=myList[length-1]
print(last)

# 4
indexof=myList.index("Mazda")
myList[indexof]="Toyota"
print(myList)

# 5
print(bool(myList.index("Mercedes")))

# 6
print(myList[-2])

# 7
print(myList[0:3])

# 8
myList[-2]="Toyota"
myList[-1]="Renault"
print(myList)

# 9
myList.append("Audi")
myList.append("Nissan")
print(myList)

# 10
myList.pop()  #sondan siler  
print(myList)

# 11
myList2=myList.reverse()
print(myList2)


# 12
studentA=["Yigit Bilgi",2010,(70,60,70)]
studentB=["Sena Turan",1999,(80,80,70)]
studentC=["Ayse Ayhan",2002,(90,100,100)]
studentList=[studentA]+[studentB]+[studentC]
print(studentList)