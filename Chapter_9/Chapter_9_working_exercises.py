name = raw_input("Enter file name:\n")
if len(name) < 1: name = "clown.txt"
try:
    handle = open(name)
except:
    print "File <",name,"> does not exist"
    
text = handle.read()

# print len(text)
# print text[:200]

words = text.split()

# print len(words)
# print words

counts = dict()
for word in words:
#     print word
    counts[word] = counts.get(word,0) + 1

# print counts
# print counts.items()

max_key = None
max_value = None
for d_key, d_val in counts.items():
    if max_value == None or d_val > max_value:
        max_value = d_val
        max_key = d_key
        
#     print d_key, d_val, max_key, max_value
    
print "Max value:", max_value
print "Max key:", max_key
