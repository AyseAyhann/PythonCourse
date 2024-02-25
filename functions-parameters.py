def changeName(n):
    n='ada'
    #return ya da print yok

name="ayse"

changeName(name)
print(name) #ayse - ismi değiştiremez


#listede value typelardan farklı olarak referans kopyalaması yapılır

# def change(n):
#     n[0]='istanbul'

cities=['ankara','izmir']

# change(cities)
# print(cities) #değişim olur- listede referans kopyalaması olur
#fonksiyonsuz, doğrudan atama yapılırsa da değişim olur
#adres kopyalaması istenmiyorsa slicing yapılmalı

n=cities[:] #slicing --value type olarak kopyalar
n[0]='istanbul'
print(cities)
print(n)

#change(cities[:]) yeni bir kopya oluşturur-aynı referans değil

def add(*params):
    print(params)
    print(params[0])
    return sum((params))# *params ile her parametreyi belirtmeye gerek kalmaz
# sum pythonda build-in fonksiyondur
#sum kullanmazsan döngü ile for n in params: sum+=n

print(add(10,40,90))

