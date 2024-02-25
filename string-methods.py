message=" Hello There. My name is Ayse Ayhan"
# message=message.upper()
# message=message.lower()
# message=message.title() # baş harfleri büyük yapar
# message=message.capitalize() # ilk harf büyük
# message=message.strip() # boşlukları almaz
# message=message.split()# her bir kelimeyi ayırır
# message=message.split(" ") # kelimeleri boşlıklardan ayırır
# message=message.split(".") # kelimeleri noktalardan ayırır
# message=' '.join(message) # eski haline döner, birleştirir, araya boşluk ekler
# message='*'.join(message) # araya * ekleyerek birleştirir

index=message.find('Ayse')
print(index)
isFound=message.startswith('B')
print(isFound)
isFound=message.endswith("n")
print(isFound)
print(message)

message=message.replace('Ayse','Karahan')
print(message)
message=message.replace(" ","*").replace("o","w")
print(message)

# message=message.center(100) #place holder-container oluşturur
message=message.center(50,'*')
print(message)