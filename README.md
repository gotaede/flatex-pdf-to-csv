# flatex-pdf-to-csv
    
The Script will parse all *.pdf files in the current folder, add the values to sparplan.csv and move the processed file to folder processed.

## How to use it
### Installation
* Download find.py and requirements.txt to folder sparplan
* Create subfolder processed
* Download PDFs from flatex to folder sparplan
* Install requirements.

``` pip install -r requirements.txt ```

## Configuration
Add all ISIN numbers. You can add multible ISIN with | as separator.
    
    regex_Name = '(IE00B3RBWM25)|(IE00BK5BQT80)'
    
### Run the script
    python.exe find.py
    

