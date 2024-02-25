# # "r+" hem okuma hem yazma modunu gösterir
# with open("newFile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# # with open("newFile.txt","r+",encoding="utf-8") as file:
# #     file.write("Trival")

# #istenilen konumda güncelleme
# with open("newFile.txt","r+",encoding="utf-8") as file:
#    file.seek(20) #kürsör 20.karakter konumuna gelir
#    file.write("Trival")
#    print(file.tell())

# with open("newFile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#**********append-sayfa sonunda güncelleme
# with open("newFile.txt","a",encoding="utf-8") as file:
#     file.write("\nİlayda Ayhan")


#**********sayfa başında güncelleme

# with open("newFile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="Ayhan e-Commerce\n"+content
#     #kürsörü başa alır, başa ekleme yapar
#     file.seek(0)
#     file.write(content)
#     print(content)

# with open("newFile.txt","r",encoding="utf-8") as file:
#     print(file.read())

#************sayfa ortasında güncelleme

with open("newFile.txt","r+",encoding="utf-8") as file:
   list=file.readlines()
   #print(list)
   list.insert(2,"\nSena Ayhan") #listeye eklendi, sayfaya da eklenmeli
   file.seek(0)
#    for i in list: #yeni listeyi sayfaya yazdırır
#       file.write(i)
   file.writelines(list)
   
with open("newFile.txt","r",encoding="utf-8") as file:
   print(file.read())

