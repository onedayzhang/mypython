#!/usr/local/bin/python3.6
x=1
while x<=10:
    print(x)
    x+=1

words=['this','is','an','ex','parrot']
for word in words:
    print(word)
numbers=[0,1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number)
print(list(range(0,10)))

d={'x':1,'y':2,'z':3}
for key in d:
    print (key,'corresponds to',d[key])
