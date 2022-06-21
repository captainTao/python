
===========================================
文件读写
--------
打开文件，先try一下，看能不能获取到文件路径

>>> f = open('/Users/michael/test.txt', 'r')
>>> f.read()
'Hello, world!'
>>> f.close()
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的;
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    print(f.read())
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


字符编码
--------
# 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
>>> f = open('/Users/michael/gbk.txt', 'rb')
>>> u = f.read().decode('gbk')
>>> u
u'\u6d4b\u8bd5'
>>> print u

# 如果每次都这么手动转换编码嫌麻烦,Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'


当我们需要调用系统的命令的时候，最先考虑的os模块。用os.system()和os.popen()来进行操作。

open(name[, mode[, buffering]])
name参数表示需要打开的文件名称，mode是打开模式，open()函数的第三个参数用来控制文件的缓冲，默认值为0，表示不缓冲，设置为1就会有缓冲。以下是open()函数的几个模式值
参数                   描述
r             读取模式打开文件
w             读写模式打开文件
a             写入模式打开文件
b             二进制模式打开文件(可以和其他模式并用)
+             读/写模式(可以和其他模式并用)
U             支持换行符(例如：\n、\r 或 \n\r 等)
rb            以字节的模式读取文件
wb            以二进制的模式写文件


 操作文件和目录

>>>os.path.exists(path) #判断路径是否存在
>>>os.listdir(path) #列出path路径下的所有文件
>>>os.path.isdir(path) #判断路径是否是文件夹
>>>os.path.isfile(path) #判断路径是否是文件
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')


# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir') #不要直接拼字符串，而要通过os.path.join()函数，在Linux/Unix/Mac下，返回：part-1/part-2；而Windows下会返回：part-1\part-2
'/Users/michael/testdir'
# 拆分路径，不能直接拆字符串，而要通过os.path.split()函数
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
>>> fileDir = "F:" + os.sep + "aaa"  # 查找F:\aaa 目录下

# 对文件的操作
# Note:复制文件的函数不在os模块中,幸运的是shutil模块提供了copyfile()的函数，还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')

利用Python的特性来过滤文件
# 比如我们要列出当前目录下的所有目录，只需要一行代码：
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Adlm', 'Applications', 'Desktop', ...]
要列出所有的.py文件，也只需一行代码：
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径
#Linux查看当前目录下所有文件及子目录文件：ls -la -R

#搜索对应路径下的对应文件类型
#这儿用的os.path.splitext,只能搜索文件类型
import os
path=raw_input("pls input search path:")
def search(s):
    if os.path.exists(s):
        fileext=raw_input('pls input search file type .*:')
        for dirpath,dirnames,filenames in os.walk(s):
        # 这个方法为3元tuple第一个参数为起始路径;第二个为起始路径下的文件夹;第三个是起始路径下的文件.
            for filename in filenames:
                if os.path.splitext(filename)[1]==fileext:
                    print (os.path.join(dirpath,filename))
    else:
        print('dir_error')
search(path)


#用os.listdir, os.path.isfile, os.path.isdir
import os
name=raw_input('please input the search name:')
path=raw_input('please input the search path:')
def seach(name, path=os.path.abspath('.')):
    for x in os.listdir(path):
        path_now = os.path.join(path, x)
        if os.path.isfile(path_now) and name in x:
            print path_now
        elif os.path.isdir(path_now):
            seach(name, path_now)#递归
seach (name,path)


#用os.walk, os.sep
import os
def search(name, path='.'):
        abspath=os.path.abspath('.')
        for i in os.walk(abspath):
                for y in [ x for x in i[2] if name in x ]:
                        print i[0]+os.sep+y
search('hello.py','/Users/captain/Desktop')


-----------------------------------------------------------------------------------------
读写文件或文本：
读方法一：
d=open ('name.txt', 'w')  //第二个为打开方式 r：read,  w:write , a:append
d.write('hi.\nsecond hi.')  //只能写字符串
d.close()
d=open('name.txt','r')
print d.readline()  //依次读取每一行的内容, read()是全部读取
print d.read(100)  //读取100个size

d.seek(0)  //光标定位到文本的第一个位置

# 三种表达方式：用line和readlines
# NO.1：
f = open("foo.txt")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    print line,                 # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()                    # 调用下一次readline()
f.close()
# No.2：
for line in open("foo.txt"):
    print line,
# NO.3：
f = open("c:\\1.txt","r")
lines = f.readlines()#读取全部内容
for line in lines
    print line

读方法二：
# 用with方法
def get_text(f):
    with open(f, 'r') as g:
        return g.read()
print get_text('/Users/captain/desktop/a.txt')
读方法三：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
d=open ('name.txt', 'w')
d.write("this is my iphone!\nenheng, python is easy and good\nwe should study hard\n")
d.close()

d=open('name.txt','r')

import linecache
print linecache.getline('name.txt',1)#读第一行
print linecache.getline('name.txt',2)#读第二行
print linecache.getline('name.txt',3)#读第三行
print linecache.getlines('name.txt')#全部读出来，并生产一个list



写方法一：重定向
#!/usr/bin/env python
# -*- coding: utf-8 -*-
f=open.('print.txt', 'w')
print >>f,"hahhahhaha",     #>>位移符号就是重定向，对文件写入后面的字符
print >>f,"xixixixixixi"
f.close()

写方法二：传统
g=open('a.txt', 'w')#这儿是传统方法
g.write('hahhhah')
g.close()
#然后运行这个py文件，再打开生成的txt文件即可看到输出结果
写方法三：with方法
#以上用with代替：
with open('a.txt', 'a') as g:#这儿‘a’的作用相当于“appnend”在文最后面进行追加
    g.write('xixi')#括号内为追加的内容，它不需要关闭文件
#然后运行这个py文件，再打开生成的txt文件即可看到输出结果




------------------------------------
一、计算文件的行数
   最简单的办法是把文件读入一个大的列表中,然后统计列表的长度.如果文件的路径是以参数的形式filepath传递的,那么只用一行代码就可以完成我们的需求了:
count = len(open(filepath,'rU').readlines())

   如果是非常大的文件,上面的方法可能很慢,甚至失效.此时,可以使用循环来处理:
count = -1
for count, line in enumerate(open(thefilepath, 'rU')):
    pass
count += 1

  另外一种处理大文件比较快的方法是统计文件中换行符的个数'\n  '(或者包含'\n'的字串,如在windows系统中):
count = 0
thefile = open(thefilepath, 'rb')
while True:
    buffer = thefile.read(8192*1024)
    if not buffer:
        break
    count += buffer.count('\n')
thefile.close( )

   参数'rb'是必须的,否则在windows系统上,上面的代码会非常慢.(图片和视频都是二进制)
linecache是专门支持读取大文件，而且支持行式读取的函数库。 linecache预先把文件读入缓存起来，后面如果你访问该文件的话就不再从硬盘读取

二、读取文件某一行的内容（测试过1G大小的文件，效率还可以）
import linecache
count = linecache.getline(filename,linenum)

三、用linecache读取文件内容（测试过1G大小的文件，效率还可以）
str = linecache.getlines(filename)
str为列表形式，每一行为列表中的一个元素


# 文件中有字符编码
# 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
>>> f = open('/Users/michael/gbk.txt', 'rb')#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
>>> u = f.read().decode('gbk')
>>> u
u'\u6d4b\u8bd5'
>>> print u
# 如果每次都这么手动转换编码嫌麻烦（写程序怕麻烦是好事，不怕麻烦就会写出又长又难懂又没法维护的代码），Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'


#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')




如下的案例：
同时打开三个文件，文件行数一样，要求实现每个文件依次读取一行，然后输出，我们先来看比较容易想到的写法：
with open(filename1, 'rb') as fp1:
    with open(filename2, 'rb') as fp2:
        with open(filename3, 'rb') as fp3:
            for i in fp1:
                j = fp2.readline()
                k = fp3.readline()
                print(i, j, k)

注意这里只能对单个文件进行for循环读取，不能写成：
for i, j, k in fp1, fp2, fp3:
    print(i, j, k)

但可使用强大的zip操作：

for i, j, k in zip(fp1, fp2, fp3):
    print(i, j, k)

这样层层的嵌套未免啰嗦，with结构支持一种更简洁的写法：

with open(filename1, 'rb') as fp1, open(filename2, 'rb') as fp2, open(filename3, 'rb') as fp3:
    for i in fp1:
        j = fp2.readline()
        k = fp3.readline()
        print(i, j, k)

或者使用更为优雅的写法，此时需要contextlib语法糖：

from contextlib improt ExitStack
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in [filename1, filename2, filename3]]
    for i, j, k in zip(files[0], files[1], files[2]):
        print(i, j, k)




try expect处理异常
------------------

if instance(i, int)： #判断i的类型
assert 3==1+2 #判断为true还是false，true的话不执行任何操作，false则抛出异常；
python -O xxx.py # -O[大写]会关闭assert，当做pass来处理
try...except.. #常见程序错误

try except处理程序异常的三种常用方法
常见错误类型以及继承关系： https://docs.python.org/2/library/exceptions.html#exception-hierarchy

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
       +-- ImportWarning
       +-- UnicodeWarning
       +-- BytesWarning

try:
    pass#抛出异常的代码
except Exception as e:
    raise #抛异常执行这,一般会打log,可以写多个except,执行多个异常
else:
    pass#没抛异常，执行这
finally:
    pass#不管异常与否，都执行这

try:
    pass
except Exception as e:
    raise
    logging.debug(e)#一般会打log
else:
    return url_info
finally:
    pass


import urllib
sth_url = "http://wasdasdasd"
try:
    d = urllib.urlopen(sth_url)
except IOError:
    print "哈哈哈出错了"
except 语法错误的异常:
    print '这儿出错'
else:
    content = d.read()
finally:
    d.close()
如果你在写python程序时遇到异常后想进行如下处理的话,一般用try来处理异常，假设有下面的一段程序：
1   try:
2       语句1
3       语句2
4       .
5       .
6       语句N
7   except .........:
8       do something .......
但是你并不知道"语句1至语句N"在执行会出什么样的异常，但你还要做异常处理，且想把出现的异常打印出来，并不停止程序的运行，所以在"except ......"这句应怎样来写呢？
总结了一下3个方法：
方法一：捕获所有异常
1   try:
2       a=b
3       b=c
4   except Exception,e:
5       print Exception,":",e
方法二：采用traceback模块查看异常
1   #引入python中的traceback模块，跟踪错误
2   import traceback
3   try:
4       a=b
5       b=c
6   except:
7       traceback.print_exc()
方法三：采用sys模块回溯最后的异常
1   #引入sys模块
2   import sys
3   try:
4       a=b
5       b=c
6   except:
7       info=sys.exc_info()
8       print info[0],":",info[1]
但是，如果你还想把这些异常保存到一个日志文件中，来分析这些异常，那么请看下面的方法：
把　traceback.print_exc()　打印在屏幕上的信息保存到一个文本文件中
1   import traceback
2   try:
3       a=b
4       b=c
5   except:
6       f=open("c:log.txt",'a')
7       traceback.print_exc(file=f)
8       f.flush()
9       f.close()

异常处理2：
raise TypeError, 'not a str Type'

------------------------------------------------


1.异常的几点注意
    一个try就有一个except

    1.1 不要没事就乱用异常
        慎用异常： 1.找到python的内置异常
                 2.理解python的内置异常分别对应什么情况
                3.阅读你的代码，找到你的代码里可能会抛出内置异常的地方
                 4.仅对这几行代码做异常处理

    假设你无法知道你的代码会抛出什么异常，那么，你的异常处理便是无效的。——> 准确了解你的代码情况。

    1.2 不要一个代码块，大try完事。
    1.3 好吧，如果想try all exception？用这个方法：sys.exc_info()
    1.4 logging如何使用呢


1.3
import sys
try:
    a=3
    assert a==4,'erro message'
except:
    exc=sys.exc_info()
    print exc[1]#取tuple的第二个元素
    print exc#返回的是一个tuple

>>>
erro message
(<type 'exceptions.AssertionError'>, AssertionError('erro message',), <traceback object at 0x10b39e128>)

1.4
import sys
import logging
try:
    a=3
    assert a==4,'erro message'
except:
    exc=sys.exc_info()
    logging.error(exc[1])
>>>
ERROR:root:erro message


#logging的一个套用格式：

import logging #内置日志模块
logger = logging.getLogger()#定义logging对象
hdlr = logging.FileHandler('/tmp/sendlog.txt')#定义文档生成路径
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')#存储的格式：时间，等级，信息
hdlr.setFormatter(formatter)#引入格式到hdlr文件对象
logger.addHandler(hdlr)#将文件对象引入日志模块中
logger.setLevel(logging.NOTSET)#设置日志的等级


然后用下面的方式就可以直接引用
logger.debug('this is a debug message')

下面就是等级比较高的error
logger.error('this is an error message')

它这有三个等级：
logging.debug
logging.error
logging.info

查看对应的log可以用如下方法(直接在命令行下输入即可)：
cat filepath


2.断言，一种开发期时检定代码的方式
    只断言绝对不能出现的错误 twisted

    先断言绝对不能发生的错误
    然后，再去处理错误 （异常）

    assert 表达式， "出错以后抛出的message"

    1 > 4
    3 > 2
    1 == 2


3.代码友好，自动处理垃圾,with.

d=open('a','r')
d.read()
d.close()
#with方法可以省略掉关闭文件的那一步骤
with open('a','r') as g:
    e=g.read()
print 4
进入时，调用对象的__enter__方法
退出时，调用对象的__exit__方法


#自己定义程序执行和退出的时候执行的内容
class sth(object):
    def __enter__(self):
        print '呵呵呵，进来了'
    def __exit__(self,type,value,traceback):#括号内的参数是必须的
        print u'哈哈哈，出去了'
with sth() as s:#s是__enter__返回的东西
    pass


class sth(object):
    """docstring for sth"""
    def __init__(self, arg):
        super(sth, self).__init__()
        self.arg = arg
    def __enter__(self):
        print '我进来了'
        print self.arg
        return self.arg
    def __exit__(self,type,value,traceback):
        print '我出去了'
with sth('a test demo') as g:
    print g
>>>
我进来了
a test demo
a test demo
我出去了


4.自己定义异常？继承exception类。


class myException(Exception):#继承exception的属性
    """docstring for myException"""
    def __init__(self, error,msg):
        self.args = (error,msg)
        self.error = error
        self.msg = msg
try:
    raise myException(1,'my exception')
except Exception as e:
    print str(e)


-------------------------------------------------


# Python内置的logging模块可以非常容易地记录错误信息：
# err.py
import logging
def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)
main()
print 'END'
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

class FooError(StandardError):# 自定义error的继承
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo(0)


import logging
logging.basicConfig(level=logging.INFO) # 有debug，info，warning，error等几个级别
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n



'''写一个方法，让Dict可以像一个对对象的属性一样，调用对应的key'''
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value): #设置对应的属性
        self[key] = value
'''
#定义方式一：
# d = Dict(name='kaka',age='22')
# print d.age
#定义方式二：
d = Dict(**{'name':'kaka','age':'22'})
print d.name
print d.school #抛异常
d.school='Huaxi Middle School'
print d.school
'''
'''如下为单元测试的内容'''
import unittest
# from mydict import Dict
class TestDict(unittest.TestCase): #继承unittest.TestCase
    def test_init(self):  #检测初始化get方法：
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self): #检测set方法
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')
    def test_attr(self): #检测set方法
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):#访问不存在的key时抛出keyError
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError): #通过d.empty访问不存在的key时，我们期待抛出AttributeError
            value = d.empty
if __name__=='__main__':
    unittest.main(verbosity=2)

