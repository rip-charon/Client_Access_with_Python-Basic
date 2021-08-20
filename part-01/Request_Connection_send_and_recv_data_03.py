import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # tcp - connection

s.connect(('192.168.1.15',80))

print("\n[+] connected.")

s.send("GET /index.txt HTTP/1.0\n\n".encode())

data = s.recv(2048)

print("[+] here is a data : \n")

print(data)

s.close()