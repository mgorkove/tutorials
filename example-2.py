#downloads all PDFs on a page
from lxml import html
import requests
import urllib

link = "http://sdirwmp.org/contact-us"

response = requests.get(link, allow_redirects = False) #get page data from server, block redirects

sourceCode = response.content #get string of source code from response

htmlElem = html.document_fromstring(sourceCode) #make HTML element object

base_href = "http://www.sandag.org" #what you need to add to the links to make them absolute

htmlElem.make_links_absolute(base_href, resolve_base_href=True) 

numPdf = 0 # number to add to the download filename of each pdf to make it unique
for elem in htmlElem.iterlinks(): #for each tuple in the generator
	link = elem[2] #get the link, which is at index 2
	fileExtension = link.split(".")[-1] 
	# ^ split link into a list by "." and get the last elem, which is the file extension
	if fileExtension == "pdf":
		downloadDir = "pdf%s.pdf" %numPdf #directory where the pdf will be downloaded to 
		urllib.request.urlretrieve(link, downloadDir) #download the pdf
		numPdf += 1

	
baseDir = "C:/Users/Someone/Documents/AllPDFs/"
filename = "pdf%s.pdf" %numPdf
downloadDir = baseDir + filename
urllib.request.urlretrieve(link, downloadDir) 

