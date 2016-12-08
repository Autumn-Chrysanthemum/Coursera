import re

expression = raw_input("Enter a regular expression: \n")

fname = raw_input("Enter a file name: \n")
if len(fname)<1: fname = "mbox.txt"
try:
    hand = open(fname)
except:
    print "File does not exist"
    quit()

count = 0
for line in hand:
    line = line.rstrip()
    if re.search(expression, line):
        count = count + 1


print "mbox.txt had", count,"lines that matched", expression