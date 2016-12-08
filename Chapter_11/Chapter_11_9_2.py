import re

fname = raw_input("Enter file: \n")
if len(fname)<1: fname = "mbox.txt"

try:
    hand = open(fname)
except:
    print "File:",fname,"does not exist"
    quit()

counter = 0
lst = list()


for line in hand:
    line = line.rstrip()
    number = re.findall("^New Revision: ([0-9]+)", line)

    if len(number)>0:
        number = float(number[0])
        # print type(number)
        lst.append(number)

print sum(lst)/len(lst)
