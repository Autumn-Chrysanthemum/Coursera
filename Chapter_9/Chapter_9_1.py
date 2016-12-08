
fname = raw_input("Please enter file name: \n")
if len(fname) < 1: fname = "words.txt"
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
    if "}" in word or word.startswith("{"): continue
    text_dict[word] = test_value
    test_value = test_value + 1
print text_dict
print test_value

check = raw_input("Please type a word:\n")
if check in text_dict:
    print "Yes!"
else:
    print "No!"
    
    
    

