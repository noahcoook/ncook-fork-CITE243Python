import ezsheets

user_spreadsheet = str(input('''Please enter a spreadsheet url.
Only include the url up to the /edit part
Example> https://docs.google.com/spreadsheets/d/.../
Can also give spreadsheet id as well, that is in between the /d/ and /edit/ tags. AKA the ... in example
                             
                             '''))


ss = ezsheets.Spreadsheet(user_spreadsheet)
print(ss.title)

def check_data_type():
    while True:
        data = str(input('''Please enter data type
Options include:
                         
Excel | ODS | CSV | TSV | PDF | HTML | 
                        
                        '''))
        if data == 'Excel':
            ss.downloadAsExcel()
            break
        elif data == 'ODS':
            ss.downloadAsODS()
            break
        elif data == 'CSV':
            ss.downloadAsCSV()
            break
        elif data == 'TSV':
            ss.downloadAsTSV()
            break
        elif data == 'PDF':
            ss.downloadAsPDF()
            break
        elif data == 'HTML':
            ss.downloadAsHTML()
            break
        else:
            continue

check_data_type()