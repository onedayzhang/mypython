#!/usr/local/bin/python3.6
#find
print ('With a moo-moo here.and a moo-moo there.'.find('a'))
title="Monty Python's Flying"
print (title.find('Monty'))
print (title.find('Python'))
print (title.find('Hello'))
subject='$$$ Get rich now!!! $$$'
print(subject.find('$$$'))
print(subject.find('$$$',1))
print(subject.find('!!!',0,16))
#join
seq=['1','2','3','4','5']
sep='+'
print(sep.join(seq))
dirs=['','usr','bin','env']
print('/'.join(dirs))
print('C:'+'\\'.join(dirs))
#lower
name='Gumby'
names=['gumby','smith','jones']
print(name.lower())
if name.lower() in names:print('Found it')
#replace
print('This is a test'.replace('is','eez'))
#split
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
#不提供分隔符,程序会把所有空格当成分隔符
print('Using the default'.split())
#strip 去除两侧(不包括内部)空格的字符串

print('        internal whitespace is kept  '.strip())

name='gumby '
names=['gumby','smith','jones']
print(name.lower())
if name.strip() in names:print('Found it')

print('***SPAM*for*everyone!!!***'.strip('*'))
#translate
table=str.maketrans('cs','kz')
print('this is an incredible test'.translate(table))
