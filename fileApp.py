# '''
#  DOCSTRİNG: ÖĞRENCİ NOT KAYIT SİSTEMİ UYGULAMASI
#  '''
#TEKRAR
#HATA VAR

# def calculateNote(line):
#    line=line[:-1] #aradaki boşlukları(\n) alır
#    liste1=line.split(':') #isimden sonraki kısmı alır, listeye her elemanı ekler
# #    print(list[0])-isim:
# #    print(list[1])-notlar
# #harf notu da return edebilirsin
#    name=liste1[0]
#    notes=liste1[1].split(',')
#    note1=int(notes[0])
#    note2=int(notes[1])
#    note3=int(notes[2])
#    mean=(note1+note2)*0.4+(note3*0.6)
#    return mean

# def readNotes(): #filename parametresi eklenebilir
#     with open("studentFile.txt","r",encoding="utf-8") as file:
#         # list=file.readlines()
#         # for i in list:
#         #     print(i)
#         for line in file:
#             #print(line)
#             print(calculateNote(line))

# def writeNotes():
#     name=input("Student Name: " )
#     surname=input("Student Surame: " )
#     mid1=int(input("Enter the first midterm note: "))
#     mid2=int(input("Enter the second midterm note: "))
#     final=int(input("Enter the final note: "))

#     with open("studentFile.txt","a",encoding="utf-8") as file:
#      file.write(f"{name} {surname}: {mid1},{mid2},{final}")

# def saveNotes():
#  with open("studentFile.txt","r",encoding="utf-8") as file:
#     liste=[]
#     for i in file:  #satır
#        liste.append(calculateNote(i))
    
#  with open("examResults.txt","w",encoding="utf-8") as file2:
#     for i in liste:
#        file2.write(i)

# while True:
#     op=input("1-Read the Points\n2-Enter the Points\n3-Save the Points\n4-Exit\n")
#     if(int(op)==1):
#        readNotes() #dosya adı burada da verilebilir
#     elif(int(op)==2):
#         writeNotes()
#     elif(int(op)==3):
#         saveNotes()
#     elif(int(op)==4):
#         break
#     else:
#         print("You entered wrong operator, please check again.")
      

'''
DOCSTRING: ÖĞRENCİ NOT KAYIT SİSTEMİ UYGULAMASI
'''

def calculateNote(line):
    line = line[:-1]  # Remove trailing newline
    parts = line.split(':')
    name = parts[0]
    notes = parts[1].split(',')
    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])
    mean = (note1 * 0.4 + note2 * 0.4 + note3 * 0.6)
    return mean

def readNotes():
    with open("studentFile.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculateNote(line))

def writeNotes():
    name = input("Student Name: ")
    surname = input("Student Surname: ")
    mid1 = int(input("Enter the first midterm note: "))
    mid2 = int(input("Enter the second midterm note: "))
    final = int(input("Enter the final note: "))

    with open("studentFile.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {surname}: {mid1},{mid2},{final}\n")

def saveNotes():
    with open("studentFile.txt", "r", encoding="utf-8") as file:
        results = []
        for line in file:
            results.append(calculateNote(line))

    with open("examResults.txt", "w", encoding="utf-8") as file2:
        for result in results:
            file2.write(str(result) + "\n")

while True:
    op = input("1-Read the Points\n2-Enter the Points\n3-Save the Points\n4-Exit\n")
    if op == "1":
        readNotes()
    elif op == "2":
        writeNotes()
    elif op == "3":
        saveNotes()
    elif op == "4":
        break
    else:
        print("You entered the wrong operator, please check again.")
