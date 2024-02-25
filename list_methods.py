numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']

val=min(numbers)  #min rakamı alır
print(val)

val=max(numbers)
print(val)

val=min(letters)  #ilk harfi alır-a
print(val)

val=max(letters)   #-y
print(val)


val=numbers[3:6]
print(val)

numbers[3]=20
numbers.append(11)
numbers.insert(3,78)
numbers.insert(-1,52) #sona ekler
numbers.pop(0)  #indexe göre siler
numbers.pop(-1)
numbers.remove(5)  # listedeki 5 sayısını siler


numbers.sort() #sayılar sıralanır
numbers.reverse()

letters.sort() #alfabetik olarak sıralanır
letters.reverse()
print(numbers)

print(len(letters))

print(numbers.count(10))
print(letters.count('a'))

numbers.clear()
print(numbers)