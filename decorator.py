'''
 bir fonksiyonun öncesinde veya sonrasında 
 belirli işlemler yapmak istenildiğinde,
 dekoratörler kullanılabilir
'''

def my_decorator(func):  # func bir fonksiyon
    def wrapper(name):  #sayHello name parametresi
        print("before the func.")
        func(name)  #sayHello ya da parametre olarak gönderilen fonksiyon çağırılır
        print("after the func.")
    return wrapper

@my_decorator
def sayHello(name):
    print("hello ",name)

 
# def sayGreeting():
#     print("greeting")

#sayHello=my_decorator(sayHello)
# sayGreeting=my_decorator(sayGreeting)
sayHello("Ayse")
# sayGreeting()

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print("fonksiyon: "+func.__name__+str(finish-start)+" saniye sürdü.")
    return inner

@calculate_time  #decorator--kod tekrarının önüne geçilir
def usalma(a,b):
    # start=time.time()
    # time.sleep(1)
    print(math.pow(a,b))
    # finish=time.time()
    # print("func "+str(finish-start)+" seconds")
    
@calculate_time
def faktoriyel(num):
    # start=time.time()
    # time.sleep(1)
    print(math.factorial(num))
    # finish=time.time()
    # print("func "+str(finish-start)+" seconds")

usalma(2,4)
faktoriyel(5)