#code from example 2 -- gets the total grant amount requested & cleans it 
from lxml import html
import re

innerHTML = browser.execute_script("return document.body.innerHTML") 

page = html.document_fromstring(innerHTML) #parse innerHTML

iput = page.get_element_by_id("autcTotalGrantReq") #get the input elem

amt = iput.value #get value

#cleans
regex = re.compile("[$,]") #compile regex
cleaned_amt = regex.sub("", amt) #replace every "$" and "," with ""

print(cleaned_amt)
