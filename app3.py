numbers=[1,3,5,7,9,12,19,21]

# 1
i=0
while (i<len(numbers)):
    print(numbers[i])
    i+=1

# 2
begin=int(input("Num: "))
end=int(input("Num: "))
i=begin
while i< end:
    if(i%2==1):
      print(i)
    i+=1

# 3
i=100
while(i>0):
   print(i)
   i-=1
  

#4
numbers=[]
i=0
while i<5:
   number=int(input("Num: "))
   numbers.append(number)
   i+=1

# 5
products=[]
count=int(input("Enter the number of products: "))
i=0
while i<count:
   name=input("Enter the name of the product: ")
   price=float(input("Enter the price of the product: "))
   products.append({
      'name': name,
      'price':price,
   })
   i+=1
#    products.update={'name':name,
#                     'price':price,
#    }

for product in products:
   print(f'product name: {product["name"]} product price:{product["price"] }')