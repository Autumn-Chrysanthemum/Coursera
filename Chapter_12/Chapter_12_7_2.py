# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

# or you have to Download BeautifulSoup form internet:
# (https://www.crummy.com/software/BeautifulSoup/#Download)
# and install Beautiful Soup 4 with: pip install beautifulsoup4
# or install it inside the PyCharm by clicking on red underline word
# Documentation: http://www.crummy.com/software/BeautifulSoup/


import urllib
from BeautifulSoup import *

url = raw_input("Enter url: \n")
if len(url)<1: url= "http://www.dr-chuck.com/page1.htm"
http = urllib.urlopen(url).read()
soup = BeautifulSoup(http)

# Retrive all of the anchor tags
tags = soup("a")
for tag in tags:
    # look at the parts of a tag

    print "TAG: \n", tag
    print "URL: \n", tag.get("href", None)
    print "CONTENT: \n", tag.contents[0]
    print "ATTRS: \n", tag.attrs


# you can use BeautifulSoup to pull out various parts of each tag
