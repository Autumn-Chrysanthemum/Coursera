# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# Program should extract and count paragraph (p) tags from the retrieved HTML document
# and display the count of the paragraphs as the output of your program.
# Do not display the paragraph text, only count them.
# Test your program on several small web pages as well as some larger web pages.


import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: \n ')
if len(url)<1: url = "http://www.py4inf.com/book.htm"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = 0
# Retrieve all of the paragraph tags
tags = soup('p')
for tag in tags:
    count = count + 1

print count, "Paragraph tags in that HTML document"