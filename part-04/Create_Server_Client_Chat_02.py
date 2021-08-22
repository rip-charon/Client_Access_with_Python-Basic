# CHARON :
# socket program for creating client on port 5050 for chatting in tcp connection with server

from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect(("192.168.1.123",5050))

print("connected to server \n")

while True:

    data = s.recv(1024)
    print("[+] person >> %s " % data.decode('utf-8'))
    print("\n")
    sms = input("[+] you >> ")
    s.send(sms.encode('utf-8'))
    print("\n")

s.close()