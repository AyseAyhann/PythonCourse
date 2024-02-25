x,y,z=2,5,10
numbers=1,5,7,10,6
num=input()
num2=input()

#1
result=int((int(num)*int((num2))-(x+y+z)))
print("Result: ",result)

#2
print(y//x)

#3
print((x+y+z)%3)

#4
print(y**x)

#5
# tuple=x,y,z
# tuple=numbers
numbers=1,5,7,10,6
x, *y,z=numbers
print(z**3)

#6
numbers=1,5,7,10,6
x,*y,z=numbers
result=y[0]+y[1]+y[2]
print(result)
# for y in numbers:
#   result+=y
# print(result)
