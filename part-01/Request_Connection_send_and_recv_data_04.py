import socket

while True :

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ip = input("[+] ip : ")

    port = int(input("[+] port : "))

    try :

        s.connect((ip,port))
        print("[+] open port.")

    except : 

        print("[+] close port")
