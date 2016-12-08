# Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time and
#   then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
#  sorted by hour as shown below.





name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "File does not exist"
    quit()

d_hours = dict()

for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
		words = line.split()
		word = words[5].split()
# 		print word
		for item in word:
		    index = item.find(":")
		    hour =item[:index]
# 		    print hour
		d_hours[hour] = d_hours.get(hour,0) + 1

# print d_hours

l_temp = list()
for key, val in d_hours.items():
    l_temp.append((key, val))
    l_temp.sort()

# print l_temp
for key, val in l_temp:
    print key, val