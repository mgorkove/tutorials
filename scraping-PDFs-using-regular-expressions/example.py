#extracts all dates in a text file
import re
text = open('test.txt') #open text file
for line in text: #iterate through every line
	#return list of dates in that line
	x = re.findall('.*?([a-zA-Z]+\s[0-9][0-9],\s[0-9][0-9][0-9][0-9]).*', line) 
	#if a date is found
	if len(x) != 0:
		print(x)
