#fixing the code below so that it runs without error

import random, sys
guess = ''
while guess not in ('heads', 'tails'):
    try:        #clean ending via ctrl + c
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    except KeyboardInterrupt:
        print('Ending now')
        sys.exit()
        
toss = random.randint(0, 1) # 0 is tails, 1 is heads

#fix -> convert toss to string 'heads' or 'tails' from and integer with a simple if statement
try:
    if toss == 0:
        toss = 'tails'
    else:
        toss = 'heads' 

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        while guess not in ('heads', 'tails'): #same while loop in first part used to stop wrong guesses from propagating further
            print('Enter heads or tails')
            guess = input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
except KeyboardInterrupt:
        print('Ending now')
        sys.exit()