#!/usr/local/bin/python3.6
fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)

import math
print(hasattr(math.sqrt,'__call__'))

def hello(name):
    return 'Hello,'+name+'!'

print(hello('world'))
print(hello('Gumby'))
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print(fibs(10))
print(fibs(0))
print(fibs(1))

def square(x):
    'calculates the suare'
    return x*x;
print(square.__doc__)
print(help(square))
