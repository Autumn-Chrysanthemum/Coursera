import re

fname = raw_input("Enter file name \n")
if len(fname)<1: fname = "mbox-short.txt"

try:
    hand = open(fname)
except:
    print "File:",fname,"does not exist"
    quit()

# for line in hand:
#     line = line.rstrip()
#     if re.search("^X\S*: [0-9.]+", line):
#         print line

# for line in hand:
#     line = line.rstrip()
#     x = re.findall("^X\S*: ([0-9.]+)", line)
#     if len(x) > 0:
#         print x

# count = 0
# for line in hand:
#     line = line.rstrip()
#     x = re.findall("^Details:.*rev=([0-9]+)", line)
#     if len(x)>0:
#         count = count + 1
#         print x
# print count


for line in hand:
    line = line.rstrip()
    x = re.findall("^From .* ([0-9][0-9]):", line)
    if len(x)>0:
        print x