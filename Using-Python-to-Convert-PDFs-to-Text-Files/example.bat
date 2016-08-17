@rem calls pdfminer from the command line to convert PDFs to text files

@rem change to your new folder
cd "C:\pdfToText" 

@rem make txt file, name it example.txt
cmd /k pdf2txt.py -o example.txt example.pdf 


@rem loop through every pdf in folder and convert it to text
cd "c:\pdftotext\pdfs"
cmd /k for %%i in (*) do "c:\pdftotext\pdf2txt.py" -o c:\pdftotext\txt\%%~ni.txt %%i
