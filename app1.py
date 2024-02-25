
# #1
# age=int(input("Age: "))
# education=input("Education: ")

# if(age>=18 and ((education=="college") or (education=="university"))):
#     print("You can have a driver lisence.")
# else:
#     print("You can not have a driver lisence.")

# #2
# mid1=int(input("Enter the first exam note: "))
# mid2=int(input("Enter the second exam note: "))
# note=(mid1+mid2)/2

# if(note>0 and note<=24):
#     print("0")
# elif(note<=44):
#     print("1")
# elif(note<=54):
#     print("2")
# elif(note<=69):
#     print("3")
# elif(note<84):
#     print("4")
# else:
#     print("5")

#else-incorrect info

# #3
# from datetime import datetime

# user_date_str=input("Enter the date (YYYY-MM-DD): ")
# # strptime stringi tarihe çevirir
# user_date=datetime.strptime(user_date_str, "%Y-%m-%d")

# current_date=datetime.now().date()
# # hata: date_difference=current_date-user_date.date()
# #güne çevrilmeli
# date_difference=(current_date-user_date.date()).days

# if(date_difference>=365 and date_difference<365*2):
#     print("1. year")
# elif(date_difference>=365*2 and date_difference<365*3):
#     print("2.year")
# elif(date_difference>=365*3 and date_difference<=365*4):
#     print("3.year")


import datetime

user_date_str = input("Enter the date (YYYY/M/D): ")
user_date = user_date_str.split('/')
print(user_date)

# You need to convert the date components to integers
year = int(user_date[0])
month = int(user_date[1])
day = int(user_date[2])

begin = datetime.datetime(year, month, day)
current_date = datetime.datetime.now()
date_difference = current_date - begin

# You need to access the days attribute to get the difference in days
days = date_difference.days

if days >= 365 and days < 365 * 2:
    print("1. year")
elif days >= 365 * 2 and days < 365 * 3:
    print("2. year")
elif days >= 365 * 3 and days <= 365 * 4:
    print("3. year")
