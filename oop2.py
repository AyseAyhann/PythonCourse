#Inheritance

class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("Person created.")
    
    def who_am_i(self):
        print("I'm a person")



class Student(Person):  #person sınıfından miras alır
    #pass
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print('Student Created')
    #method overriding
    def who_am_i(self):
        #return super().who_am_i() üst class=super class olur
        print("I'm a student")
    
    def sayHello(self):
        print(f"Hello {self.fname}!")

class Teacher(Person):
        def __init__(self,fname,lname,branch):
            super().__init__(fname,lname)
            self.branch=branch
        def who_am_i(self):
            print("I'm a teacher")

p1=Person('Ayse','Ayhan')
s1=Student('Space','x',123) #Person ın init metodunu da çağırır
t1=Teacher('Marry','West','IT')

print(f"name: {p1.fname}, last name: {p1.lname}")
p1.who_am_i()
print(f"name: {s1.fname}, last name: {s1.lname}, number: {s1.studentNumber}")
s1.who_am_i()
print(f"name: {t1.fname}, last name: {t1.lname}, branch: {t1.branch}")
t1.who_am_i()

