#lambda expressions, map and filter

square=lambda num: num**2
numbers=[1,3,5,9]
# result=list(map(lambda num: num**2, numbers))
#result=list(map(square,numbers))
result=square(3)
print(result)



root=lambda num: num**(1/2)
result=root(9)
print(result)