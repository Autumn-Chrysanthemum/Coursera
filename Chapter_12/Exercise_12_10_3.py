# Use urllib to replicate the previous exercise of
# (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document.
#  Dont worry about the headers for this exercise,
# simply show the first 3000 characters of the document contents.

import urllib

print "Please enter a URL:"
#  http://www.py4inf.com/code/romeo-full.txt
urlstr = raw_input().strip()
# print urlstr

try:
    fhand = urllib.urlopen(urlstr)
except:
    print "Please enter correct URL"
    quit()


count = 0
while True:
    data = fhand.read(150)
    if ( len(data) < 1 ) or count >= 3000: break
    count = count + len(data)
    print data

print "Number of characters:", count

fhand.close()
