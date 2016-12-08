import os
import urllib

print "Please enter a URL:"

# can use that to test:     http://www.py4inf.com/code/romeo-full.txt
urlstr = raw_input().strip()
img = urllib.urlopen(urlstr)

# get the last "word" for url

words = urlstr.split("/")
fname = words[-1]
# print fname

# don't overwrite the file
if os.path.exists(fname):
    if raw_input("Replace "+fname+" (Y/N)? \n") != "Y":
        print "Data not copied"
        exit()
    print "Replacing",fname

fhand = open(fname, "w")


size = 0
while True:
    info = img.read(100000)
    if len(info)<1: break
    size = size + len(info)
print size, "characters copied to", fname


fhand.close()