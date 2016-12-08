# Program should counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters
# and display the count of the number of characters at the end of the document.

import socket


print "Please enter a URL:"
#  http://www.py4inf.com/code/romeo-full.txt
urlstr = raw_input().strip()
# print urlstr

# get the last "word" for url
words = urlstr.split("/")
host_name = words[2]
# print host_name

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    mysock.send('GET '+urlstr+' HTTP/1.0\n\n')
except:
    print "Please enter correct URL"
    quit()

count = 0
while True:
    data = mysock.recv(150)
    if ( len(data) < 1 ) or count >= 3000: break
    count = count + len(data)
    print data

print "Number of characters:", count

mysock.close()
