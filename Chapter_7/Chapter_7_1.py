name_file = raw_input("Enter the name of the file: \n")
try:
    file = open(name_file)
except:
    print "File",name_file,"does not exist"
    quit()
count = 0
for line in file:
    count = count + 1
    if count < 6:
        line = line.rstrip()
        new_line = line.upper()
    else:
        quit()
    print new_line
print count