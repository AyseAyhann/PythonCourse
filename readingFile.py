# try:
#  file=open("newFile.txt","r")
#  print(file)
# except Exception as ex:  #FileNotFoundError
#  print("Reading file error!")
# finally:
#  print("File closed.")
#  file.close()
 

file=open("newFile.txt","r",encoding='utf-8')

# ******************#FOR loop ile okumak
# for i in file:
#     print(i,end="") #satır boşluğu bırakmaz


# *******************#read() fonksiyonu ile okumak
# content1=file.read()
# print("\ncontent 1")
# print(content1)

# content2=file.read()  
# #imleç kaldığı yerden devam eder, son okunulan yerden
# print("content 2")
# print(content2)


# content=file.read(5)  #ilk 5 karakteri okur
# content=file.read(3)  # ilk 5 karakterden sonraki 3 karakteri okur


#******************readline() fonksiyonu, her seferinde bir satır okur

#print(file.readline(),end="")


#******************readlines() fonksiyonu
liste=file.readlines()  #bilgilere tek tek ulaşılabilir
print(liste)
print(liste[0])
print(liste[0][0])  #örneğin boşluğa kadar olan stringleri de
#ayrı bir listede tutulabilir, ad soyad şeklinde 
file.close()


