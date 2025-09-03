#countdown timer with sys module
from calendar import c
import sys

starting_number = int(input("Enter a starting number for the countdown: ")) #

while starting_number > -1:
    print('Youre on number ', str(starting_number), '.')
    starting_number = starting_number - 1
    if starting_number == 0:
        print('Youve reached the end!')
        sys.exit()

    

