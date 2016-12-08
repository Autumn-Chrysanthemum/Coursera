# One of the common uses of a dictionary is to count
# the occurrence of words in a file with some written text.
# Using GET




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
    print line
#     print words
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts