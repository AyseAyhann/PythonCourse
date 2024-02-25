from unittest import result


def usalma(number):

    def inner(power):
       return number**power   
    
    return inner     

    # two=usalma(2)
    # three=usalma(3)


def yetki_sorgula(page):
    def inner(role):
        if role=="Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner
user1=yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("user"))

#fonksiyon içinde fonksiyonu return eder
def operator(op_name):
        def summation(*args):
            sum=0
            for i in args:
                sum+=i
            return sum
        def multiplication(*args):
            result=1
            for i in args:
                result*=i
            return result
        if op_name=="summation":
            return summation
        if op_name=="multiplication":
            return multiplication


sum=operator("summation")
print(sum(1,2,3,4,5))
mult=operator("multiplication")
print(mult(9,13,21))