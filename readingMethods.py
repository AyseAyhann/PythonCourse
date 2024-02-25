with open("newFile.txt","r",encoding='utf-8') as file:
    #file.close() a gerek kalmaz with ile
    content=file.read(10)
    print(content)
    file.seek(0) #kürsörü istenilen konuma getirir
    print(file.tell()) #kürsörün konumunu verir
    content2=file.read()
    print(content2)
