#!/usr/bin/env python
# -*- coding: utf-8 -*-

python语法不能识别a++

str()和repr():
链接：
http://www.cnblogs.com/itdyb/p/5046415.html
Python 有办法将任意值转为字符串：将它传入repr() 或str() 函数。
    函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式



如何查看一个模块的在线帮助文档？help?-----用help,只是在win上看不到对应的网页链接，在mac上可以看到
------------------------------------------------------------
一个二维数组，对其中的每个元素转换为大写，并返回一个二维数组？
flist=[['h', 'f', 'e', 'hf', 'e', '5', '7'], ['ge', 'ge'], ['ge', 'h', 'eh'], ['bh', 'h', 'h']]
------------------------------------------------------------
文档内容如下：
"","h","f","","e","hf"
"ge","ge"
"ge","h","eh"
"bh","h","h"
函数处理结果如下：
import linecache
f=linecache.getlines('/Users/captain/desktop/a.txt')
lines=[line[1:-2].split('","') for line in f]
print len(filter(lambda line:line[1].startswith('h'), lines)) 

liness=[line.strip().split(',') for line in f]
print len(filter(lambda line:line[1].startswith('"h'), liness)) 
结果算出来都为3，结果一致，但在作业中不一致，有点奇怪？

------------------------------------------------------------
能识别 a+=1
--------------------
检查参数类型的两种方法？（两个函数作用不一样）
assert type(user_total) == int#断言函数，一般不要放在函数内部，放在函数外面
assert fun1() ==[None, None]
if  isinstance(x, int)#参数类型检查


------------------------------
if else的三元表达式（三个条件的）有没有，如何写？
if else简写成一个三元表达式：
 4 if True else 3
等同与：
if True:
    print 4
else:
    print 3

------------------------------
数组，tuple, string互转
python中列表，元组，字符串如何互相转换
    Python中有三个内建函数：列表，元组和字符串，他们之间的互相转换使用三个函数，str(),tuple()和list(),具体示例如下所示:

>>> s = "xxxxx"
>>> list(s)
['x', 'x', 'x', 'x', 'x']
>>> tuple(s)
('x', 'x', 'x', 'x', 'x')
>>> tuple(list(s))
('x', 'x', 'x', 'x', 'x')
>>> list(tuple(s))
['x', 'x', 'x', 'x', 'x']

列表和元组转换为字符串则必须依靠join函数（前提是：列表和元组内部的元素为字符，而不是整型）

>>> "".join(tuple(s))
'xxxxx'
>>> "".join(list(s))
'xxxxx'
>>> str(tuple(s))
"('x', 'x', 'x', 'x', 'x')"
>>> 

>>> a=(1,2,1,9,7,77,32)
>>> sorted(a)              # 这儿会把一个tuple转换为list
[1, 1, 2, 7, 9, 32, 77]

------------------------------------------------------------------------
python字符串换行的三种方式

#自学python
#coding=utf-8
if __name__ == '__main__':
#第一种：三个单引号
    print ''' 我是一个程序员
        我刚开始学习Python'''
#第二种：三个双引号
    print """ 我是一个程序员
        我刚开始学习python"""
#第三种：\结尾
    print "我是一个程序员，\
-------------------------------------------------------------------------
按照124AaBCc排序：
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_filter=filter(str.isalpha,a)#a_filter为去掉数字后的字符串
print( ''.join( sorted(a_filter,key = lambda x : ord( x.lower( ))*2 + x.islower( ))))#这儿为什么*2有点不明白
--------------------------------------------------------------------------
定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。

import os
def get_text(f):
	a='cat %s'%f   #cat可以获取对应路径文件的内容，如果此路径没有，则会报错；这儿还需要考虑没有此文件的状况，这儿没获取到路径的话，怎么写
	m=os.popen(a).read()
	return m
# print get_text('/Users/captain/desktop/习题.txt')

#优化后
import os
def get_text(f):
	a='cat %s'%f
	# return a #这儿会返回 cat /Users/captain/desktop/a.tt
	if a.startswith('cat'):#拿返回的关键词做判断
		return "your input path can't be found, pls check it"
	else: 
		m=os.popen(a).read()
		return m
print get_text('/Users/captain/desktop/a.tt')

--------------------------------------------------------
可变参数的使用禁忌：
def func(arg):
	arg[0]=5
	return arg
tlist=[1,2,3,4]
print func(tlist)#[5, 2, 3, 4]
print tlist#[5, 2, 3, 4],可以看到全局变量的tlist的值也改变了，这是一个很危险的做法，不建议这样用
>>>
[5, 2, 3, 4]
[5, 2, 3, 4]


arg=1
def fx():
	arg=2
	return arg
print fx()#2
print arg#1,这儿的值没有变，想想和上面的区别

-------------------------------------------------------
>>> map(lambda x: x*x if x%2==1 else pass, [1, 2, 3, 4, 5, 6, 7, 8, 9])
  File "<stdin>", line 1
    map(lambda x: x*x if x%2==1 else pass, [1, 2, 3, 4, 5, 6, 7, 8, 9])
                                        ^
SyntaxError: invalid syntax

>>> map(lambda x: x*x if x%2==1 else None, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, None, 9, None, 25, None, 49, None, 81]

lambda函数如果要不做任何操作的话，应该怎么写？(这儿直接用filter代替map函数即可)
>>> map(lambda x: x*x if x%2==1 else x, [1, 2, 3, 4, 5, 6, 7, 8, 9])# 如果要加if必须配合else使用，else中不做任何操作不能写pass，原样输出用x
[1, 2, 9, 4, 25, 6, 49, 8, 81]

-------------------------------------------------------

popen处理文件后是否需要关闭？？
import os
def get_doc(module):
	a='pydoc %s'%module
	m=os.popen(a).read()
	return m
print get_doc('string')

import os
def get_text(f):
	a='cat %s'%f   #cat可以获取对应路径文件的内容，如果此路径没有，则会报错；这儿还需要考虑没有此文件的状况
	m=os.popen(a).read()
	return m
print get_text('/Users/captain/desktop/习题.txt')

-------------------------------------------------------
Python: 测试函数是否被调用
1	# helper class defined elsewhere
2	class CallLogger(object):
3	   def __init__(self, meth):
4	     self.meth = meth
5	     self.was_called = False
6	 
7	   def __call__(self, code=None):
8	     self.meth()
9	     self.was_called = True
然后assert CallLogger的was_called为True就行了。但是这样的Callable不是个函数：
1	isinstance(object, types.FunctionType) # Callable will be False
对于这种Callable获取参数个数需要用：
1	inspect.getargspec(fn.__call__)
