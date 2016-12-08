name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
	handle = open(name)
except:
    print "File <",name,"> does not exist"

dict_greatest = dict()

for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.rstrip()
        words = line.split()

        dict_greatest[words[1]] = dict_greatest.get(words[1],0) + 1

#print "Dictinary:", dict_greatest

largest = None
for key in dict_greatest:
    if largest is None or dict_greatest[key] > largest:
        largest = dict_greatest[key]
for key in dict_greatest:
    if dict_greatest[key] == largest:
        print key, dict_greatest[key]







        