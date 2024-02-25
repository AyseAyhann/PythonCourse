# prime number check

number=int(input("Enter a number: "))
i=2

if(number==2 or number==1):
    print("It's prime.")

else:
  while i<number:
     if(number%i==0):
        print("Not prime.")
        break
     else:
        print("It's prime.")
        break
  i+=1
     
     

#random number prime
import random

number=random.randint(1,100)
i=2
while(i<number):
   if(number%i==0):
        print(f"{number} is not prime.")
        break  #bir adet bulunması yeterli
   else:
        print(f"{number} is prime")
        break
i+=1
