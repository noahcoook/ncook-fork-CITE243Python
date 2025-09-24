import re

isStrong = False

def passwordVal(passwd):
    global isStrong
    # Assume it's strong at the start
    isStrong = True
    
    if len(passwd) < 8:
        print('min length is 8 characters')
        isStrong = False
    if not re.search(r'\d+', passwd):
        print('min one number')
        isStrong = False
    if not re.search(r'[A-Z]+', passwd):
        print('min one capital letter')
        isStrong = False
    if not re.search(r'[a-z]+', passwd):
        print('min one lowercase letter')
        isStrong = False
 
while isStrong is False:
    password = input('enter a password >\n')
    passwordVal(password)

print("Password accepted!")