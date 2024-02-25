numbers=[1,3,5,7,9,12,19,21]
#1-2-3
result=0
tri=[]
odd=[]
for number in numbers:
    result+=number
    if(number%3==0):
        tri.append(number)
    if(number%2==1):
        number=(number**2)
        odd.append(number)

print(f"Total is: {result}")
print("Triable numbers: ",tri)
print("Odd numbers' square: ",odd)

#4
cities=['kocaeli','istanbul','ankara','izmir','rize']
for city in cities:
    if(len(city)<=5):
        print(city)

#5
products=[
     {'name':'samsung S6','price':'3000'},
     {'name':'samsung S7','price':'4000'},
     {'name':'samsung S8','price':'5000'},
     {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]

# result=0
# for product in products:
#     result+=product('price')
#     if(product('price')<=5000):
#       print(product)

# print("Total price is: {result}")

total=0
for product in products:
    price=int(product['price'])
    total+=price
    if(price<=5000):
        print(product['name'])
print(f"Total price is: {total}")