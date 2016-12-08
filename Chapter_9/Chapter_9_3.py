name = raw_input("Enter file name:\n")
if len(name) < 1: name = "mbox-short.txt"
try:
    fhand = open(name)
except:
    print "File: <", name, "> does not exist"


d_mails = dict()

for line in fhand:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
#         print words
        d_mails[words[1]] = d_mails.get(words[1],0) + 1
# 
print "Mails from:", d_mails
# 

