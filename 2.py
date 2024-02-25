#Raising an Exception
#raise
# x=10

# if x>5:
#     raise Exception(" x can not be higher than 5.")


def check_passord(psw):
    import re  #regex
    if len(psw)<8:
        raise Exception("password must be at least 8 char.")
    elif not re.search("[a-z]",psw):
        raise Exception("Password must include small letter.")
    elif not re.search("[A-Z]",psw):
        raise Exception("Password must include capital letter.")
    elif not re.search("[0-9]",psw):
        raise Exception("Password must include a number.")
    elif not re.search("[_$@]",psw):
        raise Exception("Password must include alpha numeric char.")
    elif re.search("\s",psw):
        raise Exception("Password must not include space char.")
    
password="123456aA_"

try:
    check_passord(password)
except Exception as ex:
    print("Error: ",ex)
else:
    print("Correct")
finally:
    print("Validation completed")