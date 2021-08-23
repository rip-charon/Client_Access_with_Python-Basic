# CHARON :
# socket program for creating client on port 5050 for chatting in tcp connection (client side) with encryption

from socket import *
import pyaes

key = "Key_is_python_AH".encode()

aes = pyaes.AESModeOfOperationCTR(key)

s = socket(AF_INET, SOCK_STREAM)

s.connect(("192.168.1.115",5050))

print("connected to server \n")

while True:

    data = aes.decrypt(s.recv(1024))
    print("[+] person >> %s " % data.decode('utf-8'))
    print("\n")
    sms = input("[+] you >> ")
    cipher_sms = aes.encrypt(sms)
    s.sendall(cipher_sms)
    print("\n")

s.close()