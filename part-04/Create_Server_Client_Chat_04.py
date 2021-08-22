# CHARON :
# socket program for creating client on port 5050 for chatting in tcp connection with server

from socket import *

print("[+] client chat is running : ")

name = input("[+] Enter your name : ")

s = socket(AF_INET, SOCK_STREAM)

s.connect(("192.168.1.123",5050))

print("connected to server \n")

while True:

    data = s.recv(1024)
    print(data.decode('utf-8'))
    print("\n")
    sms = input("[+] you >> ")
    s.send("[+] {name} >> %s".encode('utf-8') % sms)
    print("\n")

s.close()