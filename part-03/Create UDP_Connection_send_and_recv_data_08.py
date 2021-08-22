# CHARON
# socket program for creating TCP server that have timeout

from socket import *

s = socket(AF_INET , SOCK_STREAM)

server = "0.0.0.0"

port = 5050

ADDR = (server,port)

s.bind((ADDR))

s.listen(5)

s.settimeout(6)

print("[+] server is running on port 5050 \n")

try :

    c , adrr = s.accept()

    print("[+] connected to %s \n" % str(adrr))

except :

    print("[+] server closed. ")

s.close()