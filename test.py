#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 修复文件的编码错误：
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print calc([1, 2, 3])


# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print calc(1, 2, 3)

# nums = [1, 2, 3]
# print calc(nums[0], nums[1], nums[2])
# print calc(*nums)

# def person(name, age, **kw):
#     print 'name:', name, 'age:', age, 'other:', kw

# person('Bob', 35, city='Beijing')

# kw = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=kw['city'], job=kw['job'])
# person('Jack', 24, **kw)

# def func(a, b, c=0, *args, **kw):
#     print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

# func(1, 2)
# func(1, 2, c=3)
# func(1, 2, 3, 5, 6, x=3, y=3, Z=9)
# func(1, 2, 3, 'a','b','c',x=3, y=3)
# args = (1, 2, 3, 4)
# kw = {'x': 99}
# func(*args, **kw)

# def func(a, *kw):
#     print 'a =', a,'args =', kw

# func(1, 2, 3, 5, 6, 7)
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# print fact(100)


# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

# print fact(1000)


# L=[]
# n=1
# while n<=99:
# 	L.append(n)
# 	n=n+2


# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# r=[]
# n=3
# for i in range(n):
# 	r.append(L[i])
# print r

# print L[0:3]
# print L[:3]
# print L[2]
# print L[-1]
# print L[-2:-1]

# L=range(100)
# print L[:10]
# print L[-10:]
# print L[10:20]
# print L[:10:2]  #前10个数，每两个取一个
# print L[::5]  #所有数，每5个取一个：
# print L[:]   #只写[:]就可以原样复制一个lis

# T=(0, 1, 2, 3, 4, 5)
# print T[:3]

# L=[10,20,30,50,60]
# sum=0
# for x in L:
# 	sum=sum+x
# 	print x
# print sum

# d = {'a': 1, 'b': 2, 'c': 3}
# for s in d:		#打印key
# 	print s

# for value in d.itervalues():	#打印value
# 	print value

# for k, v in d.iteritems():		#打印key和value
# 	print k, ':', v	


# for ch in 'ABC':
# 	print ch

# for i, value in enumerate(['A', 'B', 'C']):	#带有下标的liste循环
#  	print i, value

# for x, y in [(1, 1), (2, 4), (3, 9)]:	#引入两个变量
# 	print x, y

# L=[]
# for x in range(1, 11):
# 	L.append(x+3)
# print L

# L=[x*x for x in range(1, 11)]
# print L

#筛选仅出偶数的平方
# print [x * x for x in range(1, 11) if x % 2 == 0]
#两层循环
# print [m + n for m in 'ABC' for n in 'XYZ']

# import os	#导入OS模块
# print [d for d in os.listdir('.')]	#os.listdir可以列出当前目录下所有的文件和目录

#打印生成器里面的内容
# g = (x * x for x in range(10))
# for n in g:
# 	print n

#斐波拉契数列generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
# fib(6)

# def odd():
# 	print 'step 1'
#     yield 1
#     print 'step 2'
#     yield 3
#     print 'step 3'
#     yield 5
# o = odd()


# def str2int(s):
# 	def fn(x, y):
# 		return x * 10 + y
# 	def char2num(s):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# 	return reduce(fn, map(char2num, s))
# print str2int('13689')

# def fn(x, y):
#     return x * 10 + y
# def char2num(s):
#           #用字典中的key-value来确认返回值
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     #也可以用这个内置函数
#     # return int(s)
# print map(char2num,'13579')#结果是：[1, 3, 5, 7, 9]
# print reduce(fn, map(char2num,'13579'))

# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# def str2int(s):
#     return reduce(lambda x,y: x*10+y, map(char2num, s))
# print str2int('833654')
# filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 一个list中，删掉偶数，只保留奇数，可以这么写：
# def is_odd(n):
#     return n % 2 == 1
# print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# print map(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


# 不懂
# def not_empty(s):
#     return s and s.strip()
# print map(not_empty, ['A', '', 'B', None, 'C', '  '])
# print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
# print sorted([36, 5, 12, 9, 21], reversed_cmp)

# def cmp_ignore_case(s1, s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1 < u2:
#         return -1
#     if u1 > u2:
#         return 1
#     return 0
# print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


# def sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
# print sum(1, 3, 5, 7, 9)

#下面返回了函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# print f()
# print lazy_sum(1, 3, 5, 7, 9)  这种输出是错误的，返回：<function sum at 0x1056fb488>


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()
# f1=count()[0]
# print f1(),f2(),f3()
#虽然输出是个数组，但是下面如此的打印输出会报错
# a = count()
# print a
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         fs.append(f(i))
#     return fs
# f1, f2, f3 = count()
# print f1(),f2(),f3()

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# print count()

# def now():
# 	# print '2013-12-5'
# 	print 'this'
# 	return
# f=now
# print f()


# def int2(x, base=2):
#     return int(x, base)
# # print int2('10')
# print int2('10', 10)

# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def f():
# 			return i*i
# 		fs.append(f)
# 	return fs

# # f1, f2, f3 = count()
# # print f1()
# # print f2()
# # print f3()
# a,b,c=count()
# print a(),b(),c()

# def count():
# 　　fs = []
# 　　for i in range(1,4):
# 　　　　def f(j):
# 　　　　　　def g():
# 　　　　　　　　return j*j
# 　　　　　　return g
# 　　　　fs.append(f(i)) 
# 　　return fs

# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def f(j):
# 			def g():
# 				return j*j
# 			return g
# 		fs.append(f(i))
# 	return fs
# f1, f2, f3 =count()
# print f1()
# print f2()
# print f3()

# def calc_prod(lst):
#     def lazy_prod():
#         def f(x, y):
#             return x * y
#         return reduce(f, lst, 1)
#     return lazy_prod
# f = calc_prod([1, 2, 3, 4])
# print f()

# def now():
# 	print'2013-13-5'
# print now()

# import functools
# max2=functools.partial(max, 10)
# print max2(5,6,7)

# def int2(x, base=2):
# 	return int(x, base)
# print int2('1010')

# import functools
# int2=functools.partial(int, base=2)
# print int2('1011')


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ' a test module '

# __author__ = 'Michael Liao'

# import sys

# def test():
#     args = sys.argv
#     if len(args)==1:
#         print 'Hello, world!'
#     elif len(args)==2:
#         print 'Hello, %s!' % args[1]
#     else:
#         print 'Too many arguments!'

# if __name__=='__main__':
#     test()

# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print '%s: %s' % (self.name, self.score)

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()       

# a=[(1,2,5,6),(2,1,4,5),(6,7,3,5),(3,1,3,3),(3,5,2,7)]
# a=[('a', {'3': 3}), ('g', {'3': 4}), ('f', {'De': 5}), ('c', {'a': 1}), ('d', {'Af': 0})]
# # a=[(1,2,3),(2,1,4),(6,1,3),(3,5,3)]
# import operator
# a.sort(key=operator.itemgetter(1))
# print a


# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b=a.upper()
# i=0
# c=[]
# while i<len(a):
# 	if a[i]>b[i]:
# 		c.append(a[i].upper())
# 	else:
# 		c.append(a[i].lower())
# 	i+=1
# a=''.join(c)
# print a
# #1.2
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# i=0
# c=[]
# while i<len(a):
# 	if a[i].lower()==a[i].upper():
# 		c.append(a[i])
# 	i+=1
# print ''.join(c)

# a = "aAsmr3idd4bgs7Dlsf9eAF"
# c=a.upper()
# b =''.join(list(set(c)))
# i=0
# j=0
# n=0
# d={}
# while i<len(b):
# 	while j<len(a):
# 		if b[i]==c[j]:
# 			d[b[i]]=n+1
# 		j=j+1
# 	i=i+1
# print d

# >>> a='17854113534'#正确：转为list后，去重成新的list, 顺序按照老的list排序
# >>> b=list(a)
# >>> c=list(set(b))
# >>> c.sort(key=b.index)
# >>> c
# ['1', '7', '8', '5', '4', '3']
# >>> 

# >>> ''.join(['a', 'b', 'c', 'd'])
# 'abcd'
# a='abcbbcada'
# b=list(set(a))
# # >>> b
# # ['a', 'c', 'b', 'd']
# # >>> b.sort(key=a.index)#可以按照a中的字符串顺序排序
# # >>> b
# # ['a', 'b', 'c', 'd']

# c=''.join(b.sort(key=a.index)) 
# print c


# a = "aAsmr3idd4bgs7Dlsf9eAF"
# a_filter=filter(str.isalpha,a)#a_filter为去掉数字后的字符串
# print( ''.join( sorted(a_filter,key = lambda x : ord( x.lower( ))*2 + x.islower( ))))#这

# a = "aAsmr3idd4bgs7Dlsf9eAF"

# #1.1
# print a.swapcase()

# #1.2
# print ''.join(s for s in a if s.isdigit())

# #1.3
# print dict([(x, a.count(x)) for x in set(a)])

# #1.4
# a_short=list(set(a))
# a_short.sort(key=a.index)
# print ''.join(a_short)

# a = "aAsmr3idd4bgs7Dlsf9eAF"
# print ''.join(sorted(set(a), key=lambda x: a.index(x)))
# # print ''.join(set(a).sort(key=a.index))
# print ''.join(list(set(a)).sort(key=lambda x: a.index(x)))
# # print ''.join(sorted(set(a), key=a.index))
# #1.5
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# i=0
# c=[]
# while i<len(a):
# 	c.append(a[len(a)-1-i])
# 	i=i+1
# print ''.join(c)
# #或者 
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# print a[::-1] #把步长设置为-1即可



# import string
# a='Aab3IDd4Bfs'
# a=''.join([x for x in a if not x.isdigit()])
# print sorted(a ,key=string.upper)#这儿是一个隐性的大写 
# #上面隐性的大写方法与下面的类似（下面为一个实性的大写）
# a=[string.upper(x) for x in a]#string.upper(x）效果等同 x.upper()
# print sorted(a)

# #翻译表：（注意与replace的区别）
# # translate()方法语法：str.translate(table[, deletechars]);
# import string#目的在于引用maketrans这个函数
# a='12345321'
# g = string.maketrans('123','abc')#构建一个翻译表，
# h = string.maketrans('','')#这个就构成了一个不需要翻译的表
# print a.translate(g)
# print a.translate(g,'12')#删除字符串中所有的字符‘1’，‘2’,然后再执行翻译操作
# print a.translate(h,'12')#删除字符'1','2',然后进行不翻译操作
# print a.replace('123','abc')#这个与翻译表的区别是：这个是一块一块的替换，翻译表是对应字符

# g=open('a.txt', 'w')
# g.write('hahhhah')
# g.close()
# #然后运行这个py文件，再打开生成的txt文件即可看到输出结果
# #以上用with代替：
# with open('a.txt', 'a') as g:#这儿‘a’的作用相当于“appnend”在文最后面进行追加
# 	g.write('xixi')#括号内为追加的内容
# #然后运行这个py文件，再打开生成的txt文件即可看到输出结果

# import string
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# b=''.join([x for x in a if not x.isdigit()])
# print ''.join(sorted(b, key=string.upper))

# d = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
# # b=ainfo.keys()
# # b.sort()
# # for x in ainfo:
# # 	print (x, ainfo[x])
# def search(sth):
# 	keylist=[]
# 	for x, y in d.items():
# 		if y==sth:
# 			keylist.append(x)
# 	print keylist
# search('haha')

# def test():
# 	'''
# 	this is test doc
# 	'''
# 	print "this is "
# test()
# print test.__doc__
# # test.__doc__


# def power(x,n):
# 	s=1
# 	m=n
# 	while n>0:
# 		s=s*x
# 		n=n-1
# 	print "%s^%s=%s"%(x,m,s)
# 	# return s
# power(4,4)
# power(5,7)

# def enroll(name, gender, age=6, city='Beijing'):
#     print 'name:', name
#     print 'gender:', gender
#     print 'age:', age
#     print 'city:', city



# # 下面为与默认参数不一致的情况：
# enroll('Bob', 'M', 7)
# enroll('Adam', 'M', city='Tianjin')

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print calc([1, 2, 3])


# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print calc(1, 3, 5, 7)
# nums = [1, 2, 3]
# print calc(nums[0], nums[1], nums[2])
# print calc(*nums)


# def person(name, age, **kw):
#     print 'name:', name, 'age:', age, 'other:', kw
# # person('Bob', 35, city='Beijing')

# kw = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=kw['city'], job=kw['job'])
# person('Jack', 24, **kw)

# # 1
# def max3(a,b,c):
# 	return max(max(a,b),c)
# a = 123
# b = 345
# c = 444
# print max3(a,b,c)
# #简单方法直接用内置函数print max(a,b,c)
# print max(a,b,c)

# 2.1
# def ainfo(x,y,z):
# 	# # return x,y,z
# 	# a=x.value()
# 	# b=y.value()
# 	# c=z.value()
# 	#或者
# 	#return [x,y,z]
# print ainfo(x=88,y=22,z=44)




 
# import os
 
# '''
# Get all the content of the file of the specified text file.
 
# Input: filename - the filename of the text file 
# Return: content - string. all the content of filename. 
#         If the filename not a valid regular file, then return None, and error information is printed.
# '''
# def get_text_file(filename):
#     if not os.path.exists(filename):
#         print("ERROR: file not exit: %s" % (filename))
#         return None
 
#     if not os.path.isfile(filename):
#         print("ERROR: %s not a filename." % (filename))
#         return None
 
#     f = open(filename, "r")
#     content = f.read()
#     f.close()
 
#     return content



# NO.1：
# count = len(open(filepath,'rU').readlines())
# print count
# 或者
# count = -1
# for count, line in enumerate(open('/Users/captain/desktop/twitter.txt', 'rU')):
#     pass
# count += 1
# print count

# NO.2
# import linecache
# print linecache.getline('/Users/captain/desktop/twitter.txt',1)
# 或者
# content_li=open('/Users/captain/desktop/twitter.txt','rU').readlines()
# for x in content_li:
# 	print 'uid=%s'% x.split(',')[1] ,

# No.3

# d=open ('/Users/captain/desktop/name.txt', 'w')  
# d.write("this is my iphone!\nenheng, python is easy and good\nwe should study hard\n")
# d.close()

# d=open('/Users/captain/desktop/name.txt','rU')
# d.seek(0)
# li=d.readlines()
# print li


# import linecache
# # print linecache.getline('name.txt',1)#1行1行读
# print linecache.getline('name.txt',2)
# # print linecache.getline('name.txt',3)
# print linecache.getlines('name.txt')#全部读出来


# import linecache
# import time

# now = time.time() #代码开始时间


# # 前期准备，整理数据
# data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')


# keys = {data_keys[k]:k for k in xrange(0,len(data_keys))}

# f = linecache.getlines('/Users/captain/desktop/t.txt')
# print len(f)

# lines = [x.split('","') for x in f] #拆分



# users = set([line[keys['username']] for line in lines])

# user_total = len(set(users))

# assert type(user_total) == int
# print user_total

# list矩阵的运用（二维数组）
# keys={'a':0, 'b':1, 'c':2}
# all=['1,2,3','4,5,6','7,8,9']
# lines=[x.split(',') for x in all]
# print lines
# print [line[keys['c']] for line in lines]


# # 输出定义函数的名字： 
# # print func_name()

# def fun1():
# 	print 3333
# 	#return none #如果不写return，就会默认执行这一句


# def add(num):#参数是一个list
# 	d = 0
# 	for i in num:
# 		d += i
# 	return d
# print add (range(100))

# def add(*num):#参数是一个tuple
# 	d = 0
# 	for i in num:
# 		d += i
# 	return d
# print add(1,2,3,4,5)

# def add(num1 ,num2):
# 	if isinstance(num1,int) and isinstance(num2, int):#对参数进行检查，容错，可以保证函数的健壮性
# 		return num1+num2
# 	else:
# 		return '参数里有不是数字的类型'
# print add('a',(1,2,3))

# 函数的健壮性

# 1.你永远知道你的方法会返回什么（异常处理，条件判断）
# 2.返回你想要的结果


# a=(1,2,3,4)#tuple与list一样，都是可以迭代的
# for x in a:
# 	print x
# b=[1,2,3,4]
# for y in b:
# 	print y

# >>> a = {1: 'a', 2: 'e', 3: 'b', 6: 'f'}
# >>> max(a)#取max只取了前面的key
# 6

# a=(1,2,3,4)#tuple与list一样，都是可以迭代的
# for x in a:
# 	print x
# b=[1,2,3,4]
# for y in b:
# 	print y

# # 输出定义函数的名字： 
# # print func_name()
# def fun1():
# 	print 3333
# #return none #如果不写return，就会默认执行这一句


# def get_doc(x):
# 	import x
# 	# file=help(module)
# 	return help(x)
# print get_doc('string')

# 在Python中有很多很好的工具来生成字符串文档(docstring)，比如说: epydoc、doxygen、sphinx，但始终觉得pydoc还是不错的工具，用法非常简单，功能也算不错，本文主要介绍pydoc.
# pydoc是Python自带的模块，主要用于从python模块中自动生成文档，这些文档可以基于文本呈现的、也可以生成WEB 页面的，还可以在服务器上以浏览器的方式呈现！

# import os
# def get_doc(module):
# 	a='pydoc %s'%module#打印对应模块的文档
# 	m=os.popen(a).read()
# 	return m
# # print get_doc('string')
# print get_doc('linecache')

# #优化后
# import os
# def get_text(f):
# 	a='cat %s'%f
# 	# return a #这儿会返回 cat /Users/captain/desktop/a.tt
# 	if a.startswith('cat'):#拿返回的关键词做判断
# 		return "your input path can't be found, pls check it"
# 	else: 
# 		m=os.popen(a).read()
# 		return m
# print get_text('/Users/captain/desktop/a.tt')

# import glob
# def get_dir(folder):
# 	a='%s/*.*'%folder
# 	temp=glob.glob(a)
# 	if temp==[]:
# 		return "文件夹为空或不存在"
# 	else:
# 		return temp
# print get_dir('/Users/captain/desktop/')

# def func(*num):
# 	for i in num:
# 		if isinstance(i, int):
# 			a=sorted(num)
# 			return 'max=%s, min=%s'%(a[-1],a[0])
# 			# 或者
# 			# a=max(list(num))
# 			# b=min(list(num))
# 			# return 'max=%s, min=%s'%(a,b)
# 		else:
# 			return '输入的参数必须为整型'
# print func(1,3,9,5,66,0)
# print func('a','c')

# def func(*num):
# 	for i in num:
# 		if not isinstance(i, int):
# 			return '输入的参数必须为整型'	
# 	a=max(list(num))
# 	b=min(list(num))
# 	return 'max=%s, min=%s'%(a,b)
# 	# 或者
# 	# a=sorted(num)
# 	# return 'max=%s, min=%s'%(a[-1],a[0])			
# print func(1,3,9,5,66,0)			
# print func('a',3)
# print func(3,'c')

# def func(*istring):
# 	for i in istring:
# 		if not isinstance(i, str):
# 			return '输入的参数必须为多个字符串内型'
# 	#这儿只能针对字符串长度不一样的字符
# 	# d=dict([(len(i), i)for i in istring])
# 	# return 'istring_max=%s,istring_min=%s'%(d[max(d)],d[min(d)])
	
# 	#下面针对有多个相同长度的字符串做优化
# 	d=dict([(i, len(i))for i in istring])
# 	s=sorted(d.items(), key=lambda x:x[1])
# 	#遍历字符串list中长度最短和最长的元素
# 	minlist=[]
# 	maxlist=[]
# 	# for x, y in d.items():
# 	# 	if y==s[0][1]:
# 	# 		minlist.append(x)
# 	# for x, y in d.items():
# 	# 	if y==s[-1][1]:
# 	# 		maxlist.append(x)
# 	# return 'minlist=%s, maxlist=%s'%(minlist,maxlist)
# 	return 'minlist=%s, maxlist=%s'%(minlist,maxlist)
# print func('abc','a','eegegh','b','ggg','ggeedg', '3')
# print func('1')

# def fun2(*num2):
# 	b=[]
# 	for i in num2:
# 	    if isinstance(i,str):
# 	        b.append(i)
# 	    else:
# 	    	return "输入的参数必须为多个字符串内型"
# 	return "max string is %s" % max(b, key=lambda x:len(x))
# print fun2('abc','a','eegegh','b','ggg','hhh','ggeedg', '3')
# print fun2('1')


# # 因为sy.stdout是一个文件类型，所以定义一个类，继承与object父类，貌似也可以简历一个file对象，
# class TextArea(object):
# 	# 每个类必须的__int__.用于初始化类的内部结构，为类的属性设置默认值
# 	def __int__(self):
# 		self.buffer=[]
# 	#必须要有write方法，因为把sys.stdout接到这边后，print实际上就是调用了一个sys.stdout的wrtie方法
# 	def write(self, *args):
# 		for i in args:
# 			self.buffer.append(i)
# def get_doc(module):
# 	import sys
# 	#更改输出的，好像叫管道
# 	stdout=sys.stdout
# 	sys.stdout=TextArea()
# 	#help中的print出来的就被记录到TextArea()了
# 	help(module)
# 	#还原输入输出，否则后面的都不能正常使用print
# 	text_area, sys.stdout = sys.stdout, stdout
# 	# 取存在text_area.buffer中的，本应该被print的列表
# 	return ''.join([i for i in text_area.buffer])
# # assert type(get_doc(func1)) == str
# assert type(get_doc(help)) == str





# def get_doc(modu):  
#         print modu.__doc__  
# get_doc('string')
# #import time  
# #get_doc(time)  

# class TextArea(object):
# 	def __int__(self):
# 		self.buffer=[]
# 	def write(self, *args):
# 		for i in args:
# 			self.buffer.append(i)

# def get_doc(module):
# 	import sys
# 	stdout=sys.stdout
# 	sys.stdout=TextArea()
# 	help(module)
# 	text_area, sys.stdout = sys.stdout, stdout
# 	return ''.join([i for i in text_area.buffer])

# # assert type(get_doc(func1)) == str
# # assert type(get_doc(help)) == str
# print get_doc('string')



# def get_text(f):
# 	import os#
# 	if os.path.exists(f):
# 		fil=file(f)
# 		ans=fil.read()
# 		fil.close()
# 		return ans
# 	else: return None
# print get_text('/Users/captain/desktop/a.txt')

# def get_dir(folder=None):
# 	import os
# 	import glob
# 	if folder==None:
# 		folder=os.getcwd()
# 	if os.path.isdir(folder):
# 		import glob
# 		return [x.split('\\')[-1] for x in glob.glob('%s\\*.*'%folder)]
# 	else:
# 		return None
# assert type(get_dir())==list
# assert type(get_dir('abc'))==type(None)
# print get_dir('/Users/captain/desktop/')

# arg=1
# def fx():
# 	arg=2
# 	return arg
# print fx()#2
# print arg#1,这儿的值没有变，想想和上面的区别

# global arg
# arg=1
# def fx():
# 	global arg
# 	arg=2
# fx()
# print arg
# >>>2
# def func(arg):
# 	arg[0]=5
# 	return arg

# tlist=[1,2,3,4]
# print func(tlist)
# print tlist

# g= lambda x:[(x, i) for i in xrange(0,4)]
# print g(5)

# g= map(lambda x:[(x, i) for i in xrange(0,4)], xrange(0,3))
# print g

# >>>
# [[(0, 0), (0, 1), (0, 2), (0, 3)], [(1, 0), (1, 1), (1, 2), (1, 3)], [(2, 0), (2, 1), (2, 2), (2, 3)]]



# def fun(*k, **w):
# 	return k, w
# print fun(1,5,7,8,9,[1,4,6,7],{1:2, 3:4})
# print fun(1,5,7,8,9,[1,4,6,7],{1:2, 3:4},a=3,b=4,c=6)#字典和可变量的获取格式不一样

# >>>
# ((1, 5, 7, 8, 9, [1, 4, 6, 7], {1: 2, 3: 4}), {})
# ((1, 5, 7, 8, 9, [1, 4, 6, 7], {1: 2, 3: 4}), {'a': 3, 'c': 6, 'b': 4})


# def fun(*k, **w):
# 	return k, w
# print fun(1,5,7,8,9,[1,4,6,7],{1:2, 3:4})
# print fun(1,5,7,8,9,[1,4,6,7],{1:2, 3:4},a=3,b=4,c=6)

# >>>
# ((1, 5, 7, 8, 9, [1, 4, 6, 7], {1: 2, 3: 4}), {})

#字典和可变量的获取格式不一样




# def fun(*k, **w):
# 	return k, w
# print fun(1,5,7,8,9,[1,4,6,7],{1:2, 3:4})
# print fun(1,5,7,8,9,[1,4,6,7],{1:2, 3:4},a=3,b=4,c=6)#字典和可变量的获取格式不一样
# >>>
# ((1, 5, 7, 8, 9, [1, 4, 6, 7], {1: 2, 3: 4}), {})
# ((1, 5, 7, 8, 9, [1, 4, 6, 7], {1: 2, 3: 4}), {'a': 3, 'c': 6, 'b': 4})


# 递归：
# def func1(i):
# 	if i<100:
# 		return i+func1(i+1)
# 	return i 
# print func1(0)


# import os
# def get_doc(module):
# 	a='pydoc %s'%module
# 	m=os.popen(a).read()
# 	return m
# print get_doc('string')



# def get_text(f):
# 	a=open(f)
# 	re=a.read()
# 	a.close()
# 	return re
# print get_text('/Users/captain/desktop/a.txt')

# # 用with方法
# def get_text(f):
# 	with open(f, 'r') as g:
# 		return g.read()
# print get_text('/Users/captain/desktop/a.txt')

# >>> f = open('/Users/michael/test.txt', 'r')
# >>> f.read()
# 'Hello, world!'
# >>> f.close()
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

# with open('/path/to/file', 'r') as f:
#     print(f.read())

# # 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# # 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：

# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉


# def get_text(f):
# 	with open(f, 'r') as g:
# 		for line in g.readlines():
# 			print line.strip()#strip()是把末尾的'\n'给删掉
# get_text('/Users/captain/desktop/t.txt')


# import os
# def get_text(f):
# 	a='cat %s'%f   #cat可以获取对应路径文件的内容，如果此路径没有，则会报错；这儿还需要考虑没有此文件的状况
# 	m=os.popen(a).read()
# 	m.close()
# 	return m
# print get_text('/Users/captain/desktop/a.txt')
# import os#老师建议把这一句放在函数之外
# def get_text(f):
# 	if os.path.exists(f):
# 		fil=file(f)
# 		ans=fil.read()
# 		fil.close()
# 		return ans
# 	else: return None
# print get_text('/Users/captain/desktop/a.tx')


# import os
# import glob
# def get_dir(folder=None):
# 	import os
# 	import glob
# 	if folder==None:
# 		folder=os.getcwd()
# 	if os.path.isdir(folder):
# 		import glob
# 		return [x.split('\\')[-1] for x in glob.glob('%s\\*.*'%folder)]
# 	else:
# 		return None
# assert type(get_dir())==list
# assert type(get_dir('abc'))==type(None)#老师建议import导入写在函数之外，另外断言的话，不仅要检查类型，还应该检查结果
# print get_dir('/Users/captain/desktop/retest')

# import glob
# def get_dir(d):
#     for i in glob.glob(d+'\*'):
#         return i
# print get_dir('/Users/captain/desktop/retest')

# import glob
# def get_dir(folder):
# 	a='%s/*.*'%folder
# 	temp=glob.glob(a)
# 	if temp==[]:
# 		return "文件夹为空或不存在"
# 	else:
# 		return temp
# print get_dir('/Users/captain/desktop')


# import glob
# def get_dir(folder):
# 	path='%s/*.*'%folder
# 	ff=glob.glob(path)
# 	return ff
# print get_dir('/Users/captain/desktop')
# # print glob.glob(r"/Users/captain/desktop/*.*")

# import glob
# def get_dir(folder):
# 	a='%s/*.*'%folder
# 	temp=glob.glob(a)
# 	if temp==[]:
# 		return "文件夹为空或不存在"
# 	else:
# 		return temp
# print get_dir('/Users/captain/desktop/')


# import glob
# #获取指定目录下的所有图片（绝对路径）
# print glob.glob(r"/Users/captain/desktop/*.*")
#获取上级目录的所有.py文件（相对路径）
# print glob.glob(r'../*.py') #相对路径


# def get_fundoc(func):
# 	return func.__doc__
# print get_fundoc('string')


# def get_cjsun(a,b):
# 	sum=0
# 	for i in range(a,b):
# 		sum=sum+i*i
# 	return sum
# assert type(get_cjsun(2,4)) ==int
# print get_cjsun(2,4)

# a=[1,2,3]
# def list_info():
# 	b=a[:]#直接复制一个a对象的内容
# 	b[2]=5
# 	return b
# print list_info()
# print a

# def get_fundoc(func):
# 	if func.__doc__:
# 		return func.__doc__
# 	else: return 'Not found'
# print get_fundoc(int)

# def get_funcname(func):
# 	if hasattr(func, '__call__')
# 	# if isinstance(func, FunctionType)
# 		return func
# 	else: return 'func is not function'

# print get_funcname(int)


# print filter(lambda x :x%2==0, xrange(0,100))

# def get_cjsum(a,b):
# 	return reduce(lambda x,y: x+y, map(lambda x: x*x, xrange(a,b)))
# def func(*p):
# 	for i in p:
# 		if not isinstance(i, list):
# 			return '列表中有些不是list'
# 	a=p[0]
# 	for i in p:
# 		a.extend(i)
# 	a.sort()
# 	return a[-1]
# print func([1,2,3],[1,5,65],[33,445,22])


# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print fact(100)

# def fact(n):
#     return fact_iter(n, 1)
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# print fact(100)

# def func(a, b, c=0, *args, **kw):
#     print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
# func(1, 2)
# func(1, 2, c=3)
# func(1, 2, 3, 3, 5, 6, x=3, y=3, Z=9)


#coding=utf-8

# def capstr(name):
#     '''
#     capstr(name) -> str
#     name is a str.
#     return a capitalize type of name,or raise TypeError if name is not a str
#     '''
#     return name.capitalize()
# print capstr('123a')
# def shortstr(*kargs):
#     '''
#     shortstr(*kargs) -> str or None
#     return the shortest str in the kargs, or return None if no str in it.
#     '''
#     #过滤非字符串
#     lis = filter(lambda x:isinstance(x,str),kargs)
#     #收集长度
#     len_lis = [len(x) for x in lis]

#     try:
#         # 获取最短字符串长度
#         max_index=min(len_lis)#(前面的变量名有误导，最好改成min_index)
#         return lis[len_lis.index(max_index)]
#     # 没有字符串在里面，则报空
#     except ValueError:
#         return None
#     # 取其在len_list中的索引，返回对应在list中的元素


# assert shortstr(222,1111,'xixi','hahahah') == "xixi"
# assert shortstr(7,'name','dasere') == 'name'
# assert shortstr(1,2,3,4) == None
# print shortstr(222,1111,'xixi','hahahah')
# print shortstr(7,'name','dasere')
# print shortstr(1,2,3,4)
# # def shortstr(*krags):
# 	for i in krags:
# 		if isinstance(i, str):
# 			return i
# 	else: return None
# assert shortstr(222,1111,'xixi','hahahah') == "xixi"
# assert shortstr(7,'name','dasere') == 'name'
# assert shortstr(1,2,3,4) == None
# # else有时候也可以不用写		
# def func(i):
# 	if i==3:
# 		return '3a,a,,a,'
# 	return 'heheh'

# print func(3)
# print func(1)

# def func(name=None,**kargs):
#     '''
#     detail(name=None,**kargs) -> str
#     name is a str.return a str like'name,key1:value1,key2:value2'    
#     '''
#     data = []
#     for x,y in kargs.items():
#         data.extend([',', str(x), ':', str(y)])
   
#     info = ''.join(data)
#     return '%s%s'%(name,info)

# def func(name=None,**kargs):
# 	lis = ["%s:%s"%(k,v) for k,v in kargs.items()]
# 	lis.insert(0,name)
# 	return ','.join(lis)
# assert func("lilei") == "lilei"
# assert func("lilei",years=4) == "lilei,years:4"
# # assert func("lilei",years=10,body_weight=20) == "lilei,years:10,body_weight:20"
# print func("lilei",years=10,body_weight=20)


# class test(object):
# 	"""
# 	get被称之为test对象的方法
# 	"""
# 	def get(self):
# 		return 'heheh'
# t = test()
# print t.get()










# class test(object):


# 	"""

# 	get被称之为test对象的方法

# 	"""

# 	def __init__(self,var1):
# 		self.var1 = var1


# 	def get(self,a=None):
# 		return self.var1

# 	pass



# def get(a):
# 	return a


# """
# t是类test的一个实例
# """
# t = test('test str heiheihei')
# print t.get()

"""
如何去使用对象内置的方法
1.实例化这个class （test） t = test()
2.使用 class.method()的方式去调用 class 的内置方法

注意：
1.当定义一个class的内置方法method时，method的参数的第一个永远是self。
"""
# class test(object):
# 	"""docstring for test"""
# 	def __init__(self,var1):
# 		self.var1 = var1
# def get(self,a=None):
# 		return self.var1
#         pass
# t = test('test str heiheihei')
# print t.get()

# # # 函数
# # def gett(a):
# # 	return a
# # t=test()	

# try:
# 	pass
# except Exception as e:
# 	raise
# 	logging.debug(e)
# else:
# 	return url_info
# finally:
# 	pass

# def get_page(url):
#     if not isinstance(url,str):
#     	return '输入的数据类型不对'
#     if not (url.startswitch('http://')) and not url.startswitch('https://'):#这儿不能用or
#         return 'url地址不对'
#     date=urllib2.urlopen(url)
#     return date.read()
# print get_page('http://www.baidu.com')



# import urllib2
# def get_page(url):
#     if not (url.startswith('http://')) or url.startswith('https://'):
#         return 'url地址不对'
#     date=urllib2.urlopen(url)
#     return date.read()
# print get_page('http://www.baidu.com')


# import urllib2
# def get_page(url):
#     if not (url.startswith('http://')) or url.startswith('https://'):
#         return 'url地址不对'
#     date=urllib2.urlopen(url)
#     return date.read()
# print get_page('http://www.baidu.com')
# import urllib
# def get_page(url):
# 	if not (url.startswith('http://') or url.startswith('https://')):
# 		return 'url error'
# 	if not isinstance(url, str):
# 		return '输入的数据类型不对'
# 	try:
# 		url_info=urllib.open(url)
# 	except Exception as e:
# 		pass
# 		# logging.debug(e)#记录打开失败后的日志
# 	else:
# 		return url_info
# print get_page('https://www.baidu.com/')


# d=open('https://www.baidu.com/').read()
# print d
# import urllib
# import random
# import os
# # 1
# def save_url_content(url,folder_path=None):	
# 	if not (url.startswith('http://') or url.startswith('https://') ):
# 		return u'url地址不符合规格'
# 	if not os.path.isdir(folder_path):
# 		return u'folder_path非文件夹'
# 	try:
# 		d=urllib.urlopen(url)
# 	except Exception as e:
# 		print e
# 		return u'该网页无法打开'
# 	else:
# 		content = d.read()

# 	# d = urllib.urlopen(url)
# 	# content = d.read()
# 	rand_filename = 'test_%s'%random.randint(1,1000)
# 	file_path = os.path.join(folder_path,rand_filename)
# 	d = open(file_path,'w')
# 	d.write(content)
# 	d.close()
# 	return file_path
# print save_url_content('http://www.baidu.com','/Users/captain/desktop')

# import os
# #使用递归去解决
# def merge(folder_path):

# 	if not os.path.exists(folder_path):
# 		return 'not exists'

# 	for f in os.listdir(folder_path):
# 		file_path = os.path.join(folder_path,f)
# 		if os.path.isdir(file_path):
# 			merge(file_path)
# 		else:
# 			merge_file = open('/tmp/merge_test','ab+')
# 			content = open(file_path,'r').read()
# 			merge_file.write(content)
# 			merge_file.close()

# merge('/tmp/5')

#获取桌面文件的内容
# import linecache
# def get_text(p):
# 	with open(p, 'r') as g:
# 		filelist=linecache.getline(p, 1)
# 		print filelist
# 		# for line in filelist:
# 		# 	if 'unit_id=Camera360_002' in line :
# 		# 		print i
# get_text('/Users/captain/desktop/2')

# import linecache
# f=linecache.getlines('/Users/captain/desktop/a.txt')
# lines=[line[1:-2].split('","') for line in f]
# print len(filter(lambda line:line[1].startswith('h'), lines)) 

# liness=[line.strip().split(',') for line in f]
# print len(filter(lambda line:line[1].startswith('"h'), liness)) 






# def func():
# 	flist=[['h', 'f', 'e', 'hf', 'e', '5', '7'], ['ge', 'ge'], ['ge', 'h', 'eh'], ['bh', 'h', 'h']]
# 	blost=[]
# 	clist=[]
# 	for x in flist:
# 		for y in x:
# 			y=y.upper()
# 			blost.append(y)
# 		clist.append(blost)

# 	# print blost
# 	print clist
# func()


# 关于二维数组求和的几种方法：
# a = [[1,2],[3,4],[5,6]]
# 1.sum(map(sum,a)) # map(sum,a)=[3, 7, 11]
# 2.sum(sum(i) for i in a) 
# 3.sum(sum(a[i]) for i in range(len(a)))
# 4.reduce(lambda x,y:x+y, reduce(lambda x,y:x+y, a))#第一步：reduce(lambda x,y:x+y, a)=[1, 2, 3, 4, 5, 6]第一步的时候是（［1，2］＋［3，4］）＋［5，6］得到一个［1，2，3，4，5，6］，然后进行的运算是（（（（（1+2）＋3）＋4）＋5）＋6） ＝ 21



# count = len(open('/Users/captain/desktop/t.txt','rU').readlines())
# print count
# class SchoolMember(object):
#     '''Represents any school member.'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print '(Initialized SchoolMember: %s)' % self.name

#     def tell(self):
#         '''Tell my details.'''
#         print 'Name:"%s" Age:"%s"' % (self.name, self.age),

# class Teacher(SchoolMember):
#     '''Represents a teacher.'''
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print '(Initialized Teacher: %s)' % self.name

#     def tell(self):
#         print 'Salary: "%d"' % self.salary

# class Student(SchoolMember):
#     '''Represents a student.'''
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print '(Initialized Student: %s)' % self.name

#     def tell(self):
#         print 'Marks: "%d"' % self.marks

# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 22, 75)

# members = [t, s]
# for member in members:
#     member.tell()


# class test(object):
# 	"""docstring for test"""
# 	def get(self):
# 		return 4
# t=test()#t是类test的一个实例
# print t.get()


# class test(object):
# 	"""docstring for test"""
# 	@property#相当于定义一个内置属性，调用get的时候，就不需要后面的括号
# 	def get(self):
# 		return 4
# t=test()
# print t.get


# class test(object):
# 	"""docstring for test"""
# 	@staticmethod#静态方法的装饰，下面的定义函数的self就不需要添加了
# 	def get():
# 		return 4	
# print test.get()		

# if __name__=='__main':
# 	#可以把测试用例放入在这里面，来测试模块是否正确
# 	print 'sth'

# import m1
# print m1.hash()

# from m1 import *
# print hash()

# 在包m2的文件中存在，一个url_info.py文件，和一个__int__.py文件，在m2包的外层调用url_info文件
# # url_info.py文件内容如下：
# def get_page():
# 	return "this is page"

# # 外层调用
# import m2.url_info
# print m2.url_info

# # 或者:文件名太长可以另外命名一个
# import m2.url_info as url
# print url
# # 调用文件中的方法：
# print url.get_page()

# #或者
# from m2 import url_info
# print url_info.get_page()

# # import其中的方法不能这样：错误
# from m2 import url_info.get_page as get_page
# print get_page()
# # 但可以这样：
# from m2.url_info import get_page
# print get_page()

# #__int__.py文件中定义哪些文件可以进出
# __init__=['url_info']

# from m2 import *
# print url_info.get_page()


# 常用模块

# 1.我们去哪里找模块

# python的模块库：pypi.python.org 

# 2.我们应该首先选择哪些的模块

# 首先考虑的是，内置模块
# 文档：http://docs.python.org/2.7/

# 3.常用模块

# 3.1 urllib urllib2 网络
# 3.2 datetime time 时间
# 3.3 os 系统
# 3.4 pickle  对象序列化
# 	常用数据交换格式 json xml 
# 3.5 bsddb key=>value 
# 3.6 logging 日志

# import os
# import pickle,random
# def xulie(dirname,info):  
#     if not os.path.exists(dirname):  
#         return 'Not found!'  
#     a = pickle.dumps(info)  
#     filename = ''
#     for i in range(10):  
#         filename=filename+random.choice('abcedfghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890')  
#     filepath = os.path.join(dirname,filename)  
#     f = open(filepath,'a+')  
#     f.write(a)
#     f.close()  
# a=[1,2,3,4,5,6,7]  
# xulie('/users/captain/desktop',a)

# try:
# 	pass#抛出异常的代码
# except Exception as e:
# 	raise #抛异常执行这
# else:
# 	pass#没抛异常，执行这
# finally:
# 	pass#不管异常与否，都执行这


# import urllib
# sth_url = "http://www.baidu.com"
# try:
# 	d = urllib.urlopen(sth_url)
# except IOError:
# 	print "哈哈哈出错了"
# except 语法错误的异常:
# 	print '这儿出错'
# else:
# 	content = d.read()
# finally:
# 	d.close()

# print content


# def func(filename):
# 	try:
# 		f=open(filename)
# 		return f.read()
# 	except IOError:
# 		return 'Open file Error'
# 	else:
# 		pass
# 	finally:
# 		if 'data' in locals():#如果文件存在本地缓存，就关闭这个文件
# 			f.close()
# print func('/users/captain/desktop/a.txt')

#不知道异常处理得对不对
# import urllib2
# def func(urllist):
# 	for i in urllist:
# 		try:
# 			res=urllib2.urlopen(i)
# 			return res.readlines()
# 		except:
# 			file_log=open('/users/captain/desktop/error.log', 'a+')
# 			file_log.write(str(res.getcode())+'Error\n')
# 			return 'Error'
# print func(['http://www.baidu.com','http://www.qq.com'])

# print func([‘http://www.baidu.com‘,‘http://www.qq.com‘,‘http://www.xxx.com‘,‘www.qq.com‘])  
# import urllib
# def get_url(url_list):
#     for url in url_list:
#         try:   
#             print url
#             date=urllib.urlopen(url)
#                 #return date.read()
#             print date.read()
#         except: 
#             date=urllib.urlopen(url)
#             file_txt=open('/users/captain/desktop/error.txt','a+')
#             file_txt.write(str(date.getcode())+'Error\n')
#             return 'Error'
     
# print get_url(['http://www.baidu.com','http://www.qq.com','http://www.xxx.com','www.qq.com'])   
# import sys
# try:
# 	a=3
# 	assert a==4
# except:
# 	exc=sys.exc_info()
# 	print exc

# import sys
# import logging
# try:
# 	a=3
# 	assert a==4,'erro message'
# except:
# 	exc=sys.exc_info()
# 	logging.error(exc[1])

# import logging   
# logger = logging.getLogger()#定义logging对象
# logfile = 'test.log'
# hdlr = logging.FileHandler('/tmp/sendlog.txt')#定义文档生成路径
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr)
# logger.setLevel(logging.NOTSET)

#with方法可以省略掉关闭文件的那一步骤
# with open('a','r') as g:
# 	e=g.read()
# print 4

# 进入时，调用对象的__enter__方法
# 退出时，调用对象的__exit__方法

# d=open('a','r')
# d.read()
# d.close()

# class sth(object):
# 	def __init__(self,xixi):
# 		self.a=xixi
# 		print self.a
# 		# return self.a
# 	def __enter__(self):
# 		print '呵呵呵，进来了'
# 		return self.a
# 	def __exit__(self,type,value,traceback):
# 		print u'哈哈哈，出去了'
# with sth('xixi_name') as s:
# 	print s


# class sth(object):
# 	"""docstring for sth"""
# 	def __init__(self, arg):
# 		super(sth, self).__init__()
# 		self.arg = arg
# 	def __enter__(self):
# 		print '我进来了'
# 		print self.arg
# 		return self.arg
# 	def __exit__(self,type,value,traceback):
# 		print '我出去了'

# with sth('a test demo') as g:
# 	print g


# import logging #内置日志模块
# logger = logging.getLogger()#定义logging对象
# hdlr = logging.FileHandler('/tmp/sendlog.txt')#定义文档生成路径
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')#存储的格式：时间，等级，信息
# hdlr.setFormatter(formatter)#引入格式到hdlr文件对象
# logger.addHandler(hdlr)#将文件对象引入日志模块中
# logger.setLevel(logging.NOTSET)#设置日志的等级

# import urllib
# def func(urllist):
# 	for i in urllist:
# 		try:
# 			u=urllib.urlopen(i)
# 		except IOError:
# 			logging.error
# 		else:
# 			return u.read()
# 		finally:
# 			u.close()
# print func(['http://www.baidu.com','http://www.qq.com','this'])

# #ping 普通的ip地址没问题，但如果有管道（恶意代码）的话，结果就很惨，所以ping地址一般会先检测ip
# ping 126.com#这儿正常
# ping 126.com | rm-r /tmp/test#这儿就会直接删除掉/tmp/test目录下所有文件


# import os
# func(domainlist):
# 	for i in domainlist:
# 		try:
# 			os.system('ping -c 4 %s'%i)#这儿的意思是：ping 4次后终止
# 		except:
# 			pass#内容还不知道怎么写

# #或者直接用with的内置方法抛异常
# def func(filepath):
# 	with open(filepath,'r') as f:
# 		return f.read()



# import os
# func(domainlist):
# 	for i in domainlist:
# 		try:
# 			os.system('ping -c 4 %s'%i)#这儿的意思是：ping 4次后终止
# 		except:
# 			pass#内容还不知道怎么写


# def func(domainlist):
# 	system_name=platform.system()


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',8125))#绑定ip和端口
# s.listen(8)#队列
# while  1:
# 	conection,address=s.accept()
# 	buf=conection.recv(10)#接受10个字节
# 	conection.send(buf)
# s.close()

# def s(r,pi=3.14):
# 	return pi*r*r
# print s(2)
# print s(2,3.141592653)



# import os
# path = input("input zipfile path:").strip()
# if os.path.exists(path) and os.path.isfile(path):
#     print(path)
# elif os.path.exists(path) and os.path.isdir(path):
#     for i in os.listdir(path):
#         print(type(i))
#         fullpath = os.path.join(path, i)
#         print(fullpath)
# else:
#     print('err: not exist this path')



'''
import os
import platform
# print(platform.system()) #mac:'Darwin', windows:
# print(platform.python_version())
path = input(r"请拖入文件或者文件夹: ").strip()
#处理mac下拖动有空格名字文件夹，出现的转义字符
if r'\ ' in path:
    path = path.replace(r'\ ',' ')
#windows下拖动文件夹
if r'"' in path:
    path = path.replace(r'"', '')
#替换windows下\为/,一般还是不需要这个，会引起一系列的问题，比如os.path.join
if '\\' in path:
    path = path.replace('\\', '/')
'''
# os.chdir(path)

# print('后缀名:',os.path.splitext(path)[-1])
# print('文件全名:',os.path.basename(path))
# print('规范目录:',os.path.normpath(path))
# print('path是否存在：',os.path.exists(path))
# print('path是目录：',os.path.isdir(path))
# print('目录2:',path)
# path = os.path.normpath(path)
# print ('normalpath:', os.path.normpath(path))
# print('是文件',os.path.isfile(path))
# for i in os.listdir(path):
#     print(i)
    # fullpath = os.path.join(path, i)
    # print(fullpath)



# python正则没有可以测试一个字符串是否满足，然后返回False or True的函数,不像js函数，所以放弃了
# import re
# content='Where are you from? You look so hansome.'
# regex=re.compile(r'\w*som\w*')
# m=regex.search(content)
# if m:
#     print (m.group(0))
# else:
#     print ("Not found")


#python 定时器：
# from datetime import datetime
# from threading import Timer
# # 打印时间函数
# def printTime():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     t = Timer(3, printTime, ())
#     t.start()

# printTime()
# print('执行完了！')


# from datetime import datetime
# from threading import Timer
# def hello(): 
#     print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# t = Timer(10.0, hello) 
# t.start()


# import sched
# import time
# from datetime import datetime
# # 初始化sched模块的scheduler类
# # 第一个参数是一个可以返回时间戳的函数，第二参数可以在定时未到达之前阻塞
# schedule = sched.scheduler(time.time, time.sleep)
# # 被周期性调度触发函数
# def printTime(inc):
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     schedule.enter(inc, 0, printTime, (inc,))
# # 默认参数60s
# def main(inc):
#     # enter四个参数分别为：间隔事件,优先级（用于同时到达两个事件同时执行的顺序），被调度触发的函数
#     # 给该触发器函数的参数（tuple形式）
#     # schedule.enter(0, 0, printTime, (inc,))
#     printTime(inc)
#     schedule.run()
# # 5秒输出一次
# main(2)
# print('执行完了！')

# import schedule
# import time

# def job():
#     print("I'm working...")

# schedule.every(2).seconds.do(job)


'''
# 图片居中
import re
import math
from PIL import Image, ImageDraw, ImageFont

FONT_TYPE = r"/System/Library/Fonts/PingFang.ttc"

name = '耳朵-Android'
icon_name = re.split(r'-|_',name)[0]
path = '/Users/captain/Desktop'

print ('icon_name=',icon_name)

#先假设取一个值，而得到比例
font_size= 27
font = ImageFont.truetype(FONT_TYPE, size=font_size)
text_size_width = font.getsize(icon_name)[0]
print('text_size_width:',text_size_width)
#计算值
font_size_cal = math.floor(font_size*190/text_size_width)
print('font_size_cal:',font_size_cal)
if font_size_cal > 50:
    font_size_cal = 50

#font重新赋值
font = ImageFont.truetype(FONT_TYPE, size=font_size_cal)
text_size = font.getsize(icon_name)
print('text_size:',text_size)

x=100-text_size[0]/2
y=100-text_size[-1]/2

print(x,y)

img = Image.new("RGB", size=(200, 200), color=(179,238,58))  # 创建图形
draw = ImageDraw.Draw(img)

draw.text((x, y), icon_name, font=font, fill='#191970')
img.save('/Users/captain/Desktop/test.png','png')

'''

# import logging
# logging.basicConfig(filename = '/Users/captain/Desktop/testlog.txt',level = logging.WARNING,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s') #设置日志的消息级别
# logger = logging.getLogger(__name__)
 
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# 等级 debug < info < warning < error

# (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
# 找证书位置：
# import certifi
# print(certifi.where())



# import requests
# kw = {'wd':'长城'} 
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
# response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)
# # 查看响应内容，response.text 返回的是Unicode格式的数据
# print (response.text)
# # 查看响应内容，response.content返回的字节流数据
# print (response.content)
# # 查看完整url地址
# print (response.url)
# # 查看响应头部字符编码
# print (response.encoding) 
# # 查看响应码
# print (response.status_code)



# import requests
# formdata = {
#     "type":"AUTO",
#     "i":"i love python",
#     "doctype":"json",
#     "xmlVersion":"1.8",
#     "keyfrom":"fanyi.web",
#     "ue":"UTF-8",
#     "action":"FY_BY_ENTER",
#     "typoResult":"true"
# }
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null" 
# headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"} 
# response = requests.post(url, data = formdata, headers = headers) 
# # unicode码展示的
# print (response.text)
# # 如果是json文件可以直接显示
# print (response.json())



# #cookie
# import requests
# response = requests.get("http://www.baidu.com/")
# # 返回CookieJar对象:
# cookiejar = response.cookies
# # 将CookieJar转为字典：
# cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
# print (cookiejar)


# #session
# import requests
# # 1. 创建session对象，可以保存Cookie值
# ssion = requests.session()
# # 2. 处理 headers
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# # 3. 需要登录的用户名和密码
# data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}   
# # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
# ssion.post("http://www.renren.com/PLogin.do", data = data)
# # 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
# response = ssion.get("http://www.renren.com/410043129/profile")
# # 6. 打印响应内容
# print (response.text)