'''
Tarih bilgisi ile birçok işlem yapılabilir, zaman farkı, gün-ay-yıl-saniye,
zamansal sınıflandırma
'''

#import datetime

from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

#import datetime

# result=dir(datetime.time)
# result=dir(datetime.date)

now=datetime.now()
#now=datetime.today()
result=datetime.now()
result=now.year
result=now.month
result=now.day
result=now.hour
result=now.minute
result=now.second

result=datetime.ctime(now)
result=datetime.strftime(now, '%Y')
result=datetime.strftime(now, '%X')
result=datetime.strftime(now, '%d')
result=datetime.strftime(now, '%A')
result=datetime.strftime(now, '%B')
result=datetime.strftime(now, '%Y %B %A')


# t='21 Nisan 2019'
# day, month, year=t.split()
# print(day)
# print(month)
# print(year)

t='15 April 2019 hour 10:12:30'
result=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
result=result.year
# print(result)

birthday=datetime(2002,7,27,18,00)
result=datetime.timestamp(birthday) #saniyeye çevirir
result=datetime.fromtimestamp(result) #tekrar datetime a çevirir
result=datetime.fromtimestamp(0)

result=now-birthday #timedelta

#result=result.days
result=result.seconds

print(birthday)

print()
result=now+timedelta(days=730,minutes=10)
result=now-timedelta(days=10)
print(result)
