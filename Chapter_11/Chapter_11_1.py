import re

fname = raw_input("Please enter file name: \n")
if len(fname) < 1: fname = "mbox-short.txt"
try:
    hand = open(fname)
except:
    print "File", fname, "does not exist"
    quit()

# for line in hand:
#     line = line.rstrip()
#     if re.search("From:",line):
#         print line


# for line in hand:
#     line = line.rstrip()
#     if re.search("^From:",line):
#         print line

# for line in hand:
#     line = line.rstrip()
#     if re.search("^F..m:",line):
#         print line

for line in hand:
    line = line.rstrip()
    if re.search("^From:.+@",line):
        print line
