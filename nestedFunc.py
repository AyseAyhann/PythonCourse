# fonksiyonlar objelerdir

def greeting(name):
    print('hello',name)

# greeting("Ayse")
# print(greeting)

sayHello=greeting #obje atama-aynı adresi gösterir, biri silinirse diğeri kullanılabilir

# print(sayHello)
# print(greeting)
# print(greeting("Aysh"))
# print(sayHello("Aysh"))

del sayHello
print(greeting)
#print(sayHello) -not defined





# encapsulation
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1+1
    num2=inner_increment(num1)
    print(num1, num2)

outer(10)
# inner_increment(10) çalışmaz, outer kapsamında




def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number>=0:
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if number<=1:
            return 1
        return number*inner_factorial(number-1) #1'e inene kadar 1 eksiğiyle çarpar
    return inner_factorial(number)
try:
    print(factorial(-8))
except Exception as ex:
    print(ex)
print(factorial(5))