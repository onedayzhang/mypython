#!/usr/local/bin/python3.6
print (list('hello'))

#2.3.2
x=[1,1,1]
x[1]=2
print(x)

names=['Alice','Betch','Cecil']
del names[2]
print (names)

name=list('perl')
print (name)
name[2:]=list('ar')
print (name)

name=list('perl')
name[1:]=list('ython')
print (name)

num=[1,5]
num[1:1]=[2,3,4]
print (num)

num[1:4]=[]
print (num)

#2.3.3
lst=[1,2,3]
lst.append(4)
print (lst)
y=['to','be','not','to','be']
print(y.count('to'))

x=[[1,2],1,1,[2,1,[1,2]]]
print (x.count(1))
print (x.count([1,2]))

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print (a)

a=[1,2,3]
b=[4,5,6]
a[len(a):]=b
print (a)
knights =['we','are','the','knights','who','say','ni']
print (knights.index('who'))
print (knights[4])

nums=[1,2,3,5,6,7]
nums.insert(3,'four')
print (nums)

nums=[1,2,3,5,6,7]
nums[3:3]=['four']
print (nums)

x=[1,2,3]
print(x.pop())
print (x)
print (x.pop(0))
print (x)

x=[1,2,3]
x.append(x.pop())
print (x)

y=['to','be','not','to','be']
y.remove('be')
print (y);

x=[1,2,3]
x.reverse()
print (x)

x=[4,6,2,1,7,9]
x.sort()
print (x)


x=[4,6,2,1,7,9]
y=x[:]
y.sort()
print (y)
print (x)


x=[4,6,2,1,7,9]
y=sorted(x)
print (y)
print (x)

print (sorted('Python'))
#python3.x没有cmp函数了
#print (cmp(42,32))

#sort key reverse
x=['fefasdf','gergfg','df','geg']
x.sort(key=len)
print (x)

x=[4,6,9,2,1,7]
x.sort(reverse=True)
print (x)
