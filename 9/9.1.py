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
        super(CounterList,self).__init(*args)
        self.counter=0
    def __getitem__(self,index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)

