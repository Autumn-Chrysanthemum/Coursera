import re
#
# fname = raw_input("Enter file: \n")
# if len(fname)<1: fname = "regex_sum_42.txt"
#
# try:
#     hand = open(fname)
# except:
#     print "File:",fname,"does not exist"
#     quit()
#
# text = hand.read()
# text = text.strip()
# print text
# counter = 0
# lst = list()


# for line in hand:
#     line = line.rstrip()
#     number = re.findall("(\d+).*", line)
#
#     if len(number)>0:
#
#
#         number = int(number[0])
#         print number
#         # print type(number)
#         lst.append(number)
#
# print sum(lst), len(lst)

file = open("regex_sum_42.txt")
text = file.read()

x = re.findall('\d+', text)
print x, len(x)