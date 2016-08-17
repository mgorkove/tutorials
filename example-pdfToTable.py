import requests 

#uses the PDFtables API to convert a table inside a PDF to a CSV, Excel file, etc
def pdfToTable(PDFfilename, apiKey, fileExt, downloadDir):
	fileData = (PDFfilename, open(PDFfilename, 'rb'))
	files = {'f': fileData}
	postUrl = "https://pdftables.com/api?key={0}&format={1}".format(apiKey, fileExt)
	response = requests.post(postUrl, files=files)
	response.raise_for_status()
	with open(downloadDir, "wb") as f:
    	f.write(response.content)