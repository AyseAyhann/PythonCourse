names=["Ayse","Karahan","Martin"]

for name in names:
    print(f"My name is: {name}. Spell like:")
    for n in name:
     print(n)


tuple=[(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:
   print(a,b)


dictionary={'k1':1, 'k2':2, 'k3':3}
#for item in dictionary:
#for item in dictionary.items():
for key,item in dictionary.items():
   print(key,item)