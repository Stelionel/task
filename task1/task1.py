# -*- coding: utf-8 -*-
import sys
import numpy as np

a=[]
f = open(sys.argv[1], 'r')
for line in f:
    a.append([float(x) for x in line.split()])
f.close()

per=np.percentile(a,90)
print("%.2f" % per)
med=np.percentile(a,50)
print("%.2f" % med)
maxi=np.max(a)
print("%.2f" % maxi)
mini=np.min(a)
print("%.2f" % mini)
sred=np.mean(a)
print("%.2f" % sred)