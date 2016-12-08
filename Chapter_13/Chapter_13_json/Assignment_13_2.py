import urllib
import json

url = raw_input("Enter location:")
if len(url)< 1: url = "http://python-data.dr-chuck.net/comments_276678.json"

# "http://python-data.dr-chuck.net/comments_42.json"

print "Retriveing:", url

try:
    data = urllib.urlopen(url).read()
except:
    print url,"does not exist"
    quit()

# print "TYPE:", type(data)
print "Retriveing:", len(data), "characters"
# print data

info = json.loads(data)
# print "TYPE(INFO):", type(info)
# print "LEN(INFO)", len(info)
# print "All DATA: \n", json.dumps(info, indent=4)

count = 0
lst = list()
for item in info["comments"]:
    lst.append(info["comments"][count]["count"])
    count = count + 1

print "Count:", count
print "Sum:", sum(lst)

