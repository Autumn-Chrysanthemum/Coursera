import re

# s = "Helli from csev@umich.edu to cwen@iupui.edu about the meeting @2PM"
# lst = re.findall("\S+@\S+", s)
# print lst

file = raw_input("Please enter file name \n")

if len(file)<1: file = "mbox-short.txt"

try:
    hand = open(file)
except:
    print "File:",file,"does not exist"
    quit()

# for line in hand:
#     line = line.rstrip()
#     lst = re.findall("\S+@\S+", line)
#     if len(lst)>0:
#         print lst

for line in hand:
    line = line.rstrip()
    lst = re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z]", line)
    if len(lst)>0:
        print lst


