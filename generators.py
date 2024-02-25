# generator- bellekte yer kaplamayan iterator tanımlar

# def cube():
#     result=[]
#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())

def cube():
    for i in range(5):
        yield i**3  #liste döndürmez sadece iterable obje döndürür, next kullan
        #bu değere ikinci defa ulaşılamaz,
        #üretildiği an kullanılır, saklanmaz

# generator=cube()
# iterator=iter(generator)
iterator=cube()
for i in iterator:
    print(i)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

def cube():
    for i in range(5):
        yield i**3 

for i in cube():
    print(i)



# mylist=[i**3 for i in range(5)]
# print(mylist)
# for element in mylist:
#     print(element)

generator=(i**3 for i in range(5)) #gelen sonuç generator olur ()
print(generator)

#in while loop
# print(next(generator))
for i in generator:
    print(i)