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
