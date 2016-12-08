import urllib
import xml.etree.ElementTree as EC

url = raw_input("Enter location: ")
if len(url)<1: url= "http://python-data.dr-chuck.net/comments_276674.xml"
# http://python-data.dr-chuck.net/comments_42.xml
print url
print 'Retrieving', url

data = urllib.urlopen(url).read()
print 'Retrieving',len(data),'characters'
# print data

lst_count = list()
tree = EC.fromstring(data)
# counts = tree.findall("comments/comment")
counts = tree.findall(".//comment")
print "Count:", len(counts)
for item in counts:
    count = int(item.find("count").text)
    lst_count.append(count)

# print type(lst_count), lst_count
print "Sum", sum(lst_count)





