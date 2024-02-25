# opening and creating file open()
# open(file_name,file_method) #method-read/write vs

# "w": write method, dosyayı oluşturur
#  **Dosyayı konumda oluşturur,
#  **Dosya içeriğini siler ve yeniden ekleme yapar
# file=open("newFile.txt","w")
# #print(file)
# file.close()

# file=open("C:/users/90537/desktop/newFile.txt","w")
# print(file)

# file=open("newFile.txt","w", encoding='utf-8')
# file.write("Ayşe Ayhan")
# file.close()




# "a": append method, dosya konumda yoksa oluşturur
# içeriğin üzerine ekleme yapar
# bir liste döngü ile dosyaya yazdırılabilir
# file=open("newFile.txt","a",encoding='utf-8')
# file.write("\nAyşe Ayhan")
# file.write("\nİlayda Ayhan")
# file.close()

# "x": create method, dosya zaten varsa hata verir  -try except kullan
#file=open("newFile2.txt","x",encoding='utf-8')


# "r": read method, varsayılan, dosya konumda yoksa hata verir


  