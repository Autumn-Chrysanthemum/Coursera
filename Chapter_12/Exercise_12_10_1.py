import socket
import urllib

print "Please enter a URL:"
 # http://www.py4inf.com/code/romeo-full.txt
urlstr = raw_input().strip()
# print urlstr
try:
    img = urllib.urlopen(urlstr)
except:
    print "Please enter correct URL"
    quit()

# get the last "word" for url

words = urlstr.split("/")
host_name = words[2]
# print host_name

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
mysock.send('GET '+urlstr+' HTTP/1.0\n\n')
str = ""
while True:
    data = mysock.recv(512)
    str += data
    if ( len(data) < 1 ) :
        break

mysock.close()

print str