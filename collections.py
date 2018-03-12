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





#用zip函数求出频率最高的单词，这里用字典模拟创建好的单词和频率对应关系
>>> from random import randint
>>> d={x:randint(60,100) for x in 'xyzadb'}
>>> d
{'a': 94, 'b': 96, 'd': 66, 'y': 99, 'x': 85, 'z': 82}
>>> zip(d.values(),d.keys())
[(94, 'a'), (96, 'b'), (66, 'd'), (99, 'y'), (85, 'x'), (82, 'z')]
>>> sorted(zip(d.values(),d.keys()),reverse=True)
[(99, 'y'), (96, 'b'), (94, 'a'), (85, 'x'), (82, 'z'), (66, 'd')]


>>> from random import randint, sample
>>> sample('abcdefg',3) # 在abcdefg中随机3个数
['d', 'b', 'g']

>>> sample('abcdefghi',randint(3,6))# 在abcdefghi中随机3到6个数
['g', 'f', 'b', 'd', 'h', 'c']

>>> {x:randint(5,10) for x in sample('abcdefgh',randint(3,6))}# 在abcdefgh中随机3到6个数为key, value在5-10之间随机
{'a': 5, 'e': 9, 'g': 9}


>>> d
{'a': 94, 'b': 96, 'd': 66, 'y': 99, 'x': 85, 'z': 82}
>>> d.keys()# 得到的是一个数组list
['a', 'b', 'd', 'y', 'x', 'z']

>>> d.viewkeys()# 得到的是一个集合set
dict_keys(['a', 'b', 'd', 'y', 'x', 'z'])

# 系统的字典是无序的，如果要用有序的，就用collections的OrderDict
>>> from collections import OrderedDict
>>> d=OrderedDict()
>>> d['a']=3
>>> d['c']=21
>>> d['h']=33
>>> d['b']=12
>>> d
OrderedDict([('a', 3), ('c', 21), ('h', 33), ('b', 12)])

# collections中的队列可以用来记录最近几条的历史记录
>>> from collections import deque
>>> sequece=deque([],5)  # 创建5个初始为空的list
>>> sequece.append(1)
>>> sequece.append(2)
>>> sequece.append(3)
>>> sequece.append(4)
>>> sequece.append(5)
>>> sequece.append(6)
>>> sequece.append(7)
>>> sequece
deque([3, 4, 5, 6, 7], maxlen=5)  # 只记录了最近5条

具体内容可以参考collections模块：
>>> import collections
>>> dir(collections)
['Callable', 'Container', 'Counter', 'Hashable', 'ItemsView', 'Iterable', 'Iterator', 'KeysView', 'Mapping', 'MappingView', 'MutableMapping', 'MutableSequence', 'MutableSet', 'OrderedDict', 'Sequence', 'Set', 'Sized', 'ValuesView', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_abcoll', '_chain', '_class_template', '_eq', '_field_template', '_get_ident', '_heapq', '_imap', '_iskeyword', '_itemgetter', '_repeat', '_repr_template', '_starmap', '_sys', 'defaultdict', 'deque', 'namedtuple']

===============================================================================


>>> dir(dict)
>>> [ 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']


>>> dict1={'name':'wuya','age':20,'address':'xian'}
>>> dict1.fromkeys(['name','age'],('wuya',18))#利用fromkeys生成新的字典
{'age': ('wuya', 18), 'name': ('wuya', 18)}

>>> dir(set)
>>> ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']



'''
python实现冒泡排序:
---很恶心哈，python没有for(int i = 0;i<len(list);i++){}之类的代码，
sort不用，多次一举....
'''

# import random
def bubblesort(target):
    length = len(target)
    while length > 0:
        length -= 1
        cur = 0
        while cur < length: #拿到当前元素
            if target[cur] > target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
if __name__ == '__main__':
    a = [random.randint(1,100) for i in range(10)]
    print bubblesort(a)




