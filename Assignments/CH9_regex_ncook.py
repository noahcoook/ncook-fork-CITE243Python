import re

password = input('enter a password >\n')

def passwordVal(passwd):
    value = False
    while value is True:
        if len(passwd) < 8:
            print('min length is 8 characters')
            value = 
            #return False
        elif not re.search(r'[0-9]+', passwd):
            print('min one number')
            #return False
        elif not re.search(r'[A-Z]+', passwd):
            print('min one capital letter')
            #return False   
        elif not re.search(r'[a-z]+', passwd):
            print('min one lowercase letter')
            #return False
        return True

passwordVal(password)
