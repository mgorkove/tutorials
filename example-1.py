#from example 1 -- extracts & cleans text that describes the project 
from lxml import html
import re

innerHTML = browser.execute_script("return document.body.innerHTML") 

page = html.document_fromstring(innerHTML) #parse innerHTML

fset = page.get_element_by_id("fsetdesc") #get the fieldset

fset_text = fset.text_content()

#cleans 
fset_text = fset_text.replace("\n", "") #make all text one line

regex = "\(1 page\)[ \t\xa0\n]+(.+?)[ \t\xa0\n]+Identify"

project_description = re.findall(regex, fset_text)

print(project_description)