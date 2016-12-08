import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.dr-chuck.com", 80))
mysock.send("GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n")

all_data = str()
while True:
    data = mysock.recv(512)
    if (len(data) < 1): break
    all_data += data

mysock.close()

print all_data