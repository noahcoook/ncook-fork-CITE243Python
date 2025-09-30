"""
===========================================================
Program Name: CopyPDF
Author: Noah Cook
Date: 9/29/2025
Description:
    This program will look through every file in the users Downloads folder. 
    It will then check if it ends with a .pdf extension, if there is any, they will get copied into the pdfDocs folder on users DESKTOP
    It is designed to copy any pdf file into a new folder on the DESKTOP.

Usage:
    Run the script using Python 3.9. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import shutil, os, re, sys
from pathlib import Path


#gets home path of user so we can look in Downloads folder
h = Path.home()

#folder to pull pdfs from, can change if no pdfs in Downloads, just make sure path is in your user folder
sourceFolder = Path(h / 'Downloads')

#folder to send pdf copies too
destFolder = Path(h / 'Desktop/pdfDocs')

#makes destFolder if not already there
os.makedirs(destFolder, exist_ok=True)

#lists out files in sourceFolder so for loop can iterate through them
filesList = os.listdir(sourceFolder)

#regex pattern, doesnt need to be regex neccesarily but I like it. Could easily use endswith() method
pattern = (r'\.pdf$')

#loops through all files in sourceFolder
for files in filesList:
    if re.search(pattern, files):
    #if pattern matches files, then build paths
        sourcePath = os.path.join(sourceFolder, files)
        #builds full path so shutil can copy. Joins destination with filename to create proper path
        destPath = os.path.join(destFolder, files)
        shutil.copy(sourcePath, destPath)

print(f'\nYour pdf files have been copied!\nThey are in {destFolder}!\n')


#lists out list of newly copied files in a numbered print out
count = 0
print('Copied PDF\'s listed below:\n')
for pdf in os.listdir(destFolder):
    count += 1
    print(f'{count}: {pdf}')


#added this delete prompt to make it easy to remove from desktop
try:
    while True:
        userDelete = input(u'Would you like to delete newly generated folder? y or n \u2193 \n')
        if userDelete == 'y' or userDelete == 'Y':
            for pdf in os.listdir(destFolder):
                delete = os.path.join(destFolder, pdf)
                os.unlink(delete)
            print('\nDeleted!\n')
            break
        elif userDelete == 'n' or userDelete == 'N':
            print('\nNot deleted!\n')
            break
        else:
            print('\nPlease enter either y OR n\n')
            continue
except KeyboardInterrupt:
    print('\nPROGRAM EXITING\n')
    sys.exit()


