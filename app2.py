# Bank App
#ek hesap kullanımını da talebe bağlı yapabilirsin
# if balance < money: 
AyseAccount={
    'name':"Ayse Ayhan",
    'accountNum':"134200",
    'balance':1000000000,
    'additional':5000000
}

UzayAccount={
    'name':"Uzay X",
    'accountNum':"001342",
    'balance':3000,
    'additional':2000
}

ElijahAccount={
    'name':"Eli X",
    'accountNum':"981342",
    'balance':1000,
    'additional':500
}


def withdrawMoney(account):
    money=int(input(f"How much you want {account['name']}?: "))
    if(money<account['balance'] or money==account['balance']):
        account['balance']-=money
        print(f"Your balance is: {account['balance']}.")
    else:
        #ek hesap kullanılsın mı sorusuna bağlı yapabilirsin
        if(account['balance']+account['additional']>=money):
            money-=account['balance']
            account['balance']=0
            account['additional']-=money
            if(account['additional']==0):
                print("Your balance is 0.")
            else:
                print(f"Your additional balance is: {account['additional']}.")
        else:
            print(f"Insufficient funds {account['accountNum']}, your balance is {account['balance']+account['additional']}!")


#withdrawMoney(AyseAccount)
#ek hesap-tarih tutulabilir, faiz kullanılabilir
withdrawMoney(ElijahAccount)
    
