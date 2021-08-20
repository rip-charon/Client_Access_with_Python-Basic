import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # tcp - connection

s.connect(('192.168.1.115',80))

print("[+] connected.")

s.close()