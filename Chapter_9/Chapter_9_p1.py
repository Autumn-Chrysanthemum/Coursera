# you are given a string and you want to count
# how many times each letter appears
# using FOR and IN



word = raw_input("Please type any word:\n")
if len(word) <1 : word = "brontosaurus"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print d

letter = raw_input("Please type letter:\n")

print d.get(letter,0)



# while True:
#     letter = raw_input("Please type letter:\n")
#     if letter == "Done"
#         break
#     if len(letter)<1:
#         print "Try again"
#         continue
#     x = d.get(letter,0)
# print x