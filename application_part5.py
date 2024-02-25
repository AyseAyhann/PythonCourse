names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

#1 sona eklemek için append
#names.append('Cenk')


#2 araya eklemek için insert
#names.insert(0,'Sena')

#3
#names.remove('Deniz')
#names.pop(3)
print(names)

#4
print(names.index('Deniz'))

#5
print(bool(names.count('Ali')))
# result='Ali' in names
# result=names.index('Ali')

#6
names.reverse()

#7
names.sort()

#8
years.sort()

#9***
str="Chevrolet, Dacia"
result=str.split(",")
print(result)


#10
min=min(years)
max=max(years)
print(min)
print(max)

#11
print(years.count(1998))

#12
years.clear()
print(years)

#13
brands=[]
brand=input("Brand: ")
brands.append(brand)
brand=input("Brand: ")
brands.append(brand)
brand=input("Brand: ")
brands.append(brand)
print(brands)