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
        word = words[1].split()
        for item in word:
            index = item.find('@')
            domain = item[index+1:]           
#         print "Debugging", word
#         print "Debugging", index
#         print "Debugging", domain

        d_mails[domain] = d_mails.get(domain,0) + 1

print "Mails from:", d_mails