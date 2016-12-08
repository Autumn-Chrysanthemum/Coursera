import urllib

fhand = urllib.urlopen("http://www.py4inf.com/code/intro-short.txt")

for line in fhand:
    print line.strip()

