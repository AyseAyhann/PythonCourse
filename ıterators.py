# #for döngüsü otomatik iterator oluşturur

# liste=[1,2,3,4,5]
# iterator=iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# for i in liste:
#     print(i)

# iterator=iter(liste)
# while True:
#     try:
#         element=next(iterator)
#         print(element)
#     except Exception as ex:  #StopIteration
#         break

class Mynumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.stop:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration


list=Mynumbers(10,20)
iterator=iter(list)
# print(next(iterator))

while True:
    try:
        element=next(iterator)
        print(element)
    except Exception as ex:
        break


# for i in list:
#     print(i)



