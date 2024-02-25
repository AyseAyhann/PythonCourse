#ERROR HANDLING

list=["1","2","5a","10b","abc"]

 #1
for x in list:
   if x.isnumeric():  #sayı kontrolü- isnumeric()
      print(x)

#1-2.tip
for x in list:
    try:
        result=int(x)
        print(result)
    except Exception as ex:  #ValueError
        #print("{x} is not numeric.")
        continue

 #2
while True:
   num=(input("Enter a number (or 'q' to quit): "))
   if num.lower()=='q':
         break
   try:
    num=int(num)  #inte çevrilemezse input tipi sayı değildir
   except ValueError:
    print("Input must be a number")


#3
def checkPassword(passw):
    turkish_chars='şçğüıİ'
    #aynı karakterin ikisinde de olmasını kontrol eder
    for p in passw:
     if p in turkish_chars:
            raise TypeError("Password can not include Turkish chars.")
     else:
            pass
    print("Correct password.")
password=input("Enter password: ")
try:
 checkPassword(password)
except Exception as ex:
   print(ex)
   

#5
import math

def calcFactorial(num):
    try:
      num=int(num)  #inte çevrilmezse hata
      return math.factorial(num)
    except Exception as ex:
         print("Error: ",ex) #ValueError

calcFactorial("1q2")
calcFactorial(5)

#fonksiyon içinde raise ile hata göndermek, 
#dışında, fonksiyon çağrısı kısmında try-except kullanmak daha mantıklı

