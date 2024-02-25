import os
import datetime

result=dir(os)
result=os.name

#etkin dizin öğrenme
# result=os.getcwd()

#result=os.stat("_datetime.py")
# result=result.st_size/1024
# result=datetime.datetime.fromtimestamp(result.st_ctime) #oluşturulma tarihi
#result=datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi
# result=datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi
# print(result)

#dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

#klasör oluşturma
# os.mkdir("newdirectory")
# os.mkdirs("newdirectory//new")


#listeleme
# result=os.listdir()
# result=os.listdir('C:\\')
# for file in os.listdir():
#     if file.endswith('.py'):
#         print(file)

# os.system("notepad.exe")
#os.rename("newdirectory", "yeniklasör")
#os.removedir("newdirectory") #klasörü sil
# os.removedirs("yeniklasör/yeniklasör")



#path
result=os.path.abspath("os.py")
result=os.path.dirname("C:/Users/90537/Desktop/PYTHON_btk/11python_advanceModulesWebScraping/os.py")
result=os.path.dirname(os.path.abspath("os.py"))
result=os.path.exists("os.py")

result=os.path.isdir("C:/Users/90537/Desktop/PYTHON_btk/11python_advanceModulesWebScraping/os.py")
result=os.path.isfile("C:/Users/90537/Desktop/PYTHON_btk/11python_advanceModulesWebScraping/os.py")

result=os.path.join("C:\\","trival","trival1") #dizin path
result=os.path.split("C:\\deneme")
result=os.path.splitext("os.py")
result=result[0]
print(result)