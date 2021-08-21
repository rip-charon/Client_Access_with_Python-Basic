# CHARON :
# socket program for creating client on port 5050 for requesting time from server.

from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.connect(('192.168.1.115',5050))

print("[+] connected... \n")

data = s.recv(1024)

print(data)

s.close()