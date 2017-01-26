# now use socket as usual
import socket

def make_request():
    addr = socket.getaddrinfo('maker.ifttt.com', 443)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET /trigger/ESP/with/key/<my key> HTTP/1.1\r\nHost: maker.ifttt.com\r\n\r\n')
    data = s.recv(1000)
    s.close()

