list=[1,2,3]

tuple=(1,'two',3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(tuple))
print(len(list))

list=['Ali','Veli']
tuple=("Deniz","Gizem","Deniz")
names=("Demet","Emel","Ayşe")+tuple
#tuple'ın elemanları atandıktan sonra değiştirilemez, bir listeye eklenebilir
#tuple[0]="Damla"
list[0]='Ahmet'
print(list)
print(tuple)

print(tuple.count("Deniz"))
print(tuple.index("Deniz"))

print(names)

