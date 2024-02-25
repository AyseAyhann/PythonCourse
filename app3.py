# #1
# x=int(input("Enter a number: "))
# result= x>0 and x<100
# print(result)

# #2
# x=int(input("Enter a number: "))
# result=(x>0) and (x%2==0)
# print(result)

# #3
# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# z=int(input("Enter a number: "))
# print(f"Max is: {max(x,y,z)}")

# #4
# mid1=int(input("Enter midterm 1: "))
# mid2=int(input("Enter midterm 2: "))
# final=int(input("Enter final note: "))
# note=((mid1+mid2)*0.6)+(final*0.4)

# if((note>=50 and final>=50)or (final>=70)):
#     print("Passed")
# else:
#   print("Failed")

#5
name=input("Name: ")
weight=float(input("Weight: "))
high=float(input("High: "))
result=(weight)/(high**2)
print(f"{name}-index: {result}")
if(result<=18.4 and result>0):
   print("Thin")
elif(result>=18.5 and result<=24.9):
   print("Normal")
elif(result>=25.0 and result<=29.9):
    print("Overweight")
else:
   print("Obese")
  
