# string
website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1
word=" Hello World "
word=word.strip()
# word=word.lstrip()  #soldan boşluk silme
# word=word.lstrip()  #sağdan boşluk silme
# word=word.lstrip('/:pth')  #soldan siler
print(word)

# 2
indis=website.find("sadikturan")
website=website[indis:indis+10]
#website=website.strip('w.moc')  #doğrudan silinebilir, globalda değişmemesi için website yerine yeni değişkene ata
print(website)

# 3
course=course.lower()
print(course)

website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 4
print(website.count('a'))

# 5
print(website.endswith('.com'))
print(website.startswith('www'))

# 6
print(bool(website.find(".com")))  #normalde index döndürür
print(website.find('com',0,10)) # belirli aralıkta arama yapar
print(website.index('com'))
# rfind-sağdan aramaya başlar

# 7
print(course.isalpha())
print(course.isdigit())

# 8
message="Contents"
message=message.center(50,'*')
#message=message.ljust(50,'*')
#message=message.rjust(50,'*')
print(message)

# 9
course=course.replace(" ","*")
#course=course.replace(" ","*",5) #sadece 5 karakteri değiştirir
print(course)

# 10
message="Hello World"
message=message.replace("World","There")
print(message)

# 11
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#sürekli tanımlamamak için temp değişkenler üzerinde değişiklik yap
result=course.split(" ")  #her bir kelimeyi bir karakter olarak algılar
#result=result[2]  #dizi
print(result)

