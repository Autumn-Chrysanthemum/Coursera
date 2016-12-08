fname = raw_input("Please enter file name: \n")
if len(fname) < 1: fname = "romeo.txt"
try:
    fhandle = open(fname)
except:
    print "File:", fname,"does not exist"
    quit()
text = fhandle.read()
text = text.rstrip()
text = text.split()



text_dict = dict()
test_value = 0

for word in text:
    text_dict[word] = test_value
    test_value = test_value + 1
print text_dict

lst = text_dict.keys()
print lst
lst.sort()
# print lst
for key in lst:
    print key, text_dict[key]