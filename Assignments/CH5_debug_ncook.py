#fixing the code below so that it runs without error

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
print(toss)

#fix -> convert toss to string 'heads' or 'tails' from and integer with a simple if statement

if toss == 0:
    toss = 'tails'
else:
    toss = 'heads' 

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')