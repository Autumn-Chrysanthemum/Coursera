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
#		print words
	
	
	    for word in words:
			if "@" in word:
		    	dict_greatest[word]=dict_greatest.get(word,0)+1

print dict_greatest
        