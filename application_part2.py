website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1
length=len(course)
print(length)

# 2
print(website[7:10])

# 3
length2=len(website)
print(website[length2-3:length2])

# 4
print(course[0:15])
# print(course[:15])
print(course[length-15:length])
# print(course[-15:-1])
# print(course[-15:])

# 5
# tüm karakterleri normal yazdırır
print(course[::1])
# tüm karakterleri tersten yazdırır
print(course[::-1])

s="12345"*5
print(s)  # 5 kez ifadeyi tekrar eder
print(s[::5]) # her seferinde 5. indexi alır- 1 rakamına denk gelir-başa döner


# 6

name, surname, age, job="Bora","Yılmaz",32, "computer/software engineer"

result=("My name is {} {}, I'm {} years old. I am a {}.".format(name, surname,age,job))
result=(f"My name is {name} {surname}, I'm {age} years old. I am a {job}.")
print(result)

# 7
word="Hello world"
# word[7]='W'
word=word[0:6]+'W'+word[-4:]
word.replace('w','W')
print(word)

# 8
string1="abc"
print(string1*3)
