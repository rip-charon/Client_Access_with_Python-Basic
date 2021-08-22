# CHARON :
# socket program to access to cmd with python whit popen method

import subprocess

while True :

    cmd = input("shell=> ")

    c = subprocess.Popen(cmd , shell=True , stdout = subprocess.PIPE , stderr=subprocess.PIPE , stdin=subprocess.PIPE)

    cmd_ = c.stdout.read()+c.stderr.read()

    print(cmd_)