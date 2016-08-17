#extracts the second page from all PDFs in a directory and adds it to a new PDF
import os
import PyPDF2

path = "/Users/Someone/Documents/allPDFs" #path to folder
#page number to extract, added 1 to reflect counting starting at 0
page = 3 
writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object

for pdf in os.listdir(path):
	PDFfilename = path + "/" + pdf
	pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object
	pg2 = pfr.getPage(page) #extract pg 2
	writer.addPage(pg2) #add pg 2

NewPDFfilename = "allTables.pdf" #filename of your PDF/directory where you want your new PDF to be
with open(NewPDFfilename, "wb") as outputStream: #create new PDF
	writer.write(outputStream) #write pages to new PDF