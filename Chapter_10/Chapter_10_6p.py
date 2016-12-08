# The most common words

import string
fhand = open ("romeo-full.txt")

counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
#     line = line.rstrip()
    words = line.split()
    for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
        counts[word]=counts.get(word,0) + 1 

#sort dictionary by value        
lst = list()
for key, value in counts.items():
    lst.append((value, key))
lst.sort(reverse=True)

for value, key in lst[:10]:
    print value, key

