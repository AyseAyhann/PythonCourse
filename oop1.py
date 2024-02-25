#class
#instance (object)

class Person:
    #pass
    #class attributes
    address='no info'
    #constructor
    #nesne oluştururken otomatik çalışır
    def __init__(self,name,year): #self yerine this de olur
      #object attributes
        self.name=name
        self.year=year
        print("init method works")

      #instance methods- parametre olmalı-objelere hizmet eder
    def intro(self):
        print(f"Hello {self.name}!")
        v
      #instance method
    def calcAge(self):
        # return 2023-self.year
        age=2023-self.year
        print(f"Your age is {age}.")


#object(instance)
p1=Person("Ayse",2002)
p2=Person(name="Eli",year=1998)

p1.name="Aysh"
p1.address='Kopenhag'
#accessing attributes
print(f"name: {p1.name}, year: {p1.year}, address: {p1.address}")
print(f"name: {p2.name}, year: {p2.year}, address: {p2.address}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))
p1.intro()
p1.calcAge()
p2.intro()
p2.calcAge()