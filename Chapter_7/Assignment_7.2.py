fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
    quit()
    
total = 0
count = 0
average = 0

for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	else:
		pos = line.find(":")
		cut = float(line[pos+1:])
        count = count + 1
        total = total + cut
        
average = total/count            
print "Average spam confidence: ", average