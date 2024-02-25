# and or not(a==b) operatörleri kullanılır

# #1
# x=input()
# y=input()
# print("Max: ",max(x,y))
# #or
# if((x>y)and(y!=x)):
#     print("y max")
# else:
#     print("x max")


# #2
# mid1=int(input("Enter midterm 1: "))
# mid2=int(input("Enter midterm 2: "))
# final=int(input("Enter final note: "))
# note=(mid1+mid2+final)/3

# if(note>=50):
#     print("Passed")
# else:
#     print("Failed")

#bool ile de yapılabilir

# #3
# x=int(input("Enter a number: "))
# if(x%2==0):
#     print(f"{x} is even")
# else:
#     print(f'{x} is odd')


# #4
# x=int(input("Enter a number: "))
# if(x>0):
#     print("Positive")
# else:
#     print("Negative")

email=input("Enter email: ")
#ayse.ayhan6777@gmail.com
password=input("Enter password: ")
#2007

#strip ile stringleri boşluksuz al

if(email=="ayse.ayhan6777@gmail.com" and password=="2007"):
    print("Correct")
else:
    print("Error")
