# CHARON :
# socket program for creating server and read from browser.

from socket import *
import time

s = socket(2,1)

s.bind(("192.168.1.123",1234))
s.listen(5)

print("running ... \n")

while True :

    c , addr = s.accept()

    print("connected to "+str(addr)+"\n")

    s.sendall(bytearray("HTTP/1.1 200 ok\n", "ascii"))


    time.sleep(5)

s.close()