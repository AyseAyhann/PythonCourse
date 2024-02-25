# pypi.org dan farklı modül-kütüphanelere erişebilirsin
# pip install package-name

#yöntem 1-import
#math modülü

#import math

# value=dir(math) #modülün fonksiyonları
# value=help(math) #modülün yardım dokümanı
#value=help(math.factorial)
# value=math.sqrt(49)
# value=math.factorial(4)
# value=math.floor(4.6)
# value=math.ceil(4.6)

# import math as calculate

# value=calculate.sqrt(81)


#Yöntem 2- import
#from math import *  #ilgili modüldeki her şey import edilir
from math import factorial,sqrt #bu iki metodu import eder
#aynı isimdeki hangi fonksiyon en son tanımlanırsa onu kabul eder
value=factorial(4)


print(value)

