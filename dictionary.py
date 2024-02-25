# key-value
# 41-Kocaeli

cities=["kocaeli","istanbul"]
plakalar=[41,34]

print(plakalar[cities.index("istanbul")])  #dictionary kullanmadan

#print(plakalar['kocaeli']) => 41

plakalar={'kocaeli':41, 'istanbul':34}

print(plakalar['kocaeli'])

plakalar['ankara']=6
plakalar['kocaeli']='new value'
print(plakalar)


users={
    'ayseayhan':{
        'age':21,
        'roles':['admin','user'],
        'email':'ayse.ayhan6777@gmail.com',
        'address':'BURSA',
        'phone':'1231321'
    },
    'ilaydaayhan':{
        'age':24,
        'roles':['admin','user'],
        'email':'ilayda@gmail.com',
        'address':'BURSA',
        'phone':'1231320'
    }
}
print(users['ilaydaayhan']['age'])
print(users['ilaydaayhan']['roles'])
print(users['ayseayhan']['address'])


