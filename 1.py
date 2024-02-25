# python.org dan hata türlerine bakabilirsin

#error handling

#try-except

while True:
  try:
    x=int(input('x: '))
    y=int(input('y: '))
    print(x/y)

  except Exception as ex:
    print("Error: ",ex)

  else:
    print("Correct")
    break
  finally:
    print('try except finished')