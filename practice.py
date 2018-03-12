--------------习--------题-----1---分-------割-------线------------------------------------

小结习题：
一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。

二.在python中，如何修改字符串？

三.bool("2012" == 2012) 的结果是什么。

四.已知一个文件 test.txt，内容如下：

____________
2012来了。
2012不是世界末日。
2012欢乐多。
_____________

1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
 

五.请用代码的形式描述python的引用机制。

六.已知如下代码

________

a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
________

1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数

七.已知如下变量
________
a = "字符串拼接1"
b = "字符串拼接2"
________

1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
 

八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。

九.已知字符串
________

a = "i,am,a,boy,in,china"
________

1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
 

十.请将模块string的帮助文档保存为一个文件。

------------习题1------答案分割线--------------------------------------
#coding=utf-8
#@description:周末作业
#一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。
print '第一题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
#方法1
s = "i,am,lilei"
print s[2:4]
##方法2
c = s.split(',')[1]
print c
print '第二题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
#二.在python中，如何修改字符串？
#答案：可以用字符串的replace方法.
ainfo = 'i love php'
replycontent = ainfo.replace('php','python')
print replycontent
print '第三题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
#三.bool("2012" == 2012) 的结果是什么。
##答案：结果是fasle,==判断对象的数据类型，尽管看起来数值是一样的，但是他们的类型不同，一个是字符串，一个是数字
print '第四题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##四.已知一个文件 test.txt，内容如下：
f = open('test.txt','r')
content = f.read()
dcontent = content.decode('utf-8')##转换为unicode
##1.请输出内容
print content
##2.请计算该文本的原始长度.不能直接对文本进行len
print len(dcontent)
##3.请去除该文本的换行
print content.replace('\n','')
##4.请替换其中的字符"2012"为"2013"。
print content.replace('2012','2013')
##5.请取出最中间的长度为5的子串。
print dcontent[len(dcontent)/2:len(dcontent)/2+5].encode('utf-8')
##6.请取出最后2个字符。
print 'aaaa--------'
print dcontent[-2:].encode('utf-8')
print 'bbbb--------'
##7.请从字符串的最初开始，截断该字符串，使其长度为11.
print dcontent[:11].encode('utf-8')
##8.请将{4}中的字符串保存为test1.py文本.
rinfo = content.replace('2012','2013')
f = open('test1.py','w')
f.write(rinfo)
f.close()##关闭文件
print '第五题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##五.请用代码的形式描述python的引用机制。
import sys
cinfo = '1234'
print id(cinfo)  
print sys.getrefcount('1234')   #引用计数从3开始计算，引用一次+1
binfo = '1234'
print id(binfo)
print sys.getrefcount('1234')
print '第六题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##六.已知如下代码
a = "中文编程"  ##引用计数开始是3，然后a变量引用了字符串对象3 + 1 =4
print "a:%s" % id(a)
b = a
print "b:%s" % id(b)##4 + 1 = 5
c = a
print "c:%s" % id(c)## 5 + 1 = 6
print sys.getrefcount('中文编程')##输出结果是6
# print 'ssss'
a = "python编程"
print "a:%s" % id(a)###6-1 = 5##a引用另外一个字符串对象
b = u'%s' % a.decode('utf-8')
print "b:%s" % id(b)###5-1 = 4
print sys.getrefcount('中文编程')##输出结果是4
d = "中文编程"
print "d:%s" % id(d)###新建一个变量，引用字符串 4 + 1 = 5
e = a
print "e:%s" % id(e)
c = b
print "c:%s" % id(c)### c引用另外一个字符串对象，5 - 1 = 4
print sys.getrefcount('中文编程')
b2 = a.replace("中","中")
print "b2:%s" % id(b2)
print 'result-----------------'
print sys.getrefcount('中文编程')
print sys.getrefcount('python编程')
print '第七题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##七.已知如下变量
a = "字符串拼接1"
b = "字符串拼接2"
#
##请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣
##方法1：在做大量的字符串对象拼接的时候不推荐
c = a + b
##方法2：
c = "%s%s" % (a,b)
###方法3：
print 'format'
c = "{a}{b}" .format (a=a,b=b)
##方法4：
c = "".join([a,b])
print c
##请将a与b拼接成字符串c，并用逗号分隔。
c = '%s,%s' % (a,b)
##.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
lennum = len(c.decode('utf-8'))
print c.decode('utf-8')[6].encode('utf-8')
print '第八题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案
import string
##1.包含0-9的数字。
#print help(string)
print string.digits
##2.所有小写字母
print string.lowercase
##3.所有标点符号
print string.punctuation
##4:所有大写字母和小写字母。
print string.ascii_lowercase##小写字母
print string.ascii_uppercase##大写字母
print '\n'
##5：请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
strinfo = []
strinfo.append(string.digits)
strinfo.append(string.lowercase)
strinfo.append(string.punctuation)
strinfo.append(string.ascii_lowercase)
strinfo.append(string.ascii_uppercase)
print "".join(strinfo)
print '\n'
strinfo = "%s%s%s%s%s" % (string.digits,string.lowercase,string.punctuation,string.ascii_lowercase,string.ascii_uppercase)
print strinfo
print '第九题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##九.已知字符串
a = "i,am,a,boy,in,china"
##1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
ac = "i,am,a,%(sex)s,in,%(country)s"  % {'sex':'girl','country':'china'}
bc = "i,am,a,{sex},in,{country}" .format (sex='girl',country='india')
print ac
print bc
##2.请使用2种办法取出其间的字符"boy"和"china"。
##方法1
print a[7:10]
print a[-5:]
##方法2
cinfo = a.split(',')
print cinfo[3]
print cinfo[-1]
##3.请找出第一个"i"出现的位置。
print a.find('i')##-1
print a.index('i')##报错
##4.请找出"china"中的"i"字符在字符串a中的位置。
print a.find('i',a.find('china'))
print a.rfind('i')   #从字符串的右往左边开始查找
##5.请计算该字符串一共有几个逗号
print a.count(',')
print '第十题－－－－－－－－－－－－－－－－－－－－－－－－－－－－－'
##十.请将模块string的帮助文档保存为一个文件。
import sys
import string
f = open('test.log','w')
sys.stdout 




------------习题2-----分-------割-------线---------------------------------------------

1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
1.1 请将a字符串的大写改为小写，小写改为大写。
1.2 请将a字符串的数字取出，并输出成一个新的字符串。
1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
1.9 输出a字符串出现频率最高的字母

2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。

3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。
 
4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.


------------习题2----------------------------------答案分割线----------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#习题1.1
a = "aAsmr3idd4bgs7Dlsf9eAF"
print a.swapcase()

#习题1.2
a = "aAsmr3idd4bgs7Dlsf9eAF"
print ''.join([x for x in a if x.isdigit()])

#题1.3
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_lower=a.lower()
a_short=set(a_lower)
print dict([(x, a_lower.count(x)) for x in a_short])

#题1.4
a = "aAsmr3idd4bgs7Dlsf9eAF"
print ''.join(sorted(set(a), key=lambda x: a.index(x)))
#或者缩写如下：print ''.join(sorted(set(a), key=a.index))
#题1.5
a = "aAsmr3idd4bgs7Dlsf9eAF"
print a[::-1]
#或者 
a = "aAsmr3idd4bgs7Dlsf9eAF"
i=0
c=[]
while i<len(a):
	c.append(a[len(a)-1-i])
	i=i+1
print ''.join(c)
#题1.6
#方法一：（视频教程讲解）
#但程序有个bug:如果大写字母没有对应的小写字母在里面，会造成大写字母没添加上的状况
a = "aAsmr3idd4bgs7Dlsf9eAF"
# a="aAsmr3idd4bgs7Dlsf9eAFHBCJK"#如果a为这个代码，上述bug就出现了
l=sorted(a)
a_upper=[]
a_lower=[]
for x in l:
	if x.isupper():
		a_upper.append(x)
	elif x.islower():
		a_lower.append(x)
	else:
		pass
for y in a_upper:
	y_lower=y.lower()
	if y_lower in a_lower:
		a_lower.insert(a_lower.index(y_lower),y)
	else:
		pass#这儿代码应该处理大写字母没找到的情况
print ''.join(a_lower)
#方法2：
a = "aAsmr3idd4bgs7Dlsf9eAF"
# a="aAsmr3idd4bgs7Dlsf9eAFHBCJK"
b = list(filter(str.isalpha,a))#filter目的是为去掉字符串的数字
c = sorted(b,cmp=lambda x,y:1 if (x.upper()>y.upper()) else -1)
print ''.join(c)# 此排序忽略了字母的大小写
'''
cmp比较两个元素的大小，如果返回1，就知道第一个元素大于第二个元素，将第一个元素移动至后面，返回0表示相等，返回-1表示第一个元素小于第二个元素，sorted根据cmp的返回值执行算法，将小的元素放前面，大的元素放后面
'''
#方法3（很简短，赞成这个）
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_filter=filter(str.isalpha,a)#a_filter为去掉数字后的字符串
print( ''.join( sorted(a_filter,key = lambda x : ord( x.lower( ))*2 + x.islower( ))))#这儿为什么*2有点不明白
# 题1.7
a = "aAsmr3idd4bgs7Dlsf9eAFH"
search="boy"
u=set(a)
u.update(list(search))
print len(set(a))==len(u)
# 题1.8
a = "aAsmr3idd4bgs7Dlsf9eAFH"
search=['boy','girl','bird','dirty']
b=set(a)
for i in search:
	b.update(list(i))
print len(set(a))==len(b)
# 或者：
a = "aAsmr3idd4bgs7Dlsf9eAFH"
search=['boy','girl','bird','dirty']
sl=list(set(list(''.join(search))))#把搜索的字符去重成一个list
b=set(a)
b.update(sl)
print len(set(a))==len(b)
# 题1.9
a = "aAsmr3idd4bgs7Dlsf9eAFH"
l=([(x,a.count(x)) for x in set(a)])#对a去重后再进行统计
l.sort(key=lambda k:k[1],reverse=True)
print l[0][0]
# 题2
# python -m this效果等同于import this
import os
m = os.popen('python -m this').read()
m=m.replace('\n','')
l=m.split(' ')
print [(x, l.count(x)) for x in ['be','is','than']]
# 题3
byte=102324123499123
kb=byte>>10
mb=byte>>20
print 'KB:%s'%kb, 'MB:%s'%mb
# 题4
# 方法一
a =  [1,2,3,6,8,9,10,14,17]
print str(a)[1:-1].replace(', ','')
# 方法二
a = [1,2,3,6,8,9,10,14,17]
b=[]
for x in a:
	b.append(str(x))
print "".join(b)




-----------------------习题3----------以及答案---------------------
1 写一个函数代码，返回这3个数字中最大的一个。
a = 123
b = 345
c = 444

2 分别写2个函数，完成下面的功能：
提示一下用到函数的：**和*，猩猩是字典，星是元组
	2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果：[22, 44, 88]
	2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果:(‘xaay','yaay','zaay')

# 1
def max3(a,b,c):
	return max(max(a,b),c)
a = 123
b = 345
c = 444
print max3(a,b,c)
#简单方法直接用内置函数print max(a,b,c)
print max(a,b,c)
# 2.1
def ainfo(x,y,z):
	return list((x,y,z))
	#或者
	#return [x,y,z]
print ainfo(x=88, y=22, z=44)
# 或者
def ainfo(**po):
	return po.values()
print ainfo(x=88, y=22, z=44)
#2.2
def cinfo(**pw):
	li=[]
	for x in pw:
		li.append('%saay'%x) 
	return tuple(li)
print cinfo(x=88, y=22, z=44)


-----------------------总结习题---------承上启下---------------------
要求如下：

1.该文本里，有多少个用户。（要求：输出为一个整数。）

2.该文本里，每一个用户的名字。 （要求：输出为一个list。）

3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）

5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）

6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）

7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 

8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）

9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）

11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）

13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）

14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）


#coding=utf-8
import linecache
import time
now = time.time() #代码开始时间
# 前期准备，整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')
keys = {data_keys[k]:k for k in xrange(0,len(data_keys))}
f = linecache.getlines('/Users/captain/desktop/t.txt')
lines = [x[1:-1].split('","') for x in f] #拆分
    
#1 输出用户总数
users = set([line[keys['username']] for line in lines])
user_total = len(set(users))
assert type(user_total) == int#断言函数
#2 每一个用户的名字 list
users = list(users)
assert type(users) == list
#3 有多少个2012年11月发布的tweets
lines_from_2012_11 = filter(lambda line:line[keys['created_at']].startswith('2012-11'),lines)
lines_total_from_2012_11 = len(lines_from_2012_11)
assert type(lines_total_from_2012_11) == int

#4 该文本里，有哪几天的数据？ 
users_by_date = [line[keys['created_at']].split(' ')[0] for line in lines]
lines_by_created = list(set(users_by_date))
lines_by_created.sort()
assert type(lines_by_created) == list
#5 该文本里，在哪个小时发布的数据最多？ 
# todo 这里用time模块做时间转换最好。下例只为讲解拆分方法
hours = [int(line[keys['created_at']][11:13]) for line in lines]
total_by_hour = [(h,hours.count(h)) for h in xrange(0,24) ]
total_by_hour.sort(key=lambda k:k[1],reverse=True)
max_hour = total_by_hour[0][0]
assert type(max_hour) == int
#6 该文本里，输出在每一天发表tweets最多的用户
dateline_by_user = {k:dict() for k in lines_by_created}
for line in lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if dateline_by_user[dateline].has_key(username):
        dateline_by_user[dateline][username] += 1
    else:
        dateline_by_user[dateline][username] = 1
for k,v in dateline_by_user.items():
    us = v.items()
    us.sort(key=lambda k:k[1],reverse=True)
    dateline_by_user[k] = {us[0][0]:us[0][1]}
assert type(dateline_by_user) == dict
    
#7 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率
lines_from_2012_11_03 = filter(lambda line:line[keys['created_at']].startswith('2012-11-03'),lines)
hourlines_from_2012_11_03 = {str(i):0 for i in xrange(0,24)}
for line in lines_from_2012_11_03:
    hour = line[keys['created_at']][11:13]
    hourlines_from_2012_11_03[str(int(hour))] += 1 
hour_timeline_from_2012_11_03 = [(k,v) for k,v in hourlines_from_2012_11_03.items()]
hour_timeline_from_2012_11_03.sort(key=lambda k:int(k[0]))
assert type(hour_timeline_from_2012_11_03) == list
#8 统计该文本里，来源的相关信息和次数
source = set([k[keys['source']] for k in lines])
source_dict = {s:0 for s in source}
for line in lines:
    source_name = line[keys['source']]
    source_dict[source_name] += 1
source_list = [(k,v) for k,v in source_dict.items()]
source_list.sort(key=lambda k:k[1],reverse=True)
assert type(source_list) == list
#9 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个
umi_total = 0
for line in lines:
    if line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'):
        umi_total += 1
assert type(umi_total) == int
#10 UID为573638104的用户 发了多少个微博
tweets_total_from_573638104 = 0
for line in lines:
    if line[keys['uid']] == '573638104' :
        tweets_total_from_573638104 += 1
assert type(tweets_total_from_573638104) == int
#11 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
def get_user_by_max_tweets(*uids):
    
    '''
    @deprecated:参数可为字符串或者数字
    '''
    
    if len(uids) > 0:
        uids = filter(lambda u:type(u) == int or u.isdigit(),uids)
        uids = map(str,uids)
        if len(uids) > 0:
            uids_dict = {x:0 for x in uids}
            for line in lines:
                uid = line[keys['uid']]
                if uid in uids:
                    uids_dict[uid] += 1
            uids_and_tweets_total = [(x,y) for x,y in uids_dict.items()]
            uids_and_tweets_total.sort(key=lambda k:k[1],reverse=True)
            return uids_and_tweets_total[0][0]
    return "null"
assert get_user_by_max_tweets() == 'null'
assert get_user_by_max_tweets('ab','cds') == 'null'
assert get_user_by_max_tweets('ab','cds','123b') == 'null'
assert get_user_by_max_tweets('12342','cd') == '12342'
assert get_user_by_max_tweets('28803555',28803555) == '28803555'
assert get_user_by_max_tweets('28803555',28803555,'96165754') == '28803555'
#12 该文本里，谁发的微博内容长度最长 
lines_by_content_length = [(line[keys['username']],len(line[keys['content']])) for line in lines]
lines_by_content_length.sort(key=lambda k:k[1],reverse=True)
user_by_max_content = lines_by_content_length[0][0]
# todo 如果有多个最多怎么办？
assert type(user_by_max_content) == str
#13 该文本里，谁转发的URL最多 
lines_by_rt = [(line[keys['uid']],int(line[keys['rt_num']])) for line in lines if line[keys['rt_num']] != '']
lines_by_rt.sort(key=lambda k:k[1],reverse=True)
user_by_max_rt = lines_by_rt[0][0]
assert type(user_by_max_rt) == str
#14 该文本里，11点钟，谁发的微博次数最多。
lines_on_hour11 = filter(lambda line:line[keys['created_at']].startswith('11',11,13),lines)
lines_by_uid_on_hour11 = {k[keys['uid']]:0 for k in lines_on_hour11}
for line in lines_on_hour11:
    uid = line[keys['uid']]
    lines_by_uid_on_hour11[uid] += 1
d = [(k,v) for k,v in lines_by_uid_on_hour11.items()]
d.sort(key=lambda k:k[1],reverse=True)
uid_by_max_tweets_on_hour11 = d[0][0]
# todo 如果有多个最多怎么办？
assert type(uid_by_max_tweets_on_hour11) == str
#15 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
uid_by_v_url = {k[keys['uid']]:0 for k in lines}
for line in lines:
    uid = line[keys['uid']]
    if lines[keys['v_url']] != '':
        uid_by_v_url[uid] += 1
uid_sort_by_v_url = [(k,v) for k,v in uid_by_v_url.items()]
uid_sort_by_v_url.sort(key=lambda k:k[1],reverse=True)
uid_by_max_v_url = uid_sort_by_v_url[0][0]
# todo 如果有多个最多怎么办？
assert type(uid_by_max_v_url) == str
print '运算时间：%s'%(time.time() - now) #整体运行时间




自己写的：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import linecache
import time
now = time.time() #代码开始时间
# 前期准备，整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')
#tag对应的index
dkeys={data_keys[k]:k for k in xrange(0,len(data_keys))}
# 获取文件的list
file=linecache.getlines('/Users/captain/desktop/t.txt')
# 文件list的二维矩阵,strip()去掉每行末尾的\n字符,拆分符号
lines=[line[1:-2].split('","') for line in file]
#1.该文本里，有多少个用户
print len(set([line[dkeys['username']] for line in lines]))
#2.该文本里，每一个用户的名字
print list(set([line[dkeys['username']] for line in lines]))
# 3.该文本里，有多少个2012年11月发布的tweets
print ''.join([line[dkeys['created_at']] for line in lines]).count('2012-11')#用count
# 或者
ctime= [line[dkeys['created_at']] for line in lines]
print len(filter(lambda x: x.startswith('2012-11'),ctime))#用startswith
# 或者
print len(filter(lambda line:line[dkeys['created_at']].startswith('2012-11'),lines))
'''
答案中=33189，而自己算出来=32846，自带编译器算出为33190
自己用的分割方法，保留了字符中的双引号，然后用双引号统计结果为32846，少了很多，而用mac自带的文本编译器，atom,sublime搜索出来都为33190，数目都不一致，很奇怪
自用分割为：lines=[line.strip().split(',') for line in file]
'''
# 4.该文本里，有哪几天的数据
user_bydate=[line[dkeys['created_at']].split(' ')[0] for line in lines]
lines_by_created=sorted(list(set(user_bydate)))
print lines_by_created
# 5.该文本里，在哪个小时发布的数据最多
hours=[int(line[dkeys['created_at']][11:13]) for line in lines]
hours_count=[(h,hours.count(h)) for h in xrange(24)]
hours_count.sort(key=lambda x: x[1], reverse=True)
max_hours=hours_count[0][0]
print max_hours
# 6.该文本里，输出在每一天发表tweets最多的用户。
#引用题目4中的数据
user_bydate=[line[dkeys['created_at']].split(' ')[0] for line in lines]
lines_by_created=sorted(list(set(user_bydate)))
#先定义一个空的嵌套字典
dateline_by_user = {k:dict() for k in lines_by_created}
# dateline_user={k:"" for k in lines_by_created}#如果要输出一维字典，+这句
for line in lines:
	dateline=line[dkeys['created_at']].split(' ')[0]
	username=line[dkeys['username']]
	if dateline_by_user[dateline].has_key(username):#如果嵌套字典中的name不存在的话，初始化1，存在就+1
		dateline_by_user[dateline][username] += 1
	else:
		dateline_by_user[dateline][username] = 1
for k,v in dateline_by_user.items():#对嵌套的字典的value进行排序，并返回最大value的key
	us=v.items()
	us.sort(key=lambda k:k[1],reverse=True)
	dateline_by_user[k] = {us[0][0]:us[0][1]}#这儿输出的是二维字典
	# dateline_user[k]=us[0][0]#如果要输出一维字典，+这句
print dateline_user
# 7.请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率
lines_2012_11_03=filter(lambda line: line[dkeys['created_at']].startswith('2012-11-03'),lines)
hoursline_2012_11_03={str(i):0 for i in xrange(24)}
for line in lines_2012_11_03:
	hour=line[dkeys['created_at']][11:13]
	hoursline_2012_11_03[str(int(hour))]+=1
print sorted(hoursline_2012_11_03.items(), key=lambda x:int(x[0]))
# 8.统计该文本里，来源的相关信息和次数


-----------------进阶习题1-----------------------------------
习题：

1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。

2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。

3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。

例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。

4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。

5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）

习题：

1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def func(*num):
	for i in num:
		if isinstance(i, int):
			a=sorted(num)
			return 'max=%s, min=%s'%(a[-1],a[0])
			# 或者
			# a=max(list(num))
			# b=min(list(num))
			# return 'max=%s, min=%s'%(a,b)
		else:
			return '输入的参数必须为整型'
print func(1,3,9,5,66,0)
print func('a','c')
print func(3,'c')#程序有bug,此处返回max=c, min=3

上面bug修复后如下：应该把执行放在参数循环检查外面
def func(*num):
	for i in num:
		if not isinstance(i, int):
			return '输入的参数必须为整型'	
	a=max(list(num))#max或min可以直接对list和tuple进行处理,从某些方面说list和tuple,还有str是等价的
	b=min(list(num))
	return 'max=%s, min=%s'%(a,b)
	# 或者
	# a=sorted(num)
	# return 'max=%s, min=%s'%(a[-1],a[0])			
print func(1,3,9,5,66,0)			
print func('a',3)
print func(3,'c')
2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def func(*istring):
	for i in istring:
		if not isinstance(i, str):
			return '输入的参数必须为多个字符串内型'
	#这儿只能针对字符串长度不一样的字符
	# d=dict([(len(i), i)for i in istring])
	# return 'istring_max=%s,istring_min=%s'%(d[max(d)],d[min(d)])
	
	#下面针对有多个相同长度的字符串做优化（其实题目一也应该做这个优化）
	d=dict([(i, len(i))for i in istring])
	s=sorted(d.items(), key=lambda x:x[1])
	#遍历字符串list中长度最短和最长的元素
	minlist=[]
	maxlist=[]
	for x, y in d.items():
		if y==s[0][1]:
			minlist.append(x)
	for x, y in d.items():
		if y==s[-1][1]:
			maxlist.append(x)
	return 'minlist=%s, maxlist=%s'%(minlist,maxlist)
print func('abc','a','eegegh','b','ggg','ggeedg', '3')
print func('1')
答案解答如下：
def fun2(*num2):
	b=[]
	for i in num2:
	    if isinstance(i,str):
	        b.append(i)
	    else:
	    	return "输入的参数必须为多个字符串内型"
	return "max string is %s" % max(b, key=lambda x:len(x))#按照字符串的长度进行排序
print fun2('abc','a','eegegh','b','ggg','hhh','ggeedg', '3')
print fun2('1')
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。

import os
def get_doc(module):
	a='pydoc %s'%module
	m=os.popen(a).read()
	return m
print get_doc('string')


一个女大神写的类：（但结果运行出来有错）
# 因为sy.stdout是一个文件类型，所以定义一个类，继承与object父类，貌似也可以简历一个file对象，
class TextArea(object):
	# 每个类必须的__int__.用于初始化类的内部结构，为类的属性设置默认值
	def __int__(self):
		self.buffer=[]
	#必须要有write方法，因为把sys.stdout接到这边后，print实际上就是调用了一个sys.stdout的wrtie方法
	def write(self, *args):
		for i in args:
			self.buffer.append(i)
def get_doc(module):
	import sys
	#更改输出的，好像叫管道
	stdout=sys.stdout
	sys.stdout=TextArea()
	#help中的print出来的就被记录到TextArea()了
	help(module)
	#还原输入输出，否则后面的都不能正常使用print
	text_area, sys.stdout = sys.stdout, stdout
	# 取存在text_area.buffer中的，本应该被print的列表
	return ''.join([i for i in text_area.buffer])
# assert type(get_doc(func1)) == str
assert type(get_doc(help)) == str

4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。

import os
def get_text(f):
	a='cat %s'%f   #cat可以获取对应路径文件的内容，如果此路径没有，则会报错；这儿还需要考虑没有此文件的状况
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

一个女大神写的：（亲测有效）
def get_text(f):
	import os#老师建议把这一句放在函数之外
	if os.path.exists(f):
		fil=file(f)
		ans=fil.read()
		fil.close()
		return ans
	else: return None


网上答案如是说：#有效
def get_text(f):
	a=open(f)
	return a.read()  #此处是否该有文件关闭？
print get_text('/Users/captain/desktop/t.txt')

#如果有关闭的话应该如下：
def get_text(f):
	a=open(f)
	re=a.read()
	a.close()
	return re
print get_text('/Users/captain/desktop/a.txt')

# 用with方法
def get_text(f):
	with open(f, 'r') as g:
		return g.read()
print get_text('/Users/captain/desktop/a.txt')

#为了考虑大文件用with读写，可以优化如下：
def get_text(f):
	with open(f, 'r') as g:
		for line in g.readlines():
			print line.strip()#strip()是把末尾的'\n'给删掉
get_text('/Users/captain/desktop/t.txt')

5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）

import glob
def get_dir(folder):
	a='%s/*.*'%folder
	temp=glob.glob(a)
	if temp==[]:
		return "文件夹为空或不存在"
	else:
		return temp
print get_dir('/Users/captain/desktop/')

一女大神写的（测试无效）
def get_dir(folder=None):
	import os
	import glob
	if folder==None:
		folder=os.getcwd()
	if os.path.isdir(folder):
		import glob
		return [x.split('\\')[-1] for x in glob.glob('%s\\*.*'%folder)]
	else:
		return None
assert type(get_dir())==list
assert type(get_dir('abc'))==type(None)#老师建议import导入写在函数之外，另外断言的话，不仅要检查类型，还应该检查结果
print get_dir('/Users/captain/desktop/')


答案如下：
import glob
def get_dir(d):
    for i in glob.glob(d+'\*'):
        print i
get_dir('C:\Users\Administrator\Desktop')


---------------------进阶习题2--------------------------------------------
习题：

1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。(一般写程序的话，会把不需要符合条件的给过滤掉)

def get_num(num):
	lista=[]
	for i in num:
		if isinstance(i, int):
			if i%2==0:
				lista.append(i)
		else:return '你的列表中有不是字符的'
	return lista
print get_num([1,2,3,5,6,7,'ab'])

2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
import urllib
def get_page(url):
	f=urllib.urlopen(url)
	return f.readlines()
# 或者
import urllib
import urllib2
def get_page(url):
	req=urllib2.Request(url)
	res=urllib2.urlopen(req)
	return res.readlines()
print get_page('http://www.cnblogs.com/sysu-blackbear/p/3629420.html')
#网页答案
import urllib2
def get_page(url):
    if not (url.startswith('http://')) or url.startswith('https://'):#教程说中间不能用or,要用and not
        return u'url地址不对'
    date=urllib2.urlopen(url)
    return date.read()
print get_page('http://www.baidu.com')
#教程答案，试了没用 IndentationError: unindent does not match any outer indentation level
def get_page(url):
	if not isinstance(url, str):
		return '输入的数据类型不对'
    if not url.startswith('http://') and not url.startswith('https://'):
    	return 'url error'
    try:
    	url_info=url.open(url).read()
    except Exception as e:
    	logging.debug(e)#记录打开失败后的日志
    else:
    	return url_info
print get_page('http://www.baidu.com')


3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def func(*p):
	for i in p:
		if not isinstance(i, list):
			return '列表中有些不是list'
	a=p[0]
	for i in p:
		a.extend(i)
	a.sort()
	return a[-1]
print func([1,3,8],[2,5,7],[31,5,20],[5,2])
print func([1,3,8],['c',5,7],[31,5,'A'],[5,2],'abc')

4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。

import os
import glob
def get_dir(f):
	if os.path.exists(f):
		return glob.glob(f+'\*')
	else:
		return 'Not dir'
print get_dir('C:\Users\Administrator\Desktop')




---------------------进阶习题3-------------------------------------------
今天习题：

1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
#这儿还差对对象和描述文档的判读
def get_fundoc(func):
	return func.__doc__
print get_fundoc('string')

def get_fundoc(func):
	if func.__doc__:
		return func.__doc__
	else: return 'Not found'
print get_fundoc(int)
2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
def get_cjsun(a,b):
	sum=0
	for i in range(a,b):
		sum=sum+i*i
	return sum
assert type(get_cjsun(2,4)) ==int
print get_cjsun(2,4)

或者：
reduce(lambda x,y: x+y, map(lambda x: x*x, xrange(a,b)))
3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
   '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。
a=[1,2,3]
def list_info():
	b=a[:]#直接复制一个a对象的内容
	b[2]=5
	return b
print list_info()
print a

4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"。


---------------------进阶习题4----------------------------------------
今天习题：

1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）

>>> filter(lambda x :x%2==0, xrange(0,100))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445
def func(*p):
	for i in p:
		if not isinstance(i, list):
			return '列表中有些不是list'
	a=p[0]
	for i in p:
		a.extend(i)
	a.sort()
	return a[-1]
print func([1,2,3],[1,5,65],[33,445,22])

3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)
#上面的效果等同于0+1+..+100
def func2(i):
	max=101
	sum=0
	while i<max:
		sum=sum+i
		i=i+1
	return sum
print func2(0)
print sum(range(0,101))

---------------------进阶习题5----------------------------------------


'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def capstr(name):
    '''
    capstr(name) -> str
    name is a str.
    return a capitalize type of name,or raise TypeError if name is not a str
    '''
    if isinstance(name, str):
        return name.capitalize()
    else:
        raise TypeError, 'not a str type'
#上述女大神写的缺点：抛出异常用系统的就好了，不用另外写，优化后如下：        
def capstr(name):
    '''
    capstr(name) -> str
    name is a str.
    return a capitalize type of name,or raise TypeError if name is not a str
    '''
    return name.capitalize()


"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""

import string
def swastr(name, callback=None):
    '''
    swastr(name, callback=None) -> str
    name is a str.return a str of required tyoe,or a capitalize type if is not required.
    '''
    if isinstance(name,str):
        if callback==None:
            return name.capitalize()
        else:
            return callback(name)
#上述女大神写的缺点：函数if..else最好配套使用，优化后如下：
import string
def swastr(name, callback=None):
    '''
    swastr(name, callback=None) -> str
    name is a str.return a str of required tyoe,or a capitalize type if is not required.
    '''
    if callback == None:
        return name.capitalize()
    else:
        return callback(name)    

"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6


"""
def getitem(*kargs):
    return kargs

"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None


"""
女大神写的：@吐槽：这个应该可以有多个结果,应该返回一个列表才合理
def shortstr(*kargs):
    '''
    shortstr(*kargs) -> str or None
    return the shortest str in the kargs, or return None if no str in it.
    '''
    #过滤非字符串
    lis = filter(lambda x:isinstance(x,str),kargs)
    #收集长度
    len_lis = [len(x) for x in lis]
try:
        # 获取最短字符串长度
        max_index=min(len_lis)#(前面的变量名有误导，最好改成min_index)
    # 没有字符串在里面，则报空
    except ValueError:
        return None
    # 取其在len_list中的索引，返回对应在list中的元素
    else:#(这儿的else表示看不懂)
        return lis[len_lis.index(max_index)]#(把这一句放在try里面也能正常执行)
# 优化后
def shortstr(*kargs):
    '''
    shortstr(*kargs) -> str or None
    return the shortest str in the kargs, or return None if no str in it.
    '''
    #过滤非字符串
    lis = filter(lambda x:isinstance(x,str),kargs)
    #收集长度
    len_lis = [len(x) for x in lis]
if len_lis:
    		min_index = min(len_lis)
    		return lis[len_lis.index(min_index)]
    return None
#我自己理解题目的意思是返回其中的第一个字符串，没有返回none:
def shortstr(*krags):
    for i in krags:
        if isinstance(i, str):
            return i
    else: return None


"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""
def func(name=None,**kargs):
    '''
    detail(name=None,**kargs) -> str
    name is a str.return a str like'name,key1:value1,key2:value2'    
    '''
    data = []
    for x,y in kargs.items():
        data.extend([',', str(x), ':', str(y)])
   
    info = ''.join(data)
    return '%s%s'%(name,info)
# 上面优化如下：
def func(name=None,**kargs):
	lis = ["%s:%s"%(k,v) for k,v in kargs.items()]
	lis.insert(0,name)
	return ','.join(lis)

---------------------进阶习题6-------面向对象1---------------------------------


面向对象习题：

一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		super(Student, self).__init__()
		self.name = name
		self.age = age
		self.score=score
	def get_name(self):
		assert type(self.name)==str
		print 'name:%s'% self.name
	def get_age(self):
		assert type(self.age)==int
		print 'age:%s'% self.age
	def get_course(self):
		max_score=sorted(self.score)[-1]
		assert type(max_score)==int
		print 'max_score:%s'% max_score
zm = Student('zhangming',20,[69,88,100])
zm.get_name()
zm.get_age()
zm.get_course()
lq = Student('liqiang',23,[82,60,99])
lq.get_name()
lq.get_age()
lq.get_course()


二：定义一个字典类：dictclass。完成下面的功能


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})

#这儿还有一种方法，直接继承字典的属性，list.tuple.dict都可以直接继承
class Dictclass(object):
	"""docstring for Dictclass"""
	def __init__(self, arg):
		super(Dictclass, self).__init__()
		self.arg = arg
	def del_dict(self, key):
		print self.arg.pop(key,'key not found')
	def get_dict(self,key):
		print self.arg.get(key,'not found')
	def get_key(self):
		keylist=self.arg.keys()
		assert type(keylist)==list
		print keylist
	def update_dict(self,key):
		self.arg.update(key)
		print self.arg.values()
dict_a=Dictclass({'age': 22, 'name': 'lilei','sex':'girl'})
dict_a.del_dict('age')
dict_a.get_dict('sex')
dict_a.get_key()
dict_a.update_dict({'city':'beijing', 'phone':'5s'})



---------------------进阶习题7-------面向对象2---------------------------------
习题：

定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])

定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)


---------------------进阶习题8-------函数习题---------------------------------
#!/usr/bin/env python
#encoding=utf-8
'''
函数周末习题：
1.定义一个func(url,folder_path),获取url地址的内容，保存到folder_path的文件目录下，并随机生成一个文件名。
2.定义一个func(folder_path)，合并该目录下所有文件，生成一个all.txt
3,定义一个func(url)，分析该url有多少个链接
4,定义一个func(url)，获取？后面的参数，并返回一个dict
5.定义一个func(folder),删除改folder下的所有文件
'''
import urllib
import random
import os
# 习题1
def save_url_content(url,folder_path=None):	
	if not (url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	if not os.path.isdir(folder_path):
		return u'folder_path非文件夹'
	try:
		d=ulib.urlopen(url)
	except Exception as e:
		print e
		return u'该网页无法打开'
	else:
		content = d.read()
	# d = urllib.urlopen(url)#不要上面的try的话，就直接运行注释的内容就好了
	# content = d.read()
	rand_filename = 'test_%s'%random.randint(1,1000)
	file_path = os.path.join(folder_path,rand_filename)
	d = open(file_path,'w')
	d.write(content)
	d.close()
	return file_path
print save_url_content('http://www.baidu.com')


##习题2
import os
#使用递归去解决
def merge(folder_path):
if not os.path.exists(folder_path):
		return 'not exists'
for f in os.listdir(folder_path):
		file_path = os.path.join(folder_path,f)
		if os.path.isdir(file_path):
			merge(file_path)
		else:
			merge_file = open('/tmp/merge_test','ab+')
			content = open(file_path,'r').read()
			merge_file.write(content)
			merge_file.close()
merge('/tmp/5')

#习题3
def get_url_count(url):
	if not (url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	d = urllib.urlopen(url)
	content = d.read()
	return len(content.split('<a href=')) - 1
print get_url_count('http://news.baidu.com/')
##习题4
def qs(url):
	query = urlparse.urlparse(url).query
	return dict([(k,v[0]) for k,v in urlparse.parse_qs(query).items()])
print qs('http://126.com')
print qs('http://api/api?f=5&g=6&y=5')
print qs('http://api/api?11=53')
##习题5
#使用递归去解决
def delete(folder_path):
	if not os.path.exists(folder_path):
		return 'not exists'
for f in os.listdir(folder_path):
		file_path = os.path.join(folder_path,f)
		if os.path.isdir(file_path):
			delete(file_path)
		else:
			os.remove(file_path)
delete('/tmp/5')


---------------------进阶习题9------面向对象3--------------------------------

题目一： 写一个网页数据操作类。完成下面的功能：

提示：需要用到urllib模块

get_httpcode()获取网页的状态码，返回结果例如：200,301,404等 类型为int 

get_htmlcontent() 获取网页的内容。返回类型:str

get_linknum()计算网页的链接数目。


题目二：

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()

体会下这段代码，把结果的执行流程用自己的话写下。
结果为：
>>>
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)
Salary: "30000"
Marks: "75"


t = Teacher('Mrs. Shrividya', 40, 30000)#初始化是在程序指定对象时就开始运行，运行结果为：
>>>
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)


s = Student('Swaroop', 22, 75)#初始化是在程序指定对象时就开始运行，运行结果为：
>>>
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

members = [t, s]
for member in members:
    member.tell()#子类的tell()代码会覆盖父类的tell(),这就是继承的多态
>>>
Salary: "30000"
Marks: "75"



---------------------进阶习题10------常用模块--------------------------------
习题一：
 
1.1 用time模块获取当前的时间戳.

import time
time.strftime("%Y%m%d %H:%M:%S")


>>> time.strftime("%Y%m%d %H:%M:%S")
'20170621 16:07:08'

>>> time.time()
1498032024.656186

1.2 用datetime获取当前的日期，例如：2013-03-29

from datetime import date
print date.today()


>>> date.today()#两个效果相当
datetime.date(2017, 6, 21)
>>> date.fromtimestamp(time.time())
datetime.date(2017, 6, 21)


1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27

习题二:
1 用os模块的方法完成ping www.baidu.com 操作。

>>> import os
>>> os.system('ping www.baidu.com')

>>> import subprocess
>>> subprocess.call('ping www.baidu.com',shell=True)

2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，如果有2个".py"的扩展名，则返回一个".py"。

import os
def kouzhang(dirpwd):
	if not os.path.isdir(dirpwd):
	    return "Please input a exist dir"
	c=os.listdir(dirpwd)
	return c
print kouzhang('/users/captain/desktop')

习题三：

定义一个函数xulie(dirname,info) 参数：dirname:路径名，info:需要序列化的数据，功能：将info数据序列化存储到dirname路径下随机的文件里。  

#答案如是：
import os
import pickle,random
def xulie(dirname,info):  
    if not os.path.exists(dirname):  
        return 'Not found!'  
    a = pickle.dumps(info)  
    filename = ''
    for i in range(10):  
        filename=filename+random.choice('abcedfghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ1234567890')  
    filepath = os.path.join(dirname,filename)  
    f = open(filepath,'a+')  
    f.write(a)
    f.close()  
a=[1,2,3,4,5,6,7]  
xulie('/users/captain/desktop',a)


---------------------进阶习题11------异常处理1--------------------------------
1 定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。

def func(filename):
	try:
		f=open(filename,'r')
		return f.read()
	except IOError:
		return 'Open file Error'
	else:
		pass
	finally:
		if 'data' in locals():#如果文件存在本地缓存，就关闭这个文件
			f.close()
print func('/users/captain/desktop/a.txt')

#或者直接用with的内置方法抛异常
def func(filepath):
	with open(filepath,'r') as f:
		return f.read()
2 定义一个函数func(urllist)   urllist:为URL的列表，例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...] 

函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。

#不知道这儿异常处理得对不对
import urllib2
def func(urllist):
	for i in urllist:
		try:
			res=urllib2.urlopen(i)
			return res.readlines()
		except:
			file_log=open('/users/captain/desktop/error.log', 'a+')
			file_log.write(str(res.getcode())+'Error\n')
			return 'Error'
print func(['http://www.baidu.com','http://www.qq.com'])


#网友答案：
import logging #内置日志模块
logger = logging.getLogger()#定义logging对象
hdlr = logging.FileHandler('/tmp/sendlog.txt')#定义文档生成路径
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')#存储的格式：时间，等级，信息
hdlr.setFormatter(formatter)#引入格式到hdlr文件对象
logger.addHandler(hdlr)#将文件对象引入日志模块中
logger.setLevel(logging.NOTSET)#设置日志的等级
import urllib
def func(urllist):
	for i in urllist:
		try:
			u=urllib.urlopen(i)
		except IOError:
			logging.error
		else:
			return u.read()
		finally:
			u.close()
print func(['http://www.baidu.com','http://www.qq.com'])

3 定义一个函数func(domainlist)   domainlist:为域名列表，例如：['xx.com','www.xx.com','www.xxx.com'...]
函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法），这儿可以延伸一个需求：根据返回的时间对网址进行排序

#ping 普通的ip地址没问题，但如果有管道（恶意代码）的话，结果就很惨，所以ping地址一般会先检测ip
ping 126.com#这儿正常
ping 126.com | rm-r /tmp/test#这儿就会直接删除掉/tmp/test目录下所有文件
import os
def func(domainlist):
	for i in domainlist:
		try:
			os.system('ping -c 4 %s'%i)#这儿的意思是：ping 4次后终止
		except:
			pass#内容还不知道怎么写



---------------------进阶习题12------异常处理2--------------------------------

习题：
1，定义一个函数func(filename) filename:为文件名，用with实现打开文件，并且输出文件内容。

2，定好一个函数func(listinfo) listinfo:为列表，listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555] 返回一个列表包含小于100的偶数，并且用assert来断言
返回结果和类型。

3，自己定义一个异常类，继承Exception类, 捕获下面的过程：判断raw_input()输入的字符串长度是否小于5，如果小于5，比如输入长度为3则输出:" The input is of length 3,expecting at least 5'，大于5输出"print success'


---------------------进阶习题13------异常处理3-------------------------------
异常习题：
 
 一 编写with操作类Fileinfo()，定义__enter__和__exit__方法。完成功能：

 1.1 在__enter__方法里打开Fileinfo(filename)，并且返回filename对应的内容。如果文件不存在等情况，需要捕获异常。

 1.2 在__enter__方法里记录文件打开的当前日期和文件名。并且把记录的信息保持为log.txt。内容格式："2014-4-5 xxx.txt"


 二：用异常方法，处理下面需求：

 info = ['http://xxx.com','http:///xxx.com','http://xxxx.cm'....]任意多的网址

 2.1 定义一个方法get_page(listindex) listindex为下标的索引，类型为整数。 函数调用：任意输入一个整数，返回列表下标对应URL的内容，用try except 分别捕获列表下标越界和url 404 not found 的情况。 

 2.2 用logging模块把404的url，记录到当前目录下的urlog.txt。urlog.txt的格式为：2013-04-05 15:50:03,625 ERROR http://wwwx.com 404 not foud、


 三：定义一个方法get_urlcontent(url)。返回url对应内容。

 要求：
 
 1自己定义一个异常类，捕获URL格式不正确的情况，并且用logging模块记录错误信息。

 2 用内置的异常对象捕获url 404 not found的情况。并且print 'url is not found'


--------------------------进阶习题14------多线程1------------------------


习题：


习题一：已知列表 info = [1,2,3,4,55,233]

生成6个线程对象,每次线程输出一个值，最后输出："the end"。

import threading
import time
def test(p):
	# time.sleep(0.01)
	print p
info = [1,2,3,4,55,233]
ts=[]
for i in info:
	th = threading.Thread(target=test,args=[i])
	th.start()
	ts.append(th)
for i in ts:
	i.join()
print "the,end!!!!!"


习题二：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
#这个函数运行结果有错
import urllib
import re
import threading
def get_url(url):
	u=urllib.urlopen(url).read()
	re_title='<title>(.*)</title>'#这儿取title最好加一个head标签，避免取到其他地方去了
	title=re.findall(re_title,u)
	print title
urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
ul=[]
#这儿应该用队列queue生成线程最好在50-100个，这样能满足实际需求中爬取多个url的需求
for i in xrange(0,len(urlinfo)):
	th=threading.Thread(target=get_url, args=urlinfo[i])
 	th.start()
 	ul.append(th)
for i in ul:
	i.join()

习题三：已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 用多线程的方式分别打开列表里的URL，输出网页的http状态码。
#此代码运行有错，其中的相关改正策略参考上一题
import urllib
import threading
def get_code(url):
	u=urllib.urlopen(url)
	print u.get_code
urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
ts=[]
for i in xrange(0,len(urlinfo)):
	th=threading.Thread(target=get_code,args=urlinfo[i])
	th.start()
	ts.append(th)
for i in ts:
	i.join()

--------------------------进阶习题14------多线程2------------------------
习题：

有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500

用多线程的方式来解决，提示需要用到这节课的内容

import threading
mlock = threading.Lock()
num = 500#初始化
def a():
	global num	
for i in xrange(0,100):
		mlock.acquire() #加锁,这儿的锁最好应该放在一个线程里面，而不是循环里面
		num += 1 #收入+1
		mlock.release() #释放锁
	return num
	
ts=[]
for i in xrange(0,10):
	d = threading.Thread(target=a)
	d.start()
	ts.append(d)
for i in ts:
	i.join()
print'the total revenue = %s'%num
#优化后：加锁应该放在一个线程里面，从而提升它的性能，性能可以导入时间模块，来通过时间长短来判断性能：
import threading
mlock = threading.Lock()
num = 500#初始化
def a():
	global num	
	mlock.acquire() #加锁
	for i in xrange(0,100):
		num += 1 #收入+1
	mlock.release() #释放锁
	return num
	
ts=[]
for i in xrange(0,10):
	d = threading.Thread(target=a)
	d.start()
	ts.append(d)
for i in ts:
	i.join()
print'the total revenue = %s'%num

--------------------------进阶习题15------多线程3------------------------

习题一：

定义一个生成器函数，函数里只能用yield，要求输出结果：

step 1
step 2 x=haha
step 3 y=haha

提示步骤：建立生成器对象，并且用对象的next()和send()方法来输出结果。send()方法传入的参数是"haha"

def test():
	x=yield 'step1'
	x=yield 'step2 x=%s'%x
	x=yield 'step3 y=%s'%x
t=test()
print t.next()
print t.send('haha')
print t.send('haha')


习题二：用生成器yield实现斐波拉切数列。

def fun(x):
	i=1
	j=1
	k=i+i
	if x>0:
		yield i
		yield j
	else:
		yield 'arguments gets wrong, pls check!'
	while k<=x:
		yield k
		i=j
		j=k
		k=i+j
for i in fun(13):
	print i


--------------------------进阶习题15------协程yeid解决问题------------------------
1.写一个函数，输出某个范围内的质数
#参考：http://blog.csdn.net/recsysml/article/details/51321517
import math
import time
old=time.time()
def is_p(t):
	'''
	1、质数：只能被1和本身整除的数，
		那么被其他整除的数就不是了；
		1.可以优先考虑一些特殊的被整除数字，比如2,3,5
		2.再考虑0--这个数的平方根之间的数来坐除数
	2、且1不是质数
	'''	
	if t<=0 or t==1:
		return False
	elif t==2 or t==3:#排除xrange(2,2)为[]的状况
		return True
	else:
		m=int(math.sqrt(t))+1#开方运算这种方法最节省时间
		for i in xrange(2,m):
			if t%i==0:
				return False
		return True
def plist(min,max):
	pli=[i for i in xrange(min,max) if is_p(i)]
	return pli
print plist(0,1000)
print 'time=%s'%(time.time()-old)

#上面只考虑了平方根做除数的状况，下面程序把上面的都考虑进去：
import math
import time
old=time.time()
def prime(n):  
    if n==1:
    	return 0
    if n%2 == 0:
        return n==2  
    if n%3 == 0:  
        return n==3  
    if n%5 == 0:  
        return n==5  
    for p in xrange(7,int(math.sqrt(n))+1,2):  #只考虑奇数作为可能因子  
        if n%p == 0:  
            return 0  
    return 1  
if __name__ == "__main__": 
	def plist(min,max):
		pli=[i for i in xrange(min,max) if prime(i)]
		return pli
	print plist(0,100)
	print 'time=%s'%(time.time()-old)

#用埃氏筛法：
#百度百科，表示没理解程序
def primes(n):
    P = []
    f = []
    for i in range(n+1):
        if i > 2 and i%2 == 0:
            f.append(1)
        else:
            f.append(0)
    i = 3
    while i*i <= n:
        if f[i] == 0:
            j = i*i
            while j <= n:
                f[j] = 1
                j += i+i
        i += 2
 
    P.append(2)
    for x in range(3,n+1,2):
        if f[x] == 0:
            P.append(x)
 
    return P
n = 100   #100以内的素数
P = primes(n)
print P

#参考方法，表示没理解程序
import sys  
import time
old=time.time()  
def prime(n):  
    flag = [1]*(n+2)  
    p=2  
    while(p<=n):  
        print p  
        for i in range(2*p,n+1,p):  
            flag[i] = 0  
        while 1:  
            p += 1  
            if(flag[p]==1):  
                break  
# test  
if __name__ == "__main__":  
    # n = int(sys.argv[1])  
    prime(100)
    print 'time=%s'%(time.time()-old)

#程序另一种写法
def findprime(L):
    i = 0
    count = 0
    while L[i] ** 2 < L[-1]:
        for j in range(i + 1,len(L)):
            if L[j] % L[i] == 0:
                L[j] = 0
                count += 1
        L.sort()
        L = L[count:]
        count = 0
        i += 1
    return L
L = range(2,10000)
prime = findprime(L)
print prime



2.用yeild写一个函数，输出1亿以后100个质数

--------------------------进阶习题16------正则表达式1------------------------
作业：
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'
用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"

import re
relink = '<a href="(.*)">(.*)</a>'
info = '<a href="http://www.baidu.com">baidu</a>'
cinfo = re.findall(relink,info)
print cinfo
>>>
[('http://www.baidu.com', 'baidu')]


2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
import re
relink = '\d'
info = "one1two2three3four4"
cinfo = re.findall(relink,info)
print ''.join(cinfo)

3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。

4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。

--------------------------进阶习题17------正则表达式2------------------------
1.已知字符串：

info = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'

要求完成下面2个小功能：
1.1 关闭[img]标签
1.2 将url()中的["]转为[']

最后结果字符串：
"test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"


2.用re模块对字符串e='a1b2c3d4e5f'按英文字母分割为['1','2','3','4','5']

3.学习re模块中的：match，查找全部 findall，以及finditer 迭代器

-------------------------进阶习题18------多线程网络资源访问------------------------

作业1：

url :"http://money.163.com/special/pinglun/"
抓取第一页的新闻信息，并按照以下规格输出。

[ {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

  {'title':'生鲜电商为何难盈利？','created_at':'2013-05-03 08:43','url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}]

#网友答案，测试不正确
import urllib
import re
def search(url):
	f=urllib.urlopen(url).read()
	regex=re.compile('''<li><span class="article"><a href="([^"]+?)">([^<]+?)</a></span><span class="atime f12px">\(([^\])+?\)</span></li>''')
	result=re.findall(regex,f)
d_list=[]
for l in result:
	d_list.append({'title':l[1],'created_at':l[2],'url':l[0]})
return d_list


作业2：

url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"


print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}

#网友答案
import urllib
import re
url="http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"
def get_price(id):
	f=urllib.urlopen(url).read()
	regex=re.compile('''chameImgPrice2Num\(([^\]+?)\);''')
	result=re.match(regex,f)
	decodejson=json.loads(result.group(1))
	return decodejson[0]['p']
	#1.正则匹配比较难写re.compile
	#2.title格式化费脑筋，最后用re.sub搞定
	#3.字典的浅拷贝，深拷贝问题
def jd_search(keyword):
	f=urllib.urlopen(url).read()
	regex=re.compile('''xxxx''')
	result=re.findall(regex,f)
	.....

作业3：
使用beatifulsoup完成作业1的要求.


作业4：
使用scrapy完成作业2的需求。
jd_search(keyword,page_skip=1,page_limit=10) #抓1后面10页（包括第10页）的内容。
jd_search(keyword,page_skip=4,page_limit=3) #抓4后面3页（包括第6页）的内容。



-------------------------进阶习题19------http协议，用python建一个服务器----------------
作业：
用python的内库wsgiref写一个hello world，
在浏览器中输入：
http://localhost:8000， 显示hello,world
http://localhost:8000/c， 显示c,hello,world
http://localhost:8000/d， 显示d,hello,world
http://localhost:8000/e， 显示e,hello,world

'''
编写hello.py
编写server.py
放置在同一个文件夹，并执行python server.py
在浏览器中输入对应的地址，可以呈现对应的效果
'''

# hello.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    if not environ['PATH_INFO'][1:]:
        return '<h1>hello, world!</h1>'
    else:
        return '<h1>%s, hello, world!</h1>' % (environ['PATH_INFO'][1:])


# server.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application) 
print "Serving HTTP on localhost port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()



-------------------------进阶习题综合运用---------最后一节------------------------
"""

童鞋们好，我们的进阶课终于要讲完了。这里，留给大家一道进阶篇的结束题。要求如下：


【准备步骤】
1.申请一个微博的开发者账号，http://open.weibo.com/apps
2.为新申请的开发者账号，添加几个测试账号
3.找到新浪的python sdk 



【需求】

1.已知一个网站 http://c/， 网站名为 “鞋推网”
2.网站使用微博的账号密码登陆。
3.登陆成功后，显示京东网 搜索 鞋子 的第一页结果列表。（如果能分页肯定更好了，但不强求）

3.1 结果列表中需包含图片，名字。
3.2 图片需存储在本地。


4.点击列表中的任意一个图片后，立即分享到新浪微博。（使用哪个账号登陆，就使用那个账号发一个微博）微博内容如下

“我在鞋推网为我推荐了一双鞋子[鞋子的名字]，哈哈。http://c/”
此信息后附一张鞋图片


【完成】
给大家10天的时间。之后我们开始讲解这道结业题。

"""
这道题综合了我们以前所有的知识。

