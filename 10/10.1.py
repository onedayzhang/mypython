#!/usr/local/bin/python3.6
import math
print(math.sin(0))
import hello
import hello2
hello2.hello()
import sys
print(sys.path)
import drawing
import drawing.colors
from drawing import shapes

import copy
print(dir(copy))
print([n for n in dir(copy) if not n.startswith('_')])
print(copy.__all__)
#help(copy.copy)
print(copy.__file__)
print(sys.platform)
import os
os.system('ifconfig')

print(set(range(10)))
print(set([0,1,2,3,0,1,2,3,4,6]))
a=set([1,2,3])
b=set([2,3,4])
print(a.union(b))
print(a|b)

from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap=[]
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heap)
import time
print(time.asctime())
print(time.time())
print(time.localtime())
print(time.mktime(time.localtime()))

import shelve
import re
print(re.__all__)

some_text='alpha,beta....gama delta'
print(re.split('[,]+',some_text))
