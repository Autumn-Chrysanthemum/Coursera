# One of the common uses of a dictionary is to count
# the occurrence of words in a file with some written text.
# Using FOR and IN



fname = raw_input("Please enter the file name:\n")
if len(fname) < 1: fname = "romeo.txt"
try:
    fhand = open(fname)
except:
    print "File <",fname,"> cannot be opened"
    exit()
    
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
#     print words
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print counts