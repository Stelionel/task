# -*- coding: utf-8 -*-
import sys
 
queue = [[], [], [], [], []]
for i in range(5):
    f = open(sys.argv[1] + '\Cash' + str(i + 1) + '.txt', 'r')
    for line in f:
        queue[i].append(float(line.strip()))
    f.close()
 
res = sum1 = 0
for i in range(5):
    sum1 += queue[i][res]
for i in range(1, 16):
    sum2 = 0
    for j in range(5):
        sum2 += queue[j][i]    
    if sum2 > sum1:
        res = i
        sum1 = sum2
       
print(res + 1)