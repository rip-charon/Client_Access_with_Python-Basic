# CHARON :
# simple socket program just for connecting to google.com ip address and print the page in console.


import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # tcp - connection

s.connect(('172.217.19.174',80))

print("\n[+] connected.")

s.send("GET /index.php HTTP/1.0\n\n".encode())

data = s.recv(2048)

print("[+] here is a data : \n")

print(data)

s.close()