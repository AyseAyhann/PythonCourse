#random number generator
#python random
#number prediction game
import random

number=random.randint(1,100)

count=int(input("Enter the number of rights: "))

i=0
counter=0
#her soru 100/count puan
while i<count:
    prediction=int(input("Enter your prediction: "))
    counter+=1
    if(prediction==count):
        print(f"True prediction at {counter}!")
        print("Your point is: ",(100-((counter-1)*(100/count))))
        break
    else:
        if(prediction>count):
            print("Lower")
            
        else:
            print("Higher")
    i+=1
    if(i==count):
        print(f"You failed. The number is: {number}")

