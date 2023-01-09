# PDF recreate creation date script
# Written to handle PDF files that have been downloaded and therefore have their file date set as the download date
# PyPDF2 used to extract the PDF Creation Date metadata from the file, then use touch to change the file attribute

from PyPDF2 import PdfReader
import subprocess
from glob import glob

def get_info(path):
    print(path)
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        info = pdf.metadata
    
    touchDate = info.creation_date_raw[2:14]
    subprocess.run(('touch', '-t', touchDate, path))

if __name__ == '__main__':
    path = '1.pdf'
    directories = glob("*.pdf")
    for file in directories:
        get_info(file)
