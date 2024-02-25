import module
import math
#oluşturulan modülü python klasöründe lib'in içine atarsan
#  standart modül olarak kullanabilirsin

document=help(module)
print(document)

details=dir(module)
print(details)

func=help(module.func)
print(func)

num=module.number
numbers=module.numbers
name=module.person["name"]
print(num)
print(numbers)
print(name)

result=module.func(20)
print(result)

p=module.Person()
p.speak()