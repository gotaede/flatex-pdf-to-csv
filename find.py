import re
from pdfminer import high_level as pdf
import os
import shutil

## Add all ISIN numbers with | as separator.
regex_Name = '(IE00B3RBWM25)|(IE00BK5BQT80)'

regex_Valuta = '(Valuta) *(\d\d.\d\d.\d\d\d\d)'
regex_Ausgefuehrt = '(Ausgef(.)*hrt) *: *(\d*.\d*)'
regex_Kurswert = '(Kurswert) *: *(\d*.\d*)'
regex_Kurs = '(Kurs) *: *(\d*.\d*)'
regex_Provision = '(Provision) *: *(\d*.\d*)'



sparplan = 'sparplan.csv'
inputfolder = '.'
outputfolder = 'processed'


def findfiles (dir=inputfolder):
    
    files = []
    folder = os.listdir(dir)
            
    for file in folder:
        if file.lower().endswith(('.pdf')):
            files.append(os.path.join(inputfolder,file))
        
    return files
    
def data_ (file):
    return pdf.extract_text(file)
    

def finddata (regex, data):
    regex = re.compile(regex)
    find = regex.search(data)
    
    return find

def write_csv (name, datum, stueck, kurs, kurswert, provision, filename=sparplan):

    if not os.path.exists(filename):
        not_exist = True
    else:
        not_exist = False
        
    with open(filename, 'a+') as file_object:
        
        #add first line headers if file does not exist
        if not_exist:
            file_object.write(f'Name;Datum;Stueck;Kurs;Kurswert;Provision\n')
            
        file_object.write(f'{name};{datum};{stueck};{kurs};{kurswert};{provision}\n')
        
    return True
    
     
if __name__ == '__main__':

    files = findfiles()
    for file in files:
        data = data_(file)
        name = finddata(regex_Name, data).group()
        datum = finddata(regex_Valuta, data).group(2)
        stueck = finddata(regex_Ausgefuehrt, data).group(3)
        kurs = finddata(regex_Kurs, data).group(2)
        kurswert = finddata(regex_Kurswert, data).group(2)
        provision = finddata(regex_Provision, data).group(2)
        
        if write_csv(name, datum, stueck, kurs, kurswert, provision):
            shutil.move(file, os.path.join(inputfolder, outputfolder))
        