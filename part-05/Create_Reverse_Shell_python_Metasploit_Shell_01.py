# CHARON :
# socket program to access to cmd with python whit checl_output method

import subprocess

while True :

    cmd = input("shell=> ")

    c = subprocess.check_output(cmd , shell=True)

    print(c)