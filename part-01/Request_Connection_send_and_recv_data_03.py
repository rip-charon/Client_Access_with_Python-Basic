# CHARON :
# simple socket program just for connecting to local ip address and read the file in server .

import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # tcp - connection

s.connect(('192.168.1.115',80))

print("\n[+] connected.")

s.send("GET / HTTP/1.1\r\nHost:192.168.1.115\r\n\r\n".encode())

data = s.recv(2048)

print("[+] here is a data : \n")

print(data)

s.close()
