# (Advanced) Change the socket program so that it only
# shows data after the headers and a blank line have been received.
# Remember that recv is receiving characters (newlines and all), not lines



import socket
import string

print "Please enter a URL:"
#  http://www.py4inf.com/code/romeo.txt
urlstr = raw_input("").strip()
# print urlstr

# get the last "word" for url

words = urlstr.split("/")
host_name = words[2]
# print host_name

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host_name, 80))
mysock.send('GET '+urlstr+' HTTP/1.0\n\n')

file_data = str()
while True:
    data = mysock.recv(512)
    file_data += data
    if ( len(data) < 1 ) :break

mysock.close()
# print file_data

split_data = string.split(file_data, '\n')
# print split_data
for item in split_data:
        # print item
    if(item == '\r'):
        pos = split_data.index(item)
end_data = split_data[pos+1:]

print "\n".join(end_data)
