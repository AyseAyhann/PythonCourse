class Person:
    def __init__(self,name,age):
        self.age=age
        if len(name)>8:
            print("Name must be under 8 char.")
        else:
            self.name=name


p=Person("Marianaaa",21)