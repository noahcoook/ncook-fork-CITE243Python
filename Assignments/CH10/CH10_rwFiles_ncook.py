"""
===========================================================
Program Name: Regex MadLibs
Author: Noah Cook
Date: 9/24/25
Description:
    This program performs Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
    ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

    It is designed to take user input for adjectives, nouns, adverbs, and verbs and replace them in madlibs.txt. New file created with new words and outputted on screen.
    
Usage:
    Run the script using Python 3.9. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import os, re, sys
from pathlib import Path
try:
    #opens file, reads content as 'content', if not found then program exits
    with open('Assignments/CH10/madlibs.txt', 'r', encoding='UTF-8') as madlib:
        content = madlib.read()
except FileNotFoundError:
    print('no file found!')
    sys.exit()

#basic asking for input
adjective = input('please enter a adjective > ')
noun = input('please enter a noun > ')
adverb = input('please enter a adverb > ')
verb = input('please enter a verb > ')

#modifying 'content's string, replacing keyword with input
content = re.sub(r'ADJECTIVE', adjective, content)
content = re.sub(r'NOUN', noun, content)
content = re.sub(r'ADVERB', adverb, content)
content = re.sub(r'VERB', verb, content)

#now writing new file as 'content' string
with open('Assignments/CH10/madlibsDone.txt', 'w', encoding='UTF-8') as output:
    output.write(content)

#prints new madlib seperated by lots of dashes
print('\nYour madlib is\n' + '-' * 70 + '\n' + content)






