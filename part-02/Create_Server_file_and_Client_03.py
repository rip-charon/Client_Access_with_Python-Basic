# CHARON :
# socket program for creating server on port 5050 [ time server ].

from socket import *
import time

s = socket(AF_INET,SOCK_STREAM)

server = "0.0.0.0"

port = 5050

ADDR = (server,port)

s.bind((ADDR))

s.listen(5)

while True:

    client , addr = s.accept()
    print("connected to"+str(addr)+"\n")
    date = time.ctime()
    data = "time : "+date
    client.sendall(data.encode("utf-8"))

client.close()