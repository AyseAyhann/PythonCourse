#random modülü
import random

details=dir(random)
print(details)

 # document=help(random)
 # print(document)

number=random.randint(1,100)
print(number)

result=random.random()  #0.0-1.0 arası random sayı üretir
result=random.random()*100  #((0.0-1.0)*100) arası random sayı üretir
result=int(random.uniform(10,100))
print(result)

greeting="Hello "
quizNames=['ali','yagmur','deniz','cenk']
name=quizNames[random.randint(0,(len(quizNames)-1))]
result=random.choice(quizNames) #listeden random eleman seçer
#result=greeting+random.choice(quizNames)
result=random.choice(greeting) #string elemanlarından birini seçer-harf seçer
print(name)
print(result)


liste=list(range(1,10))
random.shuffle(liste) #elemanları karıştırır
#listede yapılan değişiklik mutlaka yansır-address
result=liste
print(liste)

liste=range(100)
result=random.sample(liste,3)  #3 rastgele sayı alır
names=random.sample(quizNames,2) #isim listesinden 2 kişiyi getirir
print(result)
print(names)