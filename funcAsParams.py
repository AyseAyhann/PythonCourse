def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi): #func1, fun2,func3 ..f1=toplama() oldu, parametreye göre
    if islem_adi=="toplama":
        print(f1(2,3))   # toplama(2,3)--f1=toplama, parametreye bağlı
    elif islem_adi=="cikarma":
        print(f2(5,3))
    elif(islem_adi=="carpma"):
        print(f3(3,4))
    elif(islem_adi=="bolme"):
        print(f4(10,2))
    else:
        print("geçersiz işlem...")

islem(toplama, cikarma, carpma, bolme,"toplama")  #toplama=f1, cikarma=f2
islem(toplama, cikarma, carpma, bolme,"cikarma") #fonksiyonları parametre olarak gönderir
islem(toplama, cikarma, carpma, bolme,"carpma")
islem(toplama, cikarma, carpma, bolme,"bolme")