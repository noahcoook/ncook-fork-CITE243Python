#password length checker/mini login
username = input('Enter a username>')
password = input('Enter your strong password>')

if len(password) <= 5: #checks if password is less than or equal to 5 characters
	print('Password is too short')
	exit()
elif len(password) >= 15: #checks if password is greater than or equal to 15 characters
	print ('Password is too long')
	exit()
else:
	print ('Password is accepted') #if password is between 6 and 14 characters, it is accepted

#now login
check_user = input('Username: ') #variable check_user is used to check if inputted username is equal to username created previously
if check_user == username:
	print('Success, now enter password')
else:
	print('No user with that name')
	exit()

check_pass = input('Password: ') #variable check_pass is used to check if inputted password is equal to password created previously
if check_pass == password:
	print('Success, now you\'re logged in!')
else:
	print('Wrong password, try again')
	exit()
