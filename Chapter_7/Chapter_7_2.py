name_file = raw_input("Enter the file name: \n")
try:
    file = open(name_file)
except:
    print "File",name_file,"does not exist"
    quit()
count = 0
sum_line = 0
avg = 0
for line in file:    
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        line = line.rstrip()
        pos = line.find(":")
        host = float(line[pos+1:])
        sum_line = sum_line + host
    else:
        continue    
avg = sum_line / count
print "Average spam confidence:", avg
print "Count:", count
print "Sum:", sum_line 
