# fixMyPDFs
A python script to set a PDF file's "created date" attribute to its original creation date as stored in the PDF metadata

I want to export all of my PDF attachments from Evernote and import them to Google Drive, but I found that exporting from Evernote sets the PDF file attributes to the date of the export, not the original date that the PDF file was created. That would mean that my PDFs can't be sorted in scanned-date order.

I've created this python app to work on all PDFs in a folder and change each file's creation date to the Creation Date PDF metadata that is stored inside the PDF file

As an extra I also found that some of my PDFs were created without OCRed searchable text so I included a check. Any files without text get run through OCRmyPDF

This simple python script leans heavily on PyPDF2 and OCRmyPDF, massive thanks to both:

https://pypi.org/project/PyPDF2/

https://ocrmypdf.readthedocs.io/en/latest/index.html
