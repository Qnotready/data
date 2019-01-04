#!/usr/bin/env python
# -*- coding:utf-8 -*-

msg = "abdcefghIJKLMNOPQRstuvwxyz"
b = []
c = []
for i in msg:
    b.append(int(ord(i)))

for j in b:
    if j >= 97:
        j = j - 32
        c.append(chr(j))
    else:
        j = j + 32
        c.append(chr(j))

print(list(msg))
print(c)
