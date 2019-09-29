# -*- coding: utf-8 -*-
import sys
 
a = [0] * 721
f = open(sys.argv[1], 'r')
for line in f:
    t1, t2 = line.strip().split()
    h1, m1 = list(map(int, t1.split(':')))
    h2, m2 = list(map(int, t2.split(':')))
    print(60 * (h1 - 8) + m1, 60 * (h2 - 8) + m2)
    for i in range(60 * (h1 - 8) + m1, 60 * (h2 - 8) + m2):
        a[i] += 1
f.close()
 
f = False
res = max(a)
for i in range(721):
    if a[i] == res:
        if not f:
            f = True
            h = str(8 + i // 60)
            m = str(i % 60)
            if len(m) == 1:
                m = '0' + m
            print(h, m, sep=':', end='')
    else:
        if f:
            f = False
            print(' ', end='')
            h = str(8 + i // 60)
            m = str(i % 60)
            if len(m) == 1:
                m = '0' + m            
            print(h, m, sep=':')