import json
#logged out ve exit ekle-tekrar yap
class User:
        pass
        # def __init__(self,username,password,email):
        #     self.username=username
        #     self.password=password
        #     self.email=email

class UserRepository:
        
        def __init__(self):
            self.data=[]
            # self.username=username
            # self.password=password
            # self.email=email

        def savetoFile(self):
         with open("users.json",'a') as file:
            json.dump(self.data,file) #save to file
            
        def register(self):
         uname=input("Your username: ")
         passw=input("Your password: ")
         self.data.append({"name": uname, "password":passw})
         self.savetoFile()

        def login(self):
         uname=input("Your username: ")
         passw=input("Your password: ")

         with open("users.json","r") as file:
            self.data=json.load(file)  #string to dictionary

         for user in self.data:
          if user["name"]==uname and user["password"]==passw:
                print("Login successfully.")
                return
          
        print("Username or password incorrect.")



user=UserRepository()
while True:
    choice=input("What do you want to do? 1 To Register, 2 To Login".center(50,' '))
    if(choice=="1"):
        user.register()
        break
    elif(choice=="2"):
        user.login()
        break
    else:
        print("Wrong operator!") 


   
