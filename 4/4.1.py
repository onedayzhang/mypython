#!/usr/local/bin/python3.6
names=['Alice','Beth','Cecil','Dee-Dee','Earl']
numbers=['2341','9102','3158','0142','5551']
print(numbers[names.index('Cecil')])

#4.2
phonebook={'Alice':'2341','Beth':'9102','Cecil':'3258'}

#4.2.1 dict
items=[('name','Gumby'),('age',42)]
d=dict(items)
print(d)
print(d['name'])

d=dict(name='Gumby',age=42)
print(d)

x={}
x[42]='foobar'
print(x)
#4.2.3
phonebook={'Alice':'2341','Beth':'9102','Cecil':'3258'}
print(phonebook)
print("cecil's phone number is %(Cecil)s"%phonebook)

template='''<html>
<head><titile>%(title)s</title></head>
<body>
<hl>%(title)s</hl>
<p>%(text)s</p>
</body>'''
data={'title':'My Home Page','text':'Welcom to my home page!'}
print(template%data)
#4.2.4字典方法
#clear
d={}
d['name']='Gumby'
d['age']=42
print(d)
returned_value=d.clear()
print(returned_value)
#copy
#浅拷贝 替换值，原始字典不受影响，修改值会影响
x={'username':'admin','machines':['foo','bar','baz']}
y=x.copy()
y['username']='mlh'
y['machines'].remove('bar')
print(y)
print(x)
#深拷贝

from copy import deepcopy
d={}
d['name']=['Alfred','Bertrand']
c=d.copy()
dc=deepcopy(d)
d['name'].append('Clive')
print(c)
print(dc)
#fromkeys
print({}.fromkeys(['name','age']))
#python 3.x不一样
print(dict.fromkeys(['name','age']),'(unknown)')

#get
d={}
print(d.get('name'))
print(d.get('name','N/A'))
d['name']='Eric'
print(d.get('name'))
#has_key python 3.0没有

#items 和iteritems(python3.0没有)
d={'title':'Python Web Site','url':'http://www.python.org','spam':0}
print(d.items())

print(d.keys())
#pop
d={'x':1,'y':2}
print(d.pop('x'))
print(d)
#popitem
d={'title':'Python Web Site','url':'http://www.python.org','spam':0}
print(d.popitem())
print(d)
#setdefault
d={}
print(d.setdefault('name','N/A'))
print(d)
d['name']='Gumby'
print(d.setdefault('name','N/A'))
print(d)
d={}
print(d.setdefault('name'))
#update
d={
    'title':'Python web stie',
    'url':'http://www.python.org',
    'changed':'Mar 14 22:09:15 MET 2008'
    }
x={'title':'Python Language Website'}
d.update(x)
print(d)
#values itervalues
d={}
d[1]=1
d[2]=2
d[3]=3
d[4]=1
print(d.values())
