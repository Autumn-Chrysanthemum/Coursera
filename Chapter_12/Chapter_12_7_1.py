# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# or you have to Download BeautifulSoup form internet
# (https://www.crummy.com/software/BeautifulSoup/#Download)
# and install Beautiful Soup 4 with: pip install beautifulsoup4
# or install it inside the PyCharm by clicking on red underline word
# Documentation: http://www.crummy.com/software/BeautifulSoup/

import urllib
from BeautifulSoup import *

url = raw_input("Enter url: \n")
if len(url)<1: url = "http://www.dr-chuck.com/page1.htm"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print tag.get("href", None)

# The program prompts for a web address,
# then opens the web page, reads the data
# and passes the data to the BeautifulSoup parser,
# and then retrieves all of the anchor tags
# and prints out the href attribute for each tag
