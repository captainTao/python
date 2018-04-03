#!/usr/bin/env python
# -*- coding: utf-8 -*-

使用type():


>>> type(123)
<type 'int'>
>>> type('str')
<type 'str'>
>>> type(None)
<type 'NoneType'>



如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：

>>> type(123)==type(456)
True
>>> type('abc')==type('123')
True
>>> type('abc')==type(123)
False


但是这种写法太麻烦，Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：

>>> import types
>>> type('abc')==types.StringType
True
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True



最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：
>>> type(int)
<type 'type'>
>>> type(int)==type(str)==types.TypeType




使用isinstance():

object -> Animal -> Dog -> Husky

>>> a = Animal()
>>> d = Dog()
>>> h = Husky()

>>> isinstance(h, Husky)
True

>>> isinstance(h, Dog)
True

>>> isinstance(d, Husky)
False


能用type()判断的基本类型也可以用isinstance()判断：

>>> isinstance('a', str)
True
>>> isinstance(u'a', unicode)
True
>>> isinstance('a', unicode)
False



并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：

>>> isinstance('a', (str, unicode))
True
>>> isinstance(u'a', (str, unicode))
True
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
True



由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：

>>> isinstance(u'a', basestring)
True



配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()

#属性
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19

>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404

#方法  也可以获得对象的方法：
>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81

/////////////////////////////////////////////////

包（__int__.py文件和模块文件）

模块的常见写法（这儿以hello.py为例）
#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a test module '#模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = 'Michael Liao'#作者
import sys#利用这个变量，可以访问sys模块的所有功能
def test():
    args = sys.argv#sys模块有一个argv变量，用list存储了命令行的所有参数。
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'
if __name__=='__main__': #当模块是被调用执行的，__name__取值为模块的名字；当模块是直接执行的，则__name__该变量取值为：__main__
    test()

# 运行hello.py看看效果：
$ python hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael!
# 如果启动Python交互环境，再导入hello模块：
>>> import hello
>>>
# 导入时，没有打印Hello, word!，因为没有执行test()函数。调用hello.test()时，才能打印出Hello, word!：
>>> hello.test()
Hello, world


别名
# 导入模块时，还可以使用别名，这样，可以在运行时根据当前环境选择最合适的模块。比如Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快，所以，你会经常看到这样的写法：
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO
# 这样就可以优先导入cStringIO。如果有些平台不提供cStringIO，还可以降级使用StringIO。导入cStringIO时，用import ... as ...指定了别名StringIO，因此，后续代码引用StringIO即可正常工作。
# 还有类似simplejson这样的库，在Python 2.6之前是独立的第三方库，从2.6开始内置，所以，会有这样的写法：
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5
# 由于Python是动态语言，函数签名一致接口就一样，因此，无论导入哪个模块后续代码都能正常工作。模块搜索路径

模块搜索路径
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python34.zip', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/plat-darwin', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages']
如果我们要添加自己的搜索目录，有两种方法：
一是直接修改sys.path，添加要搜索的目录：
>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
这种方法是在运行时修改，运行结束后失效。
第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
------------------------------------------

常用模块
1.我们去哪里找模块

python的模块库：pypi.python.org 

2.我们应该首先选择哪些的模块

首先考虑的是，内置模块
文档：http://docs.python.org/2.7/

3.常用模块

3.1 urllib urllib2 网络
3.2 datetime time 时间
3.3 os 系统
3.4 pickle  对象序列化
	常用数据交换格式 json xml 
3.5 bsddb key=>value 
3.6 logging 日志


------------------------------------------
1.模块的基本概念

导入模块，然后用help方法可以查看模块对应的功能和链接
>>> import collections
>>> help(collections)


dir(linecache)：可以查看下模块提供的方法
>>> import linecache
>>> dir(linecache)
['__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cache', 'checkcache', 'clearcache', 'getline', 'getlines', 'os', 'sys', 'updatecache']

>>> linecache.__doc__查看模块的说明
'Cache lines from files.\n\nThis is intended to read lines from modules imported -- hence if a filename\nis not found, it will look down the module search path for a file by\nthat name.\n'

>>> linecache.__file__模块文件的位置
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/linecache.pyc'

if __name__=='__main':
	#可以把测试用例放入在这里面，来测试模块是否正确
	print 'sth'


2.模块的基本操作
import linecache #这个是模块的全部导入
from module_name import method #这个是模块的部分导入
from module import all #验证之后，输入all不能用

eg:
from linecache import getlines #导入linecache的getlines方法
from linecache import * 
#*号代表会从模块的all列表中去导入，__all__ = ["getline", "clearcache", "checkcache"]

#m1.py是一个模块文件
m1.py文件的内容如下：
#coding=utf-8
__all__=['hash']
def hash():
	return 4

在另外一个文件中导入这个文件运用：
import m1
print m1.hash()

from m1 import *  #  导入*号，需要在另外一个文件中定义 __all__ =[]
print hash()


3.包的创建


包就是一个文件夹，里面有：各个模块文件，还有一个__int__.py文件
# 在包m2的文件中存在，一个url_info.py文件，和一个__int__.py文件，在m2包的外层调用url_info文件



# url_info.py文件内容如下：
def get_page():
	return "this is page"

# 外层调用
import m2.url_info
print m2.url_info

# 或者:文件名太长可以另外命名一个
import m2.url_info as url
print url
print url.get_page()# 调用文件中的方法：

#或者
from m2 import url_info
print url_info.get_page()

# import其中的方法不能这样：错误
from m2 import url_info.get_page as get_page
print get_page()
# 但可以这样：
from m2.url_info import get_page
print get_page()

#或者
#__int__.py文件中定义哪些文件可以进出，这个一般是py文件引用同层包内部的模块
__init__=['url_info']
from m2 import *
print url_info.get_page()


4.搜索模块 
#如果包内部py要引用外部其他路径的py文件
import sys
sys.path.append('path')
import name.py

------------------------------------------
查看方法的区别：
dir(list)	dir(json)#查看模块
help(type(list))	type(help(json))


pillow(PIL) # 图片处理模块：
# 安装:pip install Pillow
>>> from PIL import Image
>>> im = Image.open('test.png')
>>> print(im.format, im.size, im.mode)
PNG (400, 300) RGB
>>> im.thumbnail((200, 100)) # 用它生成缩略图
>>> im.save('thumb.jpg', 'JPEG')
# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2


from PIL import Image
# 打开一个jpg图像文件
im = Image.open('/Users/captain/desktop/720.960.jpg')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/captain/desktop/720.9602.jpg', 'jpeg')


'''其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
比如，模糊效果也只需几行代码：'''
from PIL import Image, ImageFilter
im = Image.open('/Users/captain/desktop/who.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/captain/desktop/whoi.jpg', 'jpeg')


OS

>>> dir(os.path)
['abspath', 'altsep', 'basename', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys', 'walk', 'warnings']

>>> import os
>>> os.name # 操作系统名字
'posix'
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
>>> os.uname()#这个方法在windows上不提供
('Darwin', 'huangcdeMac-mini.local', '16.6.0', 'Darwin Kernel Version 16.6.0: Fri Apr 14 16:21:16 PDT 2017; root:xnu-3789.60.24~6/RELEASE_X86_64', 'x86_64')
>>> os.environ#获取环境变量
>>>os.getenv('PATH')#获取某个环境变量的值
'/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/aria2/bin:/Users/captain/library/android/sdk/tools:/Users/captain/library/android/sdk/platform-tools'
>>>os.path.exists(path) #判断路径是否存在

pydoc:文档生成工具（打印对应模块的帮助文档）：
原始链接：http://blog.csdn.net/jerry_1126/article/details/43968231
在Python中有很多很好的工具来生成字符串文档(docstring)，比如说: epydoc、doxygen、sphinx，但始终觉得pydoc还是不错的工具，用法非常简单，功能也算不错，本文主要介绍pydoc.
pydoc是Python自带的模块，主要用于从python模块中自动生成文档，这些文档可以基于文本呈现的、也可以生成WEB 页面的，还可以在服务器上以浏览器的方式呈现！

python -m pydoc string	#windows和mac下可用
pydoc string	#mac下可用

huangcdeMac-mini:~ captain$ python -m pydoc linecache
可以查看linecache的帮助文档
  
  
pydoc -k <keyword>  在所有可用的模块中按关键词搜索
    Search for a keyword in the synopsis lines of all available modules.  
eg:   
huangcdeMac-mini:~ captain$ python -m pydoc -k xml.sax
xml.sax - Simple API for XML (SAX) implementation for Python.
xml.sax._exceptions - Different kinds of SAX Exceptions
xml.sax.expatreader - SAX driver for the pyexpat C module.  This driver works with
xml.sax.handler - This module contains the core classes of version 2.0 of SAX for Python.
xml.sax.saxutils - A library of useful helper classes to the SAX classes, for the
xml.sax.xmlreader - An XML Reader is the SAX 2 name for an XML parser. XML Parsers


pydoc -p <port>  
    Start an HTTP server on the given port on the local machine.  
eg:
huangcdeMac-mini:~ captain$ python -m pydoc -p 1234
pydoc server ready at http://localhost:1234/
然后在浏览器中打开http://localhost:1234/就可以看到所有的帮助文档

pydoc -w <name> ...  
    Write out the HTML documentation for a module to a file in the current  
    directory.  If <name> contains a '/', it is treated as a filename; if  
    it names a directory, documentation is written for all the contents.  
eg:
D:\Learn\Python>python -m pydoc math -w math.html  # math是模块名，-w:写  在D:\Learn\Python目录下会生成math.html文件


glob 文件路径查找
原始地址：http://python.jobbole.com/81552/
glob模块是最简单的模块之一，内容非常少。用它可以查找符合特定规则的文件路径名。跟使用windows下的文件搜索差不多。
查找文件只用到三个匹配符：”*”, “?”, “[]”。”*”匹配0个或多个字符；”?”匹配单个字符；”[]”匹配指定范围内的字符，如：[0-9]匹配数字。
glob.glob
返回所有匹配的文件路径列表。它只有一个参数pathname，定义了文件路径匹配规则，这里可以是绝对路径，也可以是相对路径。下面是使用glob.glob的例子：
import glob
#获取指定目录下的所有图片（绝对路径）
print glob.glob(r"E:/Picture/*/*.jpg")
#获取上级目录的所有.py文件（相对路径）
print glob.glob(r'../*.py') #相对路径

glob.iglob
获取一个可编历对象，使用它可以逐个获取匹配的文件路径名。
与glob.glob()的区别是：glob.glob同时获取所有的匹配路径，而glob.iglob一次只获取一个匹配路径。这有点类似于.NET中操作数据库用到的DataSet与DataReader。下面是一个简单的例子：
import glob
#父目录中的.py文件
f = glob.iglob(r'../*.py')
print f #<generator object iglob at 0x00B9FF80>
for py in f:
    print py


httplib模块
import  httplib
def getBaidu():
    '''对百度发送一个GET请求'''
    http_client=httplib.HTTPConnection('www.baidu.com',80,timeout=20)
    http_client.request('GET','')
    r=http_client.getresponse()
'''
    print dir(r) #查看r的方法 
    ['begin', 'chunk_left', 'chunked', 'close', 'debuglevel', 'fileno', 'fp', 'getheader', 'getheaders', 'isclosed', 'length', 'msg', 'read', 'reason', 'status', 'strict', 'version', 'will_close']
    print r.status #查看返回的状态
    print r.read() #查看返回的内容
    print r.reason #请求是否ok
    print r.getheaders() #header是什么
    print r.msg #responese的消息结构
'''
getBaidu()

urllib模块
源地址：
http://www.cnblogs.com/sysu-blackbear/p/3629420.html
python爬虫库urllib：
http://cuiqingcai.com/947.html
1	import urllib2
2	 
3	response = urllib2.urlopen("http://www.baidu.com")
4	print response.read()

1.urllib.urlopen(url, data, timeout)
>>> import urllib
>>> f = urllib.urlopen('http://www.google.com.hk/')
>>> firstLine = f.readline()   #读取html页面的第一行
>>> firstLine
'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"><head><meta content="/images/google_favicon_128.png" itemprop="image"><title>Google</title><script>(function(){\n'
 urlopen返回对象提供方法：
# print help(f) 
# ['close', 'code', 'fileno', 'fp', 'getcode', 'geturl', 'headers', 'info', 'next', 'read', 'readline', 'readlines', 'url']
-         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
-         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
-         getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
-         geturl()：返回请求的url
 
2.urllib.urlretrieve(url[,filename[,reporthook[,data]]])
urlretrieve方法将url定位到的html文件下载到你本地的硬盘中。如果不指定filename，则会存为临时文件。
urlretrieve()返回一个二元组(filename,mine_hdrs)
临时存放：
>>> filename = urllib.urlretrieve('http://www.google.com.hk/')
>>> type(filename)
<type 'tuple'>
>>> filename[0]
'/tmp/tmp8eVLjq'
>>> filename[1]
<httplib.HTTPMessage instance at 0xb6a363ec>
存为本地文件:
>>> filename = urllib.urlretrieve('http://www.google.com.hk/',filename='/home/dzhwen/python文件/Homework/urllib/google.html')
>>> type(filename)
<type 'tuple'>
>>> filename[0]
'/home/dzhwen/python\xe6\x96\x87\xe4\xbb\xb6/Homework/urllib/google.html'
>>> filename[1]
 
>>> import urllib
>>> f=urllib.urlretrieve('http://www.baidu.com/',filename='/Users/captain/desktop/baidu.txt')#把爬下来的文件放在桌面的baidu.txt
3.urllib.urlcleanup()
清除由于urllib.urlretrieve()所产生的缓存
 
4.urllib.quote(url)和urllib.quote_plus(url)
将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受。
>>> urllib.quote('http://www.baidu.com')
'http%3A//www.baidu.com'
>>> urllib.quote_plus('http://www.baidu.com')
'http%3A%2F%2Fwww.baidu.com'
5.urllib.unquote(url)和urllib.unquote_plus(url)
与4的函数相反。
6.urllib.urlencode(query)
将URL中的键值对以连接符&划分
这里可以与urlopen结合以实现post方法和get方法：
GET方法：
>>> import urllib
>>> params=urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
>>> params
'eggs=2&bacon=0&spam=1'
>>> f=urllib.urlopen("http://python.org/query?%s" % params)
>>> print f.read()

POST方法：
>>> import urllib
>>> parmas = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
>>> f=urllib.urlopen("http://python.org/query",parmas)
>>> f.read()

#这里还可以把请求的地址单独拎出来写
#get
import urllib2
 
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl) #单独拎出来
response = urllib2.urlopen(request)
print response.read()
#post
import urllib
import urllib2
 
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)#单独拎出来
response = urllib2.urlopen(request)
print response.read()



time

import  time
print u'休眠二秒打印出hello world,开始倒计时...'
time.sleep(2)
print 'hello world'
#获取时间戳(1970年开始计时的)
print u'获取时间戳:',time.time()
print u'返回当前日期的字符串格式:\n',time.ctime()
print u'时间戳转为字符串:\n',time.ctime(time.time())
print u'时间戳转为struct_time格式:\n',time.gmtime(time.time())
time_gmtime=time.gmtime(time.time())
print u'查看struct_time格式的显示年月日时分秒结果:\n',str(time_gmtime.tm_year)+'-'+str(time_gmtime.tm_mon)+'-'+str(time_gmtime.tm_mday)+' '+str(time_gmtime.tm_hour)+':'+str(time_gmtime.tm_min)+':'+str(time_gmtime.tm_sec)
print u'时间戳转为struct_time,但是返回本地时间:\n',time.localtime(time.time())
print u'获取当前时间并且进行格式化:',time.strftime('%y-%m-%d %X',time.localtime())


sys

import  sys
print u'获取python解释程序的版本信息:',sys.version
print u'获取最大的int值:',sys.maxint
print u'获取操作系统平台名称:',sys.platform
print u'返回模块的搜索路径:\n'
for item in sys.path:
    print item  
print u'模拟进度条的实现:\n'
for i in range(15):
    sys.stdout.write('#')
    import  time
    time.sleep(0.03)  
print u'\n读取屏幕的输入:'
val=sys.stdin.readline()[:-1]
print u'屏幕输入的内容为:',val

datetime

import  datetime
import  time
print u'当前时间:\n',datetime.datetime.today()
print u'时间戳转成时间格式:\n',datetime.datetime.fromtimestamp(time.time())
print u'获取当前时间:\n',datetime.datetime.now()
print u'当前时间指定的值被替换:'
current_time=datetime.datetime.now()
print current_time.replace(2000,01,01)
print u'返回struct_time时间格式:',datetime.datetime.now().timetuple()
print u'字符串转换为时间格式:',datetime.datetime.strptime('21/11/06 22:11','%d/%m/%y %H:%M')
print u'当前时间加上10天的时间为:\n',datetime.datetime.now()+datetime.timedelta(days=10)


序列化模块：
'''Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。用的时候，先尝试导入cPickle，如果失败，再导入pickle：'''
try:
    import cPickle as pickle
except ImportError:
    import pickle
序列化后的类型都为str类型
模块名称	描述	提供的api
json	用于实现Python数据类型与通用（json）字符串之间的转换	dumps()、dump()、loads()、load()
pickle	用于实现Python数据类型与Python特定二进制格式之间的转换	dumps()、dump()、loads()、load()
shelve	专门用于将Python数据类型的数据持久化到磁盘，shelve是一个类似dict的对象，操作十分便捷	open()

shelve用法：
http://www.cnblogs.com/yyds/p/6563608.html

json

import  json
list1=[1,2,3,4,5]
tuple=('wuya','age','address')
dict={'name':'wuya','age':20,'address':'xian'}
print u'对列表进行序列化:',json.dumps(list1)
print u'序列化后的类型:',type(json.dumps(list1))
print u'对list序列化后的内容进行反序列化:',json.loads(json.dumps(list1))
print u'类型:',type(json.loads(json.dumps(list1)))
print u'对元组进行序列化:',json.dumps(tuple)
print u'序列化后的类型:',type(json.dumps(tuple))
print u'对tuple序列化后的内容进行反序列化:',json.loads(json.dumps(tuple))
print u'类型:',type(json.loads(json.dumps(tuple)))
print u'对字典进行序列化:',json.dumps(dict)
print u'序列化后的类型:',type(json.dumps(dict))
print u'对dict序列化后的内容进行反序列化:',json.loads(json.dumps(dict))
说明：
• Python dict中的非字符串key被转换成JSON字符串时都会被转换为小写字符串；
• Python中的tuple，在序列化时会被转换为array，但是反序列化时，array会被转化为list；
• 由以上两点可知，当Python对象中包含tuple数据或者包含dict，且dict中存在非字符串的key时，反序列化后得到的结果与原来的Python对象是不一致的；
• 对于Python内置的数据类型（如：str, unicode, int, float, bool, None, list, tuple, dict）json模块可以直接进行序列化/反序列化处理；对于自定义类的对象进行序列化和反序列化时，需要我们自己定义一个方法来完成定义object和dict之间进行转化。


pickle
把内存中的文件存储，或者把文件放在内存中的过程
# 常用的方法就四个，具体为：dumps(),dump(),loads(),load()

'''
dumps()和loads()方法见示例：
使用dump()方法对文件直接写进去;
with open('pickle.md','wb') as f:
    pickle.dump(account_dic,f)
    print u'数据类型为:',type(pickle.dump(account_dic,f))
load()方法不需要read()方法，直接读取文件就可以了
with open('pickle.md','rb') as f:
    account_dict1=pickle.load(f)
    print u'文件的内容为:\n',account_dict1
'''

import pickle
accounts={
    10:
        {
            'name':'wuya',
            'mail':'wuyaf@outlook.com',
            'password':'password',
            'balance':1500,
            'phone':'134XXXXXXXX'
        }
}
#序列化
account_dumps=pickle.dumps(accounts, True)
print u'查看序列化后的内容:\n',account_dumps,u'查看序列化后的数据类型:\n',type(account_dumps)
#进行反序列化
account_loads=pickle.loads(account_dumps)
print u'反序列化后的内容：{0}'.format(account_loads),u'数据类型为:{0}'.format(type(account_loads))


#序列化和反序列化在文件读写中的运用：
import pickle
accounts={
    10:
        {
            'name':'wuya',
            'mail':'wuyaf@outlook.com',
            'password':'password',
            'balance':1500,
            'phone':'13484545195'
        }
}
#把accounts内容写到文件中
accounts_dump=pickle.dumps(accounts, True)
with open('pickle.md','wb') as f:
    f.write(accounts_dump)
#对文件的内容进行反序列化
accounts_file=open('pickle.md','rb')
account_dict=accounts_file.read()
fileContent=pickle.loads(account_dict)
print u'读取文件的内容:\n',fileContent
#对文件的内容进行修改
fileContent[10]['balance']=-500
#把修改后的文件内容写入到文件中
with open('pickle.md','wb') as f:
    f.write(pickle.dumps(fileContent))
#对修改后的文件进行反序列化
with open('pickle.md','rb') as f:
    f2=f.read()
print u'修改后的文件进行序列化后的内容为:\n',pickle.loads(f2)





Python单元测试：unittest
参考：
http://www.cnblogs.com/weke/articles/6271206.html
'''
测试：二个数相除的函数
1.先写函数
2.引入unittest,对结果进行判定
'''
def div(a,b):
    return a/b
import  unittest
class TestDiv(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_001(self):
        self.assertEqual(div(1,1),1)
    def test_002(self):
        self.assertRaises(ZeroDivisionError,div,1,0) #不理解这儿内部的参数？
if __name__=='__main__':
    unittest.main(verbosity=2)
'''
test_001 (__main__.TestDiv) ... ok
test_002 (__main__.TestDiv) ... ok
----------------------------------------------------------------------
Ran 2 tests in 0.004s
OK
'''


import unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):# 抛出异常
            s.split(2)
if __name__ == '__main__':
    unittest.main(verbosity=2) # 这儿verbosity=2表示查看详细日志
'''
也可用下面的两行代替上面的最后的两行:
suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
'''
'''
>>>
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.005s
OK
'''

selinum结合unittest来写：
# unittest结合selenium来进行测试，可以看到浏览器打开关闭了两次，即：执行一次用例关闭一次，可否再优化？
def div(a,b):
    return a/b
import unittest
from selenium import webdriver
class TestDiv(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()# 用Chrome的话，这儿用Chrome()
        self.driver.get('http://www.baidu.com')
    def tearDown(self):
        self.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
if __name__=='__main__':
    unittest.main(verbosity=2)


#优化浏览器只打开一次，然后执行两个用例：（这里使用的是钩子方法）
import unittest
from selenium import webdriver
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
if __name__=='__main__':
    unittest.main(verbosity=2)

#测试用例想要顺序执行的：用addTest()
import unittest
from selenium import webdriver
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestDiv('test_001')) #这儿只执行了test_001
    unittest.TextTestRunner(verbosity=2).run(suite)


# 或者重构为：,建议用这种方法：
import unittest
from selenium import webdriver
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
    @staticmethod
    def suites():
        tests=['test_001','test_002']
        return unittest.TestSuite(map(TestDiv,tests))
if __name__=='__main__':
    unittest.TextTestRunner(verbosity=2).run(TestDiv.suites())


# 某些用例不执行的可以忽略，使用的方法是makeSuite(）
import  unittest
from selenium import  webdriver
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')
    @unittest.skip(u'忽略该测试用例,谢谢!')
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
if __name__=='__main__':
    suite=unittest.TestSuite(unittest.makeSuite(TestDiv))
    unittest.TextTestRunner(verbosity=2).run(suite)
# 除了用TestSuite()方法外，也可以用TestLoader()加载测试用例
import unittest
from selenium import webdriver
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title,u'百度一下，你就知道')
    def test_002(self):
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
if __name__=='__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(TestDiv)
    unittest.TextTestRunner(verbosity=2).run(suite)
#assert断言,这个是python自带的断言；
import unittest
from selenium import webdriver
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        assert self.driver.title in u'百度一下，你就知道'
    def test_002(self):
        assert self.driver.current_url in 'https://www.baidu.com/'
if __name__=='__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(TestDiv)
    unittest.TextTestRunner(verbosity=2).run(suite)

#除上面自带的断言之外，unnitest还有很多断言

Method	Checks that	New in
assertEqual(a, b)	a == b	 
assertNotEqual(a, b)	a != b	 
assertTrue(x)	bool(x) is True	 
assertFalse(x)	bool(x) is False	 
assertIs(a, b)	a is b	3.1
assertIsNot(a, b)	a is not b	3.1
assertIsNone(x)	x is None	3.1
assertIsNotNone(x)	x is not None	3.1
assertIn(a, b)	a in b	3.1
assertNotIn(a, b)	a not in b	3.1
assertIsInstance(a, b)	isinstance(a, b)	3.2
assertNotIsInstance(a, b)	not isinstance(a, b)	3.2

# 用HTMLTestRunner.py来生成测试报告,这个需要下载之后https://pypi.python.org/pypi/HTMLTestRunner放在python/lib目录下
import unittest
from selenium import webdriver
import HTMLTestRunner
class TestDiv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_001(self):
        self.assertEqual(self.driver.title, u'百度一下，你就知道')
    def test_002(self):
        self.assertTrue(self.driver.find_element_by_id('kw').is_enabled())
    def test_003(self):
        self.assertIsNot(self.driver.current_url,'www.baidu.com')
if __name__=='__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(TestDiv)
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=file('/Users/captain/desktop/testReport.html','wb'),
        title=u'TestReport',
        description=u'测试报告详细信息'
    )
    runner.run(suite)



requests
url: http://www.cnblogs.com/weke/articles/6309044.html
安装：pip install requests
['adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'pyopenssl', 'request', 'session', 'sessions', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']

类似的库有：urllib, urllib2, httplib
# 示范
import requests
requests.get('https://github.com/timeline.json') 
requests.put('http://httpbin.org/put')
requests.post('http://httpbin.org/post')
requests.delete('http://httpbin/ddelete')
# get #get(url,params=None,**kwargs)
r=requests.get(
    url='http://yuedu.baidu.com/ebook/3c0077aaa32d7375a41780bb',
    params={'_searchquery':'selenium-python%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4'})
print r.url
# post #post(url,data=None,json=None,**kwargs)
r=requests.post(
    url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
    data={'cityId':438}) # post后面的参数是一个字典
print r.json() # 在requests库中有一个内置的JSON解码器，来帮助我们处理JSON数据，可以精简反序列化的过程


# 使用requests发送一个请求，我们可以获取这个请求的响应内容，HTTP的状态码，以及URL
import requests
r=requests.get('http://www.bing.com')
print u'HTTP状态码:',r.status_code
print u'请求的URL:',r.url
print u'获取Headers:',r.headers
print u'响应内容:',r.text




moco server:

moca server是模拟一个服务器
使用介绍 :
http://www.cnblogs.com/weke/articles/6859021.html
http://blog.csdn.net/crisschan/article/details/53335234
github: https://github.com/dreamhead/moco

1.下载moco-runner-0.11.1-standalone.jar放在moco-master文件夹
2.编写foo.json文件，可以编写reqeust和response，然后放在moco-master文件夹
json文件内容如下：

[
  {
    "request":
    {
      "method":"post",
      "uri":"/login",
      "json":
      {
        "username":"admin",
        "password":"admin",
        "roleID":22
      }
    },
    "response":
    {
      "json":
      {
        "username":"wanghaitao",
        "userID":27,
        "year":1989,
        "token":"asdgfhh32456asfgrsfss"
      }
    }
  }
]
'''
#对json文件可以对response进行文件封装：
[
  {
    "request":
    {
      "method":"post",
      "uri":"/login",
      "json":
      {
        "username":"admin",
        "password":"admin",
        "roleID":22
      }
    },
    "response":
    {
      "file":"response.json"
    }
  }
]
下面为response.json文件内容，最好将文件放在同一个文件夹下：
{
        "username":"wanghaitao",
        "userID":22,
        "token":"asdgfhh32456asfgrsfss"
}
'''
3.在moco-master文件夹中,执行java -jar moco-runner-0.11.1-standalone.jar http -p 12306 -c foo.json,启动server
4.在浏览器中打开http://localhost:12306/就可以看到返回值了，也可以在postman中验证返回值


#然后编写接口测试内容：
import  unittest
import  requests
class MockLoginTest(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:12306'
    def tearDown(self):
        pass
    def getUrl(self,path):
        return self.url+path
    def getToken(self):
        '''获取token'''
        data={
            "username":"admin",
            "password":"admin",
            "roleID":22
        }
        r=requests.post(self.getUrl('/login'),json=data)
        return r.json()['token']
    def test_login(self):
        '''验证moco登录的接口'''
        data={
            "username":"admin",
            "password":"admin",
            "roleID":22
        }
        r=requests.post(self.getUrl('/login'),json=data)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['username'],'wanghaitao')
if __name__=='__main__':
    unittest.main(verbosity=2)
    
---------------------------------------
# 对于上面增加一种业务：
# 增加对停车时间的查询，需要带着服务端返回的token字段去请求：

# 先来看json字段的内容：
[
  {
    "request":
    {
      "method":"post",
      "uri":"/login",
      "json":
      {
        "username":"admin",
        "password":"admin",
        "roleID":22
      }
    },
    "response":
    {
      "file":"login_response.json"
    }
  },

  {
    "request":
    {
      "method":"post",
      "uri":"/parkinside",
      "json":
      {
        "token":"asdgfhh32456asfgrsfss",
        "vpl":"AJ3585"
      }
    },
    "response":
    {
      "file":"parkinside.json"
    }
  }
]
# login_response.json的内容：
{
        "username":"wanghaitao",
        "userID":22,
        "token":"asdgfhh32456asfgrsfss"
}
# parkinside.json的内容：
{
  "vplInfo":
  {
    "userID":22,
    "username":"wanghaitao",
    "vpl":"京AJ3585"
  },
  "Parking time long":"20小时18分钟",
  "Parking fee":"20$"
}

主程序业务的内容编写：
import  unittest
import  requests
class MockTest(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:12306'     
    def tearDown(self):
        pass    
    def test_login(self,url='/login'):
        '''验证登录的接口'''
        data={
            "username":"admin",
            "password":"admin",
            "roleID":22
        }
        r=requests.post(self.url+url,json=data)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['username'],'wanghaitao')  
    def getToken(self,url='/login'):
        '''登录moco成功后获取token'''
        data={
            "username":"admin",
            "password":"admin",
            "roleID":22
        }
        r=requests.post(self.url+url,json=data)
        return r.json()['token']    
    def test_parkingside(self,url='/parkinside'):
        '''验证查询停车时长接口'''
        data={
            "token":self.getToken(),#这个调取了服务端返回的token
            "vpl":"AJ3585"
        }
        r=requests.post(self.url+url,json=data)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['Parking time long'],u'20小时18分钟')
        self.assertEqual(r.json()['Parking fee'], u'20$')
        
if __name__=='__main__':
    unittest.main(verbosity=2)







#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
pip install pycurl
关于python网络编程，使用urllib与服务器通信时，客户端的数据是添加到Head里面通过URL，发送到服务器端，urllib包实现客户端上传文件时，会出现死掉的状态（实际上是超时设置问题）。
Pycurl包是一个libcurl的Python接口，它是由C语言编写的。与urllib相比，pycurl的速度要快很多。
Libcurl 是一个支持FTP，FTPS，HTTP，HTTPS，GOPHER，TELNET，DICT，FILE 和 LDAP的客户端URL传输库。libcurl也支持HTTPS认证，HTTP、POST、HTTP PUT、FTP上传，代理，Cookies，基本身份验证，FTP文件断点继传，HTTP代理通道等等。
'''
c = pycurl.Curl()    #创建一个curl对象 
c.setopt(pycurl.CONNECTTIMEOUT, 5)    #连接的等待时间，设置为0则不等待  
c.setopt(pycurl.TIMEOUT, 5)           #请求超时时间  
c.setopt(pycurl.NOPROGRESS, 0)        #是否屏蔽下载进度条，非0则屏蔽  
c.setopt(pycurl.MAXREDIRS, 5)         #指定HTTP重定向的最大数  
c.setopt(pycurl.FORBID_REUSE, 1)      #完成交互后强制断开连接，不重用  
c.setopt(pycurl.FRESH_CONNECT,1)      #强制获取新的连接，即替代缓存中的连接  
c.setopt(pycurl.DNS_CACHE_TIMEOUT,60) #设置保存DNS信息的时间，默认为120秒  
c.setopt(pycurl.URL,"http://www.baidu.com")      #指定请求的URL  
c.setopt(pycurl.USERAGENT,"Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)")    #配置请求HTTP头的User-Agent
c.setopt(pycurl.HEADERFUNCTION, getheader)   #将返回的HTTP HEADER定向到回调函数getheader
c.setopt(pycurl.WRITEFUNCTION, getbody)      #将返回的内容定向到回调函数getbody
c.setopt(pycurl.WRITEHEADER, fileobj)        #将返回的HTTP HEADER定向到fileobj文件对象
c.setopt(pycurl.WRITEDATA, fileobj)          #将返回的HTML内容定向到fileobj文件对象
c.getinfo(pycurl.HTTP_CODE)         #返回的HTTP状态码
c.getinfo(pycurl.TOTAL_TIME)        #传输结束所消耗的总时间
c.getinfo(pycurl.NAMELOOKUP_TIME)   #DNS解析所消耗的时间
c.getinfo(pycurl.CONNECT_TIME)      #建立连接所消耗的时间
c.getinfo(pycurl.PRETRANSFER_TIME)  #从建立连接到准备传输所消耗的时间
c.getinfo(pycurl.STARTTRANSFER_TIME)    #从建立连接到传输开始消耗的时间
c.getinfo(pycurl.REDIRECT_TIME)     #重定向所消耗的时间
c.getinfo(pycurl.SIZE_UPLOAD)       #上传数据包大小
c.getinfo(pycurl.SIZE_DOWNLOAD)     #下载数据包大小 
c.getinfo(pycurl.SPEED_DOWNLOAD)    #平均下载速度
c.getinfo(pycurl.SPEED_UPLOAD)      #平均上传速度
c.getinfo(pycurl.HEADER_SIZE)       #HTTP头部大小 
