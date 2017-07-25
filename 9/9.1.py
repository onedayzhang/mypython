#!/usr/local/bin/python3.6
class FootBar:
    def __init__(self,value=42):
        self.somevar=value
f=FootBar()
print(f.somevar)

f=FootBar('This is a constructor argument')
print(f.somevar)

class A:
    def hello(self):
        print("hello,I'm A")
class B(A):
    pass
a=A()
b=B()
a.hello()
b.hello()
class C(A):
    def hello(self):
        print("Hello I'm C")
c=C()
c.hello()
'''
class bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah')
            self.hungry=False
        else:
            print('No thanks')
class SongBird(bird):
    def __init__(self):
        bird.__init__(self)
        self.sound='Suark'
    def sing(self):
        print(self.sound)
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()
'''
__metaclass__=type
class bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaah')
            self.hungry=False
        else:
            print('No thanks')
class SongBird(bird):
    def __init__(self):
   #     bird.__init__(self)
        super(SongBird,self).__init__()
        self.sound='Suark'
    def sing(self):
        print(self.sound)

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter=0
    def __getitem__(self,index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)
cl=CounterList(range(10))
print (cl)
cl.reverse()
print (cl)
del cl[3:6]
print (cl)
print(cl.counter)
print(cl[4]+cl[2])
print(cl.counter)
'''
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
r=Rectangle()
r.width=10
r.height=5
print(r.getSize())
r.setSize((150,100))
print(r.width)
'''
__metaclass__=type
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)

r=Rectangle()
r.width=10
r.height=5
print(r.getSize())
r.setSize((150,100))
print(r.width)
'''
__metaclass__=type

class MyClass:
    
    def smeth():
        print('This is a static method')
    meth=staticmethod(smeth)
    def cmetch(cls):
        print('This is a class method of',cls)
    cmetch=classmethod(ceth)
'''

__metaclass__=type

class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
MyClass.smeth()
MyClass.cmeth()

class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fibs=Fibs()
for f in fibs:
    if f>1000:
        print(f)
        break

class TestIterator:
    value=0
    def __next__(self):
        self.value+=1
        if self.value>10: raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti=TestIterator()
print(list(ti))
def flatter(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested=[[1,2],[3,4],[5]]
for num in flatter(nested):
    print (num)

print(list(flatter(nested)))

def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
print(list(flatten([[[1],2],3,4,[5,[6,7]],8])))
