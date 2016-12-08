import urllib
import re

url = raw_input('Enter URL: \n')
# http://www.py4inf.com/book.htm

html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
print type(links)
for link in links:
    print link