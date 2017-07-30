#!/usr/local/bin/python3.6
f=open('somefile.txt','w')
f.write('Hello,')
f.write('world!')
f.close()

f=open('somefile.txt','r')
print(f.read(4))
print(f.read())
f.seek(0)
print(f.read())

f=open(r'test.txt')
print(f.read(7))
print(f.read(4))
f.close()
f=open(r'test.txt')
print(f.read())
f.close()
f=open(r'test.txt')
for i in range(3):
    print(str(i)+':'+f.readline())
f.close()

def process(string):
    print('Processing;',string)
'''
f=open(r'test.txt')
char=f.read(1)
while char:
    process(char)
    char=f.read(1)
f.close()
'''
import fileinput
for line in fileinput.input("test.txt"):
    process(line)
