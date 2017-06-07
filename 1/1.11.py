#!/usr/local/bin/python3.6
#py3的print需要加括号了
x="Hello."
y="world!"
print (x+y)

print (str("hello.worild"))
print (repr(x+y))
temp=42
print ("The temperature is " +repr(temp))

print ('''this is a very very long string.
it continues here
and it's not over yet
"hello.world"
still here.''')
print ('hello\nworld')
#原始字符
print (r'C:\Program Files\fnord\foo\bar')
print (r"let\'s go")
#Unicode字符串
print (u'Hello.world')
