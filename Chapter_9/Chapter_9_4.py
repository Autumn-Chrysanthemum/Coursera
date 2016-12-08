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
        d_mails[words[1]] = d_mails.get(words[1],0) + 1
        
larger_key = None
larger_value = None

for d_key, d_val in d_mails.items():
    if larger_value == None or d_val > larger_value:
        larger_value = d_val
        larger_key = d_key
        
print "Mails from:", d_mails
print larger_key, larger_value

