import re
a = input("Enter the password :")

if(len(a)>=8) :
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',a))==True):
        print("Your password is strong")
    
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',a))==True):
        print("Your password is weak")

else :
    print("You have entered an invalid password.")

