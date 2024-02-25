# function- dictionary-different type of values

# dicionary için iki yıldız **args
# liste için *params

def displayUser(**args):
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name="Ayse", age=21, email="ayse.ayhan@gmail.com", phone="1234")
displayUser(name= "Ege",age=27,city="ankara")

def myfunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50,key1='value', key2='value2')