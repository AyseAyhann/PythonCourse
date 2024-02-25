#web3schooldan bakabilirsin
import re
result=dir(re)
#print(result)

# re module

str="Python Kursu: Python Programlama Rehberiniz | 40 saat"

#re.findall()

# result=re.findall("Python",str)
# result=len(result)

# re.split()
result=re.split(" ",str)

#re.sub()
result=re.sub(" ","-",str)


#re.search()
result=re.search("Python",str)
#result=result.span() #konumunu alır
# result=result.start() #başlangıç indexi
# result=result.end()  #bitiş indexi
# result=result.group()
# result=result.string #aranılan stringin hangi patternde olduğu
print(result)


#NOTES
'''
re.findall(" ",str) kullanılır
# []-Köşeli parantezler arasına yazılan bütün karakterler aranır.
# . -Herhangi bir tek karakteri belirtir.
.. -ikili karakterler ab, abc,abcd

# ^ -Belirtilen karakterle başlıyor mu?
# $ -Belirtilen karakterle bitiyor mu?
# * -Bir karakterin sıfır veya daha fazla sayıda olmasını kontrol eder re.findall("sa*t",str)
# + -Bir karakterin bir veya daha fazla sayıda olmasını kontrol eder
# ? -Bir karakterin sıfır ya da bir kez olmasını kontrol eder
# {} -Karakter sayısını kontrol eder  al{2}-l karakteri iki kez tekrarlanmalı
# | -alternatif seçeneklerden birinin gerçekleşmesi gerekir  a|b= a ya da b
# ()- gruplamak için kullanılır (a|b|c)xz--axz ya da bxz
# \ -özel karakterleri aramamızı sağlar  \$a a yı arar
# \A - belirtilen karakter stringin başında mı  \Athe-the strin başında mı
# \Z -belirtilen karakter stringin sonunda mı
# \b -karakter stringin başında mı ya da sonunda mı
#  \d- [0-9] ile aynı işlev, rakamları arar
# \D - [^0-9] ile aynı anlamda, rakam olmayanları arar
# \s boşluk karakterlerini arar
# \S boşluk dışındakiler
# \w -alfabetik karakterler-rakam-alt çizgi
# \W- w nin tersi



'''