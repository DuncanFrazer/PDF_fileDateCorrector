# PDF fixer to recreate file creation date, and add an OCR layer if it doesn't exist (English)
# Written to handle PDF files that have been downloaded and therefore have their file date set as the download date
# PyPDF2 used to extract the PDF Creation Date metadata from the file, then use touch to change the file attribute
# OCRmyPDF used to add an OCR layer to the PDF document so that the PDF is searchable

from PyPDF2 import PdfReader
import subprocess
from glob import glob

filesProcessed = 0
filesOCRed = 0
filesWithNoCreatedDate = 0

def get_info(path):
    global filesProcessed
    global filesOCRed
    global filesWithNoCreatedDate

    print(path)
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        info = pdf.metadata
        text = pdf.pages[0].extract_text()
    
    if text=="":
        print("*** no embedded OCR text, running OCRmyPDF ***")
        subprocess.run(('ocrmypdf', path, path)) # by default ocrmypdf will work in English. I want the original file overwritten with the OCRed version
        filesOCRed += 1

    # run date correct after any OCR activity otherwise the OCRing will cause the file to have today's date
    try:
        info.creation_date_raw
    except:
        filesWithNoCreatedDate += 1
        print("*** no creation date in the PDF, skipping ***")
    else:
        touchDate = info.creation_date_raw[2:14]
        subprocess.run(('touch', '-t', touchDate, path))
        filesProcessed += 1

if __name__ == '__main__':
    directories = glob("*.pdf")
    for file in directories:
        get_info(file)
    print ("--------------------------------")
    print ("Files processed = " + str(filesProcessed))
    print ("Files that had OCR added = " + str(filesOCRed))
    print ("Files that had no date and need manual date correction = " + str(filesWithNoCreatedDate))

