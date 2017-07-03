#!/usr/local/bin/python3.6
from random import choice
x=choice(['Hello,world!',[1,2,'e','e',4]])
print(x.count('e'))

def add(x,y):
    return x+y

print(add(1,2))
print(add('Fish','license'))
def lendth_message(x):
    print("The length of",repr(x),"is",len(x))

lendth_message('Fnord')
lendth_message([1,2,3])

#o=OpenObject()
#o.setName('Sir')
#print(o.getname())

__metaclass__=type
class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print("hello,world I'm %s."%self.name)
foo=Person()
bar=Person()
foo.setName('luke')
bar.setName('Anakin')
foo.greet()
bar.greet()
print(foo.name)
bar.name='yoda'
bar.greet()

class Class:
    def method(self):
        print('I have a self')
def function():
    print('I dont...')
instance=Class()
instance.method()
instance.method=function
instance.method()

class Secretive:
    def __inaccessible(self):
        print("bet you can't see me...")
    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()
s=Secretive()
#s.__inaccessible()
s.accessible()

s._Secretive__inaccessible()
