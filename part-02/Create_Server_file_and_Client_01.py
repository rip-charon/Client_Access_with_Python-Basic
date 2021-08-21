# CHARON :
# socket program fot creating server on port 2323 and send and recive data from client side.

from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.bind(("192.168.1.115",2323))

s.listen(5)

print("[+] server start running on port 2323 \n")

client , addr = s.accept()

print("connected to %s \n " % str(addr))

client.sendall("hello i am server... ")

data = client.recv(1024)

print(data)

client.close()