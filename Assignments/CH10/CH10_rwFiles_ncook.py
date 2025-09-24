"""
===========================================================
Program Name: Regex MadLibs
Author: Noah Cook
Date: 9/24/25
Description:
    This program performs Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word
    ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

    It is designed to [specific purpose or goal].
    
Usage:
    Run the script using Python 3.x. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import os, re

adjective = input('please enter a adjective > ')
noun = input('please enter a noun > ')
adverb = input('please enter a adverb > ')
verb = input('please enter a verb > ')

adjectivePattern = re.compile(r'ADJECTIVE')
nounPattern = re.compile(r'NOUN')
adverbPattern = re.compile(r'ADVERB')
verbPattern = re.compile(r'VERB')



