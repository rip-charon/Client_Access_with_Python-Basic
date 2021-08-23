# simple command for running python simple http server :

# >> python -m http.server 5050

# some example code and method (useful ones) :

import socket

# domin convert to ip :

print(socket.gethostbyname("google.com")) 

# domin convert to ip return with domin:

print(socket.gethostbyname_ex("bing.com"))

# ip system :

print(socket.gethostbyname(socket.gethostname()))

# ip system return with pc name :

print(socket.gethostbyname_ex(socket.gethostname()))

# ip convert to domin :

print(socket.gethostbyaddr('172.217.21.46'))

# tell port of portocol by name :

print(socket.getservbyname('http'))

# tell port of portocol by name and type :

print(socket.getservbyname('smtp','tcp'))

# tell service name by port :

print(socket.getservbyport(80))