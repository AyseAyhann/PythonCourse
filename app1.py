#1
word=input("Word: ")
times=int(input("How many times: "))

def printWord(str,count):
    i=0
    while i<count:
        print(str)
        i+=1

    #print(str*count) da olur

printWord(word,times)


# #2

def toList(*params):
    list=[]
    for param in params:
        list.append(param)
    return list 

result=(toList(5,"aysh","1234",3.7,))
print(result)


#3
def findPrimes(a,b):
    for x in range(a,b+1):
      if x>2:
            for i in range(2,x):
                if(x%i==0):
                    break
            else:
                print(x)
 
print(findPrimes(2,20))    
        

#4
def findDivisor(num):
    divisorList=[]
    i=0
    while i<num:
        i+=1
        if(num%i==0):
            divisorList.append(i)
    return divisorList

print(findDivisor(216))