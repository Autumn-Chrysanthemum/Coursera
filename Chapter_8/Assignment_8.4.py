fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
try:
	fh = open(fname)
except:
    print "File",fname,"does not exist"
    quit()

lst = list()


for line in fh:
    line = line.rstrip()
    line = line.split("\n")

        
    for element in line:
        element = element.split()

        
        for item in element:            
            if item not in lst:
                lst.append(item)


lst.sort()           
print lst
                    

