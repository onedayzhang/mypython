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
#print(help(square))
def try_to_change(n):
    n='Mr.Gumby'
    print(n)
name='Mrs. Entity'
try_to_change(name)
print(name)

def hello_1(greeting,name):
    print('%s,%s!'%(greeting,name))

def hello_2(name,greeting):
    print('%s,%s!'%(name,greeting))

hello_1('hello','world')
hello_2('hello','world')

hello_1(greeting='hello',name='world')
hello_1(name='world',greeting='hello')

def heelo_3(greeting='hello',name='world'):
    print('%s,%s'%(greeting,name))
heelo_3()
heelo_3('Greetings')
heelo_3('greetings','universe')
heelo_3(name='Gumby')

def print_params(*params):
    print (params)

print_params('Testing')
print_params(1,2,3)

def print_params_2(title,*params):
    print (title)
    print (params)
print_params_2('params',1,2,3)
print_params_2('nothing')

def story(**kwds):
    return 'Once upon a time there was a '\
            '%(job)s called %(name)s.'%kwds
def power(x,y,*others):
    if others:
        print('Received redundant parameters: ',others)
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for setp>0'
    if stop is None:
        start,stop=0 ,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

print (story(job='king',name='Gumby'))
print (story(name='Sir Robin',job='brave knight'))
params={'job':'language','name':'python'}
print (story(**params))
del params['job']
print(story(job='stoke of genius',**params))

print(power(2,3))
print(power(3,2))
print(power(y=3,x=2))
params_1=(5.)*2
print(params_1)
#print(power(*params_1))
print(power(3,3,'Hello,world'))

print(interval(10))
print(interval(1,5))
print(interval(3,12,4))
print(power(*interval(3,7)))
