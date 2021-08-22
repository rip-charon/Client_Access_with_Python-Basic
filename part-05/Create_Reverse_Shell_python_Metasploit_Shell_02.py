# CHARON :
# socket program to access to cmd with python with call method

import subprocess

while True :

    cmd = input("shell=> ")

    c = subprocess.call(cmd , shell=True)

    print(c)