#!/usr/local/bin/python3.6
#字符串都是不可变的，分片赋值不合法

#字符串格式化
format="Hell.%s.%s.enough for ya?"
values=('world','Hot')
print(format%values)

format="pi is :%.3f"
from math import pi
print (format%pi)

print ('Price of eggs: $%d' % 42)
print ('Price of eggs: $%x' % 42)

from math import pi
print ('pi is %f'%pi)
#字段宽度和精度
print ('%10f'%pi)
print ('%10.2f'%pi)
print ('%.2f'%pi)
print ('%.5s'%'Guido van Rossum')
print ('%.*s'%(5,'Guido van Rossum'))

