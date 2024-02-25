# method
#
#
list=[1,2,3]
list.append(4)  #method
list.pop()
print(type(list)) 
print(list)


myString='Hello'
print(myString.upper())
print(type(myString))

#
#
# function
name=input("Your name: ")
def sayHello(str='user'):  
     #default değer atarsan 
     #fonksiyon çağrısında parametre göndermesen de olur
   
    return 'Hello'+name
    #print(f"Hello {str}!")
    #print("Hello"+name)
 
msg=sayHello("Aysh")
print(msg)

sayHello(name)
sayHello()


def total(num1, num2):
    return num1+num2

#fonksiyon değer return ettiği için yazdırmak için print edilmeli
result= total(10,20)
print(result)

date=int(input("Your birth year: "))
def calculateAge(year=1999):
    return 2023-year

result=calculateAge(date)
print(f"Your age:{result}")


def Emeklilik(birthYear=1999, name='user'):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: year of birth
    OUTPUT: hesaplanan yıl bilgisi
    
    '''
    age=calculateAge(birthYear)
    emeklilik=65-age
    if(emeklilik>0):
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Emeklisiniz.")

Emeklilik(2002,"Ayse")
print(help(Emeklilik))  #fonksiyon docstring bilgisini yazdırır ''' '''


list=[1,2,3]
print(help(list.append)) # method parantezi kullanılmaz()