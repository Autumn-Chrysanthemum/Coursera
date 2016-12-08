import urllib
from BeautifulSoup import *

url = raw_input("Enter URL: ")
if len(url)<1:
    url = "http://python-data.dr-chuck.net/known_by_Chidera.html"
    print url
try:
    count = int(raw_input("Enter count: "))
    position = int(raw_input("Enter position: "))
    html = urllib.urlopen(url).read()
except:
    print "Please check your data and try again"
    quit()

soup = BeautifulSoup(html)
tags = soup("a")


for tag in tags:
    while count >= 0:
        print "Retrieving: ", url
        url = tags[position - 1].get("href", None)
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup("a")
        count = count - 1

