import urllib
from BeautifulSoup import *

url = raw_input("Enter - ")
if len(url)<1: url = "http://python-data.dr-chuck.net/comments_276677.html"

try:
    html = urllib.urlopen(url).read()
except:
    print "File: <",url,"> does not exist"
    quit()

soup = BeautifulSoup(html)

tags = soup("span")

count = 0
comments_sum = list()
for tag in tags:
    count  = count + 1
    number = int(tag.contents[0])
    comments_sum.append(number)

print "Count", count
print "Sum", sum(comments_sum)



