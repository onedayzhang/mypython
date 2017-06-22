#!/usr/local/bin/python3.6
import math as footbar
print(footbar.sqrt(4))

from math import sqrt as footbar
print(footbar(4))

#5.2
x,y,z=1,2,3
print(x,y,z)
x,y=y,x
print(x,y,z)
#5.4
name=input('What is your name?')
if name.endswith('Gumby'):
 print('Hello,Mr.Gumby')
else:
 print('Hello, stranger')
num=int(input('Enter a number:'))
if num>0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('zero')


name=input('What is your name?')
if name.endswith('Gumby'):
 if name.startswith('Mr.'):
  print('Hello,Mr.Gumby')
 elif name.startswith('Mrs.'):
  print('Hello,Mrs.Gumby')
else:
 print('Hello, stranger')
