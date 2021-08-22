# CHARON
# TCP socket program for scan ip address for checking close or open port.

from socket import *

while True:

    s = socket(AF_INET,SOCK_STREAM)

    ip = input("[+] ip : ")

    port = int(input("[+] port : "))

    r = s.connect_ex((ip,port))

    if r == 0 :

        print("[-] check >> open port")

    else :

        print("[-] check >> close port")

s.close()