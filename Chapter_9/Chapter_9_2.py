name = raw_input("Enter file name:\n")
if len(name) < 1: name = "mbox-short.txt"
try:
    fhand= open(name)
except:
    print "File: <", name,"> does not exist"
    

d_weeks = dict()

for line in fhand:    
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
#         print "Debug", words
        
        d_weeks[words[2]] = d_weeks.get(words[2],0) + 1

print d_weeks