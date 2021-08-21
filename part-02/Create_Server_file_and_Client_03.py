# CHARON :
# socket program for creating server on port 5050 [ time server ].

from socket import *
import time

s = socket(AF_INET,SOCK_STREAM)

s.bind(("0,0,0,0",5050))

s.listen(5)

while True:

    client , addr = s.accept()
    print("connected to"+str(addr)+"\n")
    date = time.ctime()
    client.sendall("time : "+date)

client.close()