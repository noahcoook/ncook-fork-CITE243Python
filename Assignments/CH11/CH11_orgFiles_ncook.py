import shutil, os, re
from pathlib import Path

filesList = os.listdir(r'C:/Users/cookn/Downloads')

#print(f'{filesList}')
pattern = (r'\.pdf$')
for files in filesList:
    if re.search(pattern, files):
        shutil.copy(files, 'Assingments/CH11/pdfDocs')