import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80)) #up to this point we just open the socket
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n') # here we actually send the request to the socket. We need to specify the protocol which in this case is HTTP and we need the two lines

while True:
    data = mysock.recv(512) # .recv specify the size of what it is sent
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()