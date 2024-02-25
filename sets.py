#indekslenemez bir liste
#aynı elemandan yalnızca bir tane olabilir

fruits={'orange','apple','banana'}
#print(fruits[0]) indekslenemez

for x in fruits:
  print(x)

fruits.add('cherry')
fruits.update({'mango','grape','apple'}) 

print(fruits)

myList=[1,2,5,4,4,2,1]
print(myList)
print(set(myList)) #tekrarlı elemanlar gider

fruits.remove('apple')
fruits.discard('mango')

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)