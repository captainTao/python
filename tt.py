#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
如何统计序列中元素出现的频度？
1.某随机序列【12，5，6，4，6，5，5，7，...】中，找到出现次数最高的三个元素，他们出现的次数是多少？
2.对某英文文章的单词，进行次频统计，找到出现次数最高的10个单词，他们出现的次数是多少？

解决方法： 
一、直接遍历，然后统计
二、使用collections.Counter对象
讲序列传入Counter的构造器，得到Counter对象是元素频度的字典
Counter.most_common(n)方法得到频度最高的n个元素列表；
'''
# 1：直接遍历
from random import randint
data=[randint(0,20) for _ in xrange(30)] #从0到20之间随机产生30个数
c=dict.fromkeys(data,0) #随机数序列一个默认值为0的字典
for x in data:
    c[x] += 1
print c

print '\n'
print '---------我是分割线----------'

# 2.用collections
from random import randint
data=[randint(0,20) for _ in xrange(30)]
from collections import Counter
c2=Counter(data)
print c2 #功能同一中的c
print c2.most_common(3) #打印出前三个频率最高的
