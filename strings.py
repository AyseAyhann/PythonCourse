name="Ayse"
surname="Ayhan"
age=21

# greeting=("Hello!"+"\nName: "+name+" Surname: "+surname+"\nAge: "+str(age))
# print(greeting)
# print(greeting[0])
# print(greeting[1])
# print(greeting[2])
# print(greeting[3])
# print(greeting[4])

# print(len(greeting))
# print(greeting[(len(greeting)-1)])
# length=len(greeting)
# print(greeting[length-1])
# print(greeting[-1])

# print(greeting[2:5])
# print(greeting[3:])
# print(greeting[:15])

# print(greeting[2:40:2])

#string format
# print("My name is {} {}, I am {} years old.".format(name, surname, str(age)))
# print("My name is {0} {1}, I am {2} years old.".format(name, surname, str(age)))
print("My name is {s} {n}, I am {a} years old.".format(n=name, s=surname, a=str(age)))

# result=200/500
# print("the result is {r:1.3}".format(r=result))

# format with f string
print(f"My name is {name} {surname} and I'm {age} years old.")
