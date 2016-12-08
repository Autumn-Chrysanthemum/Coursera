import re

fname = raw_input("Enter file: \n")
if len(fname)<1: fname = "regex_sum_276672.txt"

try:
    hand = open(fname)
except:
    print "File:",fname,"does not exist"
    quit()

lst = list()
text = hand.read()
numbers = re.findall('\d+', text)

for number in numbers:
    number = int(number)
    lst.append(number)
print sum(lst)

