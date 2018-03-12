#!/usr/bin/env python
# -*- coding: utf-8 -*-


无涯python网址： http://www.cnblogs.com/weke/category/831885.html
python标识
#!/usr/bin/env python

含有中文的python头部标识
#!/usr/bin/env python
# -*- coding: utf-8 -*-
退出python环境：
Use exit() or Ctrl-D (i.e. EOF) to exit

占位符：print('What is your {0}? It is {1}.'.format('q', 'a'))
# What is your q? It is a.

python清屏 //针对windows,mac下试试把cls改为clear
import os
os.system('cls')


python py文件中执行另一个py文件
最简单的方法：
import os
os.system("python filename")
filename最好是全路径+文件名；

其他方法：
execfile('xx.py')，括号内为py文件路径；
如果需要传参数，就用os.system()那种方法；
如果还想获得这个文件的输出，那就得用os.popen（）；

判断s是否为unicode:
isinstance(s, unicode)


多个元素赋值：
>>> a,b,c=1,2,3
>>> a
1
>>> b
2
>>> c
3
>>> a,b,c=[3,52,6]
>>> a
3
>>> b
52
>>> c
6
a,b,c="str","str1",4
a,b,c=("str","str1",4)


单行注释#
多行注释:三个双引号
"""
……………………
"""

同一行显示多条语句
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
#!/usr/bin/python
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

导入模块
import test  #导入testy.py
反斜杠\，换号的链接字符

查看python变量的类型
type(a)
查看id标识符
id(a)



删除变量
del a 
联合删除变量；
del a,b,c   删除对象的引用
del a[:]    清空列表对象里的元素

三个常用内置函数type,help,dir
type(b)
help(time)   help(time.sleep)  查看对应模块的用法
dir(time)    查看time模块中有哪些可以用的方法
id(a)            查看变量a的内存id

查看python版本
python -V(大写的V)

赋bool值，需要大写
a=True

常用基本数据类型.
int 整型，可以写成16进制，0x开头
浮点数，即小数，用1.23e9表示1.23x10^9
boolean 布尔
string  字符串
list 列表
tuple 元组
dict 字典

数据类型的可变和不可变
不可变类型：int，string， tuple //（字符串不能修改）
可变类型:list,dict

print "The quick brown fox","jumps over","the lazy dog"[遇到逗号会输出一个空格]

提示用户输入：name=raw_input()

python对大小写敏感，严格执行缩进

python中，通常用全部大写的变量名表示常量  PI=3.141592653

区别：ASCII编码是1个字节，而Unicode编码通常是2个字节，UTF-8是综合两种方式
ASCII----python------Unicode----------UTF-8

list和tuple是Python内置的有序集合，一个可变，一个不可变。

list可以转换字符串，tuple，直接生成一个列表,如果参数为空，则返回一个空的列表
list转换为字符串用 ''.join()
>>> a="this"
>>> list(a)
['t', 'h', 'i', 's']

>>> list((1,3))
[1, 3]


range:直接生成列表对象
xrange:生成xrange对象，可以省内存（生成器）
for m in range(1000):#内存中会生成0-999
    if m == 10:
      print 'sss'
      break
for m in xrange(1000):#内存中会生成0-10
    if m == 10:
      print 'sss'
      break

列表生成器：
生成字符串：['the %s' % d for d in xrange(10)]
生成元组：[(x,y) for x in range(2) for y in range(2)]
生成一个字典：dict([(x,y) for x in range(3) for y in range(2)])  #前面作为键，后面作为值

eg:用两种方法生成100内的大于20的偶数
用列表推导式：
>>> [x for x in range(21,100) if x%2==0]
用过滤器
>>> def odd(n):
...     return n%2==0
...
>>> filter(odd, range(21,100))

生成包含1到10的所有奇数列表。
>>>range(1,11,2)
或：
>>>[x for x in range(1,11) if x % 2 == 1]  //取余

生成字符串：
>>> ['%s love python' % s for s in range(1,10) if s%2==1]
['1 love python', '3 love python', '5 love python', '7 love python', '9 love python']


-----------------------------------------------------------------

list和dict的互转：
>>> a=[(1,2),(3,4),(5,6)] //数组内需要是tuple
>>> dict(a)
{1: 2, 3: 4, 5: 6}

>>> b={1: 2, 3: 4, 5: 6}
>>> list(b)
[1, 3, 5]//只取了字典前面的key


-------------------------------------------------

排序翻转：sort,reverse
a = [33,11,22,44]
这个方式直接修改原列表。他的返回值为none，
所以b = a.sort()，print b 输出的内容是None

list的reverse函数：反转一个list, 他的返回值为none
比如上面的列表ab = a. reverse()， print b 输出的内容是None

>>> a = [33,11,22,44]
>>> b=a.sort()
>>> a
[11, 22, 33, 44]
>>> b   #b为空
>>> if b is None:
...     print "the content is null"
...
the content is null


>>> c=a.reverse()
>>> c
>>> a
[44, 33, 22, 11]

-------------------------------------
r"\n"
不转义(前面标识r,就不转义)

u"哈哈哈"
转义


占位符：

>>> a='jay'
>>> b='python'
>>> print "my name is %s, I love %s." % (a,b)
my name is jay, I love python.


占位符的三种用法：
>>> "this is %s %s." %("my", "apple")
'this is my apple.'

>>> "this is {} {}" .format ("my", "apple")
'this is my apple'
>>> "this is {1} {0}" .format ("apple", "my") //可以不按照顺序来,括号的1，0表示位置
'this is my apple'

>>> "this is {whose} {fruit}" .format (fruit="apple", whose="my")//这种很有优势，优先
'this is my apple'


字典占位符
>>> "this is %(whose)s %(fruit)s" % {"whose":"my","fruit":"apple"}
'this is my apple'




bin()可以直接转换10进制位二进制
>>> bin(2)
'0b10'

int(0bxx)可以将二进制转换为十进制
>>> int(0b0110)
6


下面为二进制运算
1.难缠符号之一	 >> <<	 位移
2.难缠符号之二 	&	 按位与
3.难缠符号之三	 | 	按位或
4.难缠符号之四	 ^	按位异或
5.难缠符号之五 		按位取反

位移的应用
• 判断奇偶数（其实是判定其二进制的末尾为0还是1）
>>> 5&1
1        //结果为1，表示为奇数
>>> 6&1
0       //结果为0，表示为奇数
• 判别文件的的大小（ls-al会列出文件的字节数，然后按照2^10=1024，转换为KB,MB）
>>> 197121 >>10
192

% 	得余数
/	得商

应用：
>>> [x for x in xrange(4)]
[0, 1, 2, 3]

>>> [(2*(x/2)>>0, 2*(x%2)) for x in xrange(4)]
[(0, 0), (0, 2), (2, 0), (2, 2)]

>>> [((x>>1)<<1, (x & 1)<<1) for x in xrange(4)]
[(0, 0), (0, 2), (2, 0), (2, 2)]


字典按key的排序输出：
（note:字典的key是唯一的，value不是唯一的；一个值可以对应n个键）
可以把keys或者values生成一个list,然后sort(), 再dict[key]就可以求出对应的value
d = {'a': 1, 'f':2, 'b': 6, 'c': 3}
keylist=d.keys()
keylist.sort()
for x in keylist:
	print x, d[x]
>>>
a 1
b 6
c 3
f 2

如果要通过value来取key呢，没有内置方法--->用迭代，穷举
d = {'a': 3, 'f':2, 'b': 6, 'c': 3, 'e':5, 'g':3}
def search(sth):
	keylist=[]
	for x, y in d.items():
		if y==sth:
			keylist.append(x)
	print keylist
search(3)
>>>
['a', 'c', 'g']


print中逗号的用法：
print 2
print 4

print 2,
print 4
输出的结果：
>>>
2
4
2 4      //可以看到逗号把文件变成一行了，没有逗号是两行；这个特性可以用到写入文件中（重定向）

如下：对文件进行写入：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
f=open.('print.txt', 'w')
print >>f,"hahhahhaha",     #>>位移符号就是重定向，对文件写入后面的字符，逗号可以把两行字符变成一行
print >>f,"xixixixixixi"
f.close()


is：检查共享，判断两个是不是一个类型，一个类型则返回True, 不是一个类型则返回False
>>> True is True
True
>>> False is True
False
>>> 5 is True
False
>>> "2333" is True
False


if else简写成一个三元表达式：
4 if True else 3

if True:
    print 4
else:
    print 3


活用list,[假的答案，真的答案][条件]
>>> [4,3][True]
3
>>> [4,3][False]
4

continue和break的区别：
x=1
while True:
	x+=1
	print x
	continue  #结束单次循环,下面的语句就执行不到了,
	if x>20:
		break	#结束整个循环，python语言中有case...break

else不能和break合用；else只能当前面的程序正常执行完之后，才能用
（如下程序不能输出else中end这个值）
x=1
while True:
	x+=1
	print x
	if x>5:
		break	#结束整个循环，python语言中没有cas...break
else:
	print 'end'

>>>
2
3
4
5
6

可以与continue合用
x=1
while x<5:
	x+=1
	print x
	continue  #结束单次循环,下面的语句就执行不到了,
else:
	print 'end'

>>>
2
3
4
5
end


--------------------------

virtualenv的使用(python的沙盒)

sudo pip install virtualenv(安装沙盒)
virtualenv test1(创建沙盒test1)
cd test1
source bin/activate
pip install tornado

推荐参考书
a.程序员的数学
b.大话数据结构（大话设计模式）
c.c语言
d.python的标准库
e.python的基础教程
f.docs.python.org(官方文档)
g.啄木鸟社区的邮件列表


# 输出定义函数的名字： 
# print func_name()
def fun1():
	print 3333
	#return none #如果不写return，就会默认执行这一句

a=(1,2,3,4)#tuple与list一样，都是可以迭代的
for x in a:
	print x
b=[1,2,3,4]
for y in b:
	print y

>>> a = {1: 'a', 2: 'e', 3: 'b', 6: 'f'}
>>> max(a)#取max只取了前面的key
6

怎么去学习使用函数
	（1）别管那么多复杂的，先直接把功能实现了。不要将问题复杂化，越简单越好。
	（2）抽象成函数：命名规范，伪代码,参数默认值。
	（3）将函数变得更健壮，让它可以跑很多地方
		1.假设你写的函数是要交给你的基友用 -》 功能完整
		2.假设你写的函数是要交给你的学弟用 -》 异常处理完善
	 (4) 测试
		1.assert
		2.对函数的返回进行一个值和类型的测试。
		3.单元测试
函数中为什么要用默认值：
1.更省事
2.更可配置

函数命名：
下划线命名线  get_doc
驼峰命名法 getDocFromUrl（即：下一个单词首字母大写）


Python提供了__future__模块，把新版本3.x的特性导入到当前版本2.x
>>> from __future__ import division
>>> 10/3  #在3.x中都是精确除法
3.3333333333333335 #地板除用//
>>> 10//3
3


获取对象的信息：
type(obj)
isinstance(obj,type) 类型断言

assert xx==xxx 断言

dir(obj) 查看属性

getattr(obj, property, 出错值)
setattr(obj, property, value)
hasattr(obj, property)

