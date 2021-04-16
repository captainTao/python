#!/usr/bin/env python3.x
# -*- coding: utf-8 -*-
# -*-  -*-

# 修复文件的编码错误：
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 执行python文件的时候，找不到对应的模块，需要在文件开头添加：
# sys.path.append(os.path.dirname(sys.path[0]))


'''
问题：
1.直接print(Logger)会报错，如何查看实例化的对象是单例？

'''

'''
re:
__________
https://blog.csdn.net/Winterto1990/article/details/47361955
https://so.csdn.net/so/search/s.do?q=python%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%20re&t=blog&u=Winterto1990
https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

>>> import re
>>> dir(re)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
'''

re.match(pattern, string, flags)  #返回值: 为真或者假。
re.search(pattern, string, flags)  #返回值：如果查找到则返回查找到的值，否则返回为None



# -*- re.compile -*-
# ------------------
import re
content='Where are you from? You look so hansome.'
regex=re.compile(r'\w*som\w*')
m=regex.search(content)
if m:
    print (m.group(0))  #中间的0的意义没懂？ https://blog.csdn.net/Winterto1990/article/details/47361955
else:
    print ("Not found")

'''
MatchObject 实例有几个方法和属性；
重要的如下：
group() 返回被 RE 匹配的字符串
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置

'''



# -*- requests -*-
# ------------------
# https://blog.csdn.net/pittpakk/article/details/81218566
response = requests.post(CMS_URL+SUBMIT_URL, data=pay_load, cookies=CMS_COOKIES)
response.raise_for_status()  #re的状态，正常的话返回none，否则抛异常
print (response.text)
re_json = response.json()

'''
response.json()返回的类型为dict
response.text 返回的类型为string

7个主要方法：
requests.request()  构造一个请求，支持以下各种方法
requests.get()  获取html的主要方法
requests.head() 获取html头部信息的主要方法
requests.post() 向html网页提交post请求的方法
requests.put()  向html网页提交put请求的方法
requests.patch()    向html提交局部修改的请求
requests.delete()   向html提交删除请求


response对象有以下属性：
r.status_code   http请求的返回状态，若为200则表示请求成功。
r.text  http响应内容的字符串形式，即返回的页面内容
r.encoding  从http header 中猜测的相应内容编码方式, 'ISO-8859-1'
r.apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式）,'utf-8'
r.content   http响应内容的二进制形式
r.raise_for_status()捕获异常，正常会返回None

try:
    r=requests.get(url,timeout=30)#请求超时时间为30秒
    r.raise_for_status()#如果状态不是200，则引发异常
    r.encoding=r.apparent_encoding #配置编码
    return r.text
except:
    return "产生异常" 


method: “GET”、”HEAD”、”POST”、”PUT”、”PATCH”等等
url: 请求的网址
**kwargs: 控制访问的参数


Form Data 和 Request Payload 区别:
---------------------------------
https://juejin.im/post/5bf60a3fe51d4548c6648622
https://blog.csdn.net/zwq912318834/article/details/79930423  #scrapy

如果请求头里设置Content-Type: application/x-www-form-urlencoded，
那么这个请求被认为是表单请求，参数出现在Form Data里，格式为key=value&key=value&key=value...
在servlet中，后端可以通过request.getParameter(name)的形式来获取表单参数

原生的AJAX请求头里设置Content-Type:application/json，
或者使用默认的请求头Content-Type:text/plain;参数会显示在Request payload块里提交。
后端可以使用getRequestPayload方法来获取。


1. requests.get()
r=requests.get(url,params,**kwargs)
url: 需要爬取的网站地址。
params: 翻译过来就是参数， url中的额外参数，字典或者字节流格式，可选。
**kwargs : 12个控制访问的参数

我们先来讲讲**kwargs:
**kwargs有以下的参数，对于requests.get,其第一个参数被提出来了。

1. params：字典或字节序列， 作为参数增加到url中,使用这个参数可以把一些键值对以?key1=value1&key2=value2的模式增加到url中
 

例如：kv = {'key1':' values', 'key2': 'values'} 
r = requests.get('http:www.python123.io/ws', params=kw)

2. data：字典，字节序或文件对象，重点作为向服务器提供或提交资源是提交，，作为request的内容，与params不同的是，data提交的数据并不放在url链接里， 而是放在url链接对应位置的地方作为数据来存储。，它也可以接受一个字符串对象。

3. json：json格式的数据， json合适在相关的html，http相关的web开发中非常常见， 也是http最经常使用的数据格式， 他是作为内容部分可以向服务器提交。
 

例如：kv = {'key1': 'value1'} 
r = requests.post('http://python123.io/ws', json=kv)

4. headers：字典是http的相关语，对应了向某个url访问时所发起的http的头i字段， 可以用这个字段来定义http的访问的http头，可以用来模拟任何我们想模拟的浏览器来对url发起访问。
 

例子： hd = {'user-agent': 'Chrome/10'} 
r = requests.post('http://python123.io/ws', headers=hd)

5. cookies：字典或CookieJar，指的是从http中解析cookie
6. auth：元组，用来支持http认证功能
7. files：字典， 是用来向服务器传输文件时使用的字段。
 

例子：fs = {'files': open('data.txt', 'rb')} 
r = requests.post('http://python123.io/ws', files=fs)

8. timeout: 用于设定超时时间， 单位为秒，当发起一个get请求时可以设置一个timeout时间， 如果在timeout时间内请求内容没有返回， 将产生一个timeout的异常。
9. proxies：字典， 用来设置访问代理服务器。
10. allow_redirects: 开关， 表示是否允许对url进行重定向， 默认为True。
11. stream: 开关， 指是否对获取内容进行立即下载， 默认为True。
12. verify：开关， 用于认证SSL证书， 默认为True。
13. cert： 用于设置保存本地SSL证书路径


2. requests.head()
>>> import requests
>>> res = requests.head('http://www.baidu.com')
>>> res.headers
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Tue, 05 Nov 2019 06:58:55 GMT', 'Last-Modified': 'Mon, 13 Jun 2016 02:50:21 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18'}
>>> res = requests.head('https://comfort-qa.camera360.com/')


3. requests.post()
a. 向url post一个字典
>>> payload={"key1":"value1","key2":"value2"}
>>> r=requests.post("http://httpbin.org/post",data=payload)
>>> print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/post"
}

b. 向url post 一个字符串，自动编码为data
>>>r=requests.post("http://httpbin.org/post",data='helloworld')
>>>print(r.text)
{
  "args": {}, 
  "data": "helloworld", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "10", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/post"
}

c. 向url post一个文件
>>> import requests
>>> files = {'files':open('F:\\python\\test\\test_case\\files.txt','rb')}
>>> r = requests.post('https://httpbin.org/post',files=files)
>>> print(r.text)
{
    "args":{
 
    },
    "data":"",
    "files":{
        "files":"hello worle!"
    },
    "form":{
 
    },
    "headers":{
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"close",
        "Content-Length":"158",
        "Content-Type":"multipart/form-data; boundary=d2fb307f28aeb57b932d867f80f2f600",
        "Host":"httpbin.org",
        "User-Agent":"python-requests/2.19.1"
    },
    "json":null,
    "origin":"113.65.2.187",
    "url":"https://httpbin.org/post"
}


4. requests.put()
>>> payload={"key1":"value1","key2":"value2"}
>>> r=requests.put("http://httpbin.org/put",data=payload)
>>> print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/put"


5. requests.patch()

requests.patch和request.put类似。 
两者不同的是： 
当我们用patch时仅需要提交需要修改的字段。 
而用put时，必须将20个字段一起提交到url，未提交字段将会被删除。 
patch的好处是：节省网络带宽。

6. requests.request()

requests.request(）支持其他所有的方法。 
requests.request(method，url,**kwargs)

'''


'''
# -*- 字符拼接的方法 -*-
# ------------------
# https://www.cnblogs.com/blogsxyz/p/9019836.html

1. str1+str2
2. ''.join(Array)
>>> b = ['1','2','3']
>>> ''.join(b)
'123'

3. ,拼接
4. format拼接
'''



# -*- 返回多个值 -*-
# -----------------
# 实质是返回一个tuple
# https://www.cnblogs.com/wllhq/p/8119347.html




'''
定时器：
___________
https://www.jianshu.com/p/403bcb57e5c2
https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/
'''

# -*- 阻塞函数sleep -*-:
# --------------------
from datetime import datetime
import time
# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        time.sleep(n)

timer(5)


# -*- 阻塞函数sched -*-:
# --------------------
'''
import sched
import time
schedule = sched.scheduler(time.time, time.sleep)
schedule.enter(3, 0, sticker_publish, (platform, pid, name,))
schedule.run()
'''
import sched
import time
from datetime import datetime
# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二参数可以在定时未到达之前阻塞
schdule = sched.scheduler(time.time, time.sleep)
# 被周期性调度触发函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,)) # 方法有enter,enterabs,参数为tuple
# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件,优先级（用于同时到达两个事件同时执行的顺序），被调度触发的函数
    # 给该触发器函数的参数（tuple形式）
    schedule.enter(0, 0, pirntTime, (inc,))
    schedule.run() #不是循环的，一次调度就over
# 5秒输出一次
main(5)



# -*- schedule -*-
# ----------------
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)



# -*- APScheduler定时框架 -*-
# --------------------------
'''
pip install apscheduler
APScheduler 四个组件分别为：触发器(trigger)，作业存储(job store)，执行器(executor)，调度器(scheduler)。
可以持久化任务，并以daemon方式运行应用。

APScheduler 有三种内建的 trigger:
date: 特定的时间点触发
interval: 固定时间间隔触发
cron: 在特定时间周期性地触发

job store：
APScheduler 默认使用 MemoryJobStore，可以修改使用 db 存储方案

executor 有两种：
ProcessPoolExecutor
ThreadPoolExecutor(默认，线程池最大线程数为10)

scheduler：
配置作业存储和执行器可以在调度器中完成，例如添加、修改和移除作业。
BackgroundScheduler,调度器在后台执行

1. BlockingScheduler: use when the scheduler is the only thing running in your process
2. BackgroundScheduler: use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
3. AsyncIOScheduler: use if your application uses the asyncio module
4. GeventScheduler: use if your application uses gevent
5. TornadoScheduler: use if you’re building a Tornado application
6. TwistedScheduler: use if you’re building a Twisted application
7. QtScheduler: use if you’re building a Qt application
'''

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
# 输出时间
def job():
    print(datetime.now().strtime("%Y-%m-%d %H:%M:%S"))
def my_job(text):
    print(text)
# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=5)
# sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')
# scheduler.add_job(job, "cron"， day_of_week="1-5", hour=6, minute=30)
# sched.add_job(my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
sched.start()


'''
# 显式设置 job store(使用mongo存储)和 executor 可以这样写：
from datetime import datetime
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
# MongoDB 参数
host = '127.0.0.1'
port = 27017
client = MongoClient(host, port)
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 存储方式
jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': MemoryJobStore()
}
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
scheduler.add_job(job, 'interval', seconds=5, jobstore='mongo')
scheduler.start()
'''


# -*- Sqlalchemy -*-
# ------------------



# -*- 非阻塞函数Timer -*-
# ---------------------
from datetime import datetime
from threading import Timer
# 打印时间函数
def prinTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime,(inc,))
    t.start()

printTime(2)

# 停掉计时器用cancel()
t.cancel()


#10s后执行
from datetime import datetime
from threading import Timer
def hello():
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

t = Timer(10.0, hello)
t.start()


# 每次都会创建一个新的子线程，但活跃的线程只有一个
# 始终只有一个线程且重复调用函数方法
# https://www.cnblogs.com/tig666666/p/9300973.html
# https://juejin.im/post/5c8918f5f265da2dd6393633
import time
from threading import Timer
import threading
def print_name(inc,str):
    print ("i'm %s"%str)
    Timer(inc,print_name,(inc,str,)).start()
    # print(threading.currentThread())
    # print(threading.enumerate())
    print("threading active = {} \n   \n".format(threading.enumerate()))
print ("start")
Timer(3,print_name,(3,"superman",)).start()
Timer(5,print_name,(5,"spiderman",)).start()
print ("end")




# -*- 异步IO, 非阻塞asyncio -*-
# ----------------------------
import asyncio
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()

#异步方法：
async def async_double(x):
    return 2 * x
#异步调用：
# 要调用异步函数，必须使用await关键字
async def print_double(x):
    print(await async_double(x))  
'''
https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640#0
https://blog.csdn.net/SL_World/article/details/86597738
https://blog.csdn.net/SL_World/article/details/86691747
https://blog.csdn.net/weixin_45139605/article/details/90798253

1. 同步编程的并发性不高
2. 多进程编程效率受CPU核数限制，当任务数量远大于CPU核数时，执行效率会降低。
3. 多线程编程需要线程之间的通信，而且需要锁机制来防止共享变量被不同线程乱改，而且由于Python中的GIL(全局解释器锁)，所以实际上也无法做到真正的并行。
4. 多进程和多线程是内核级别的程序，而协程是函数级别的程序
5. asyncio是单线程就能做到不同任务之间的切换，没有了线程切换的时间消耗，也不用使用锁机制来削弱多任务并发效率。

三元素:子生成器,子生成器,调用方

# 使用同步方式编写异步功能
import time
import asyncio
@asyncio.coroutine # 标志协程的装饰器
def taskIO_1():
    print('开始运行IO任务1...')
    yield from asyncio.sleep(2)  # 假设该任务耗时2s
    print('IO任务1已完成，耗时2s')
    return taskIO_1.__name__
@asyncio.coroutine # 标志协程的装饰器
def taskIO_2():
    print('开始运行IO任务2...')
    yield from asyncio.sleep(3)  # 假设该任务耗时3s
    print('IO任务2已完成，耗时3s')
    return taskIO_2.__name__
@asyncio.coroutine # 标志协程的装饰器
def main(): # 调用方
    tasks = [taskIO_1(), taskIO_2()]  # 把所有任务添加到task中
    done,pending = yield from asyncio.wait(tasks) # 子生成器
    for r in done: # done和pending都是一个任务，所以返回结果需要逐个调用result()
        print('协程无序返回值：'+r.result())

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop() # 创建一个事件循环对象loop
    try:
        loop.run_until_complete(main()) # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close() # 结束事件循环
    print('所有IO任务总耗时%.5f秒' % float(time.time()-start))
'''

'''
python v3.5 开始引入了新的语法async和await
新语法：
把@asyncio.coroutine替换为async；
把yield from替换为await
'''

import time
import asyncio
async def taskIO_1():
    print('开始运行IO任务1...')
    await asyncio.sleep(2)  # 假设该任务耗时2s
    print('IO任务1已完成，耗时2s')
    return taskIO_1.__name__
async def taskIO_2():
    print('开始运行IO任务2...')
    await asyncio.sleep(3)  # 假设该任务耗时3s
    print('IO任务2已完成，耗时3s')
    return taskIO_2.__name__
async def main(): # 调用方
    tasks = [taskIO_1(), taskIO_2()]  # 把所有任务添加到task中
    done,pending = await asyncio.wait(tasks) # 子生成器
    for r in done: # done和pending都是一个任务，所以返回结果需要逐个调用result()
        print('协程无序返回值：'+r.result())
    '''
    resualts = await asyncio.gather(taskIO_1(), taskIO_2()) # 子生成器
    print(resualts)
    '''
    '''
    for completed_task in asyncio.as_completed(tasks):
        resualt = await completed_task # 子生成器
        print('协程无序返回值：'+resualt)
    '''
if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop() # 创建一个事件循环对象loop
    try:
        loop.run_until_complete(main()) # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close() # 结束事件循环
    print('所有IO任务总耗时%.5f秒' % float(time.time()-start))

'''
asyncio.wait
①只有当给wait()传入timeout参数时才有可能产生pending列表。
②通过wait()返回的结果集是按照事件循环中的任务完成顺序排列的，所以其往往和原始任务顺序不同。
asyncio.gather
①这个结果集的结果顺序是传入任务的原始顺序
asyncio.as_completed
①这个结果输出是按照完成任务顺序排列，跟wait一样
②不同于wait:as_completed(tasks)可以实时返回当前完成的结果，而wait(tasks)需要等待所有协程结束后返回的done去获得结果。
'''


# 协程中调用协程，在主协程中还是顺序执行的；
import asyncio
import time 
 
async def main():
    print("主协程")
    print("等待result1协程运行")
    res1 = await result1()
    print("等待result2协程运行")
    res2 = await result2(res1)
    return (res1,res2)
 
async def result1():
    print("这是result1协程")
    await asyncio.sleep(4)
    return "result1"
  
async def result2(arg):
    print("这是result2协程")
    await asyncio.sleep(2)
    return f"result2接收了一个参数,{arg}"
 
if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(main())
        print(f"获取返回值:{result}")
    finally:
        print("关闭事件循环")
        loop.close()
    print('所有IO任务总耗时%.5f秒' % float(time.time()-start))



'''
-*- pillow: -*-
—————————————————
'''
from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB",(50,50),"white")
draw_table = ImageDraw.Draw(im=image)
draw_table.text(xy=(0, 0), text=u'仰', fill='#000000', font=ImageFont.truetype('./SimHei.ttf', 50))

image.show()  # 直接显示图片
image.save('满月.png', 'PNG')  # 保存在当前路径下，格式为PNG


'''
https://www.jianshu.com/p/8ba0c3e2381b
图片中文字居中：
固定背景，字体大小不确定，然后文字居中：
________________________________
def make_icon(path, name):
    # name去掉后缀  
    icon_name = re.split(r'-|_', name)[0]
    # 先假设取一个值，而得到比例
    font_size = 27
    font = ImageFont.truetype(FONT_TYPE, size=font_size)
    text_size_width = font.getsize(icon_name)[0]
    # 计算font_size:
    font_size_cal = math.floor(font_size * 190 / text_size_width)
    if font_size_cal > 50:
        font_size_cal = 50
    # font重新赋值
    font = ImageFont.truetype(FONT_TYPE, size=font_size_cal)
    text_size = font.getsize(icon_name)
    # 取画图的起始坐标点
    x = 100 - text_size[0] / 2
    y = 100 - text_size[-1] / 2
    # 画图
    img = Image.new("RGB", size=(200, 200), color=BG_COLOR)  # 创建图形
    draw = ImageDraw.Draw(img)
    draw.text((x, y), icon_name, font=font, fill='#191970')
    # 保存
    icon_path = os.path.join(path, name + '.png')
    img.save(icon_path)
    return icon_path

'''


'''
图片中文字居中：
_______________
'''
# 导入需要的包
from PIL import Image, ImageDraw, ImageFont
import string
import os

# 背景尺寸
bg_size = (750, 1334)
# 生成一张尺寸为 750x1334 背景色为黄色的图片
bg = Image.new('RGB', bg_size, color=(255,255,0))

# 字体大小
font_size = 36
# 文字内容
text = '1lin24 is me. 我是1lin24。'

# 字体文件路径
font_path = os.path.join('.', 'fonts', 'SourceHanSansCN-Medium.otf')
# 设置字体
font = ImageFont.truetype(font_path, font_size)
# 计算使用该字体占据的空间
# 返回一个 tuple (width, height)
# 分别代表这行字占据的宽和高
text_width = font.getsize(text)
draw = ImageDraw.Draw(bg)

# 计算字体位置
text_coordinate = int((bg_size[0]-text_width[0])/2), int((bg_size[1]-text_width[1])/2)
# 写字
draw.text(text_coordinate, text,(0,0,0), font=font)

# 要保存图片的路径
img_path = os.path.join('.', 'output', 'center_text.jpg')
# 保存图片
bg.save(img_path)
print('保存成功 at {}'.format(img_path))



'''
# 放一张透明png
__________________
'''
# 导入需要的包
from PIL import Image, ImageDraw
import os

# 背景尺寸
bg_size = (750, 1334)
# 生成一张尺寸为 750x1334 背景色为白色的图片
bg = Image.new('RGBA', bg_size, color=(255,255,0,255))

# 要粘贴的图片尺寸
fruit_size = (120, 100)
# 图片地址
fruit_path = os.path.join('.', 'imgs', 'fruits.png')
# 加载png图片，并手动转为 rgba 模式
fruit = Image.open(fruit_path).convert('RGBA')
# 计算图片位置
# fruit_box 为头像在 bg 中的位置
# fruit_box(x1, y1, x2, y2)
# x1,y1 为头像左上角的位置
# x2,y2 为头像右下角的位置
x, y = int((bg_size[0]-fruit_size[0])/2), int((bg_size[1]-fruit_size[1])/2)
fruit_box = (x, y, (x + fruit_size[0]), (y + fruit_size[1]))

# 将图片设置为我们需要的大小
fruit = fruit.resize(fruit_size)
# box 为头像在 bg 中的位置
# box(x1, y1, x2, y2)
# x1,y1 为头像左上角的位置
# x2,y2 为头像右下角的位置
bg.paste(fruit, fruit_box, fruit)

# 要保存图片的路径
img_path = os.path.join('.', 'output', 'png_paste.png')
# 保存图片
bg.save(img_path)
print('保存成功 at {}'.format(img_path))

# GUI环境可以使用下面方式直接预览
# bg.show()



'''
圆形头像放背景图中央：
__________________
'''
# 导入需要的包
from PIL import Image, ImageDraw
import os

# 背景尺寸
bg_size = (750, 1334)
# 生成一张尺寸为 750x1334 背景色为白色的图片
bg = Image.new('RGB', bg_size, color=(255,255,0))

# 头像尺寸
avatar_size = (200, 200)
# 头像路径
avatar_path = os.path.join('.', 'imgs', 'avatar.jpeg')
# 加载头像文件到 avatar
avatar = Image.open(avatar_path)
# 把头像的尺寸设置成我们需要的大小
avatar = avatar.resize(avatar_size)

# 新建一个蒙板图, 注意必须是 RGBA 模式
mask = Image.new('RGBA', avatar_size, color=(0,0,0,0))
# 画一个圆
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0,0, avatar_size[0], avatar_size[1]), fill=(0,0,0,255))

# 计算头像位置
x, y = int((bg_size[0]-avatar_size[0])/2), int((bg_size[1]-avatar_size[1])/2)
# box 为头像在 bg 中的位置
# box(x1, y1, x2, y2)
# x1,y1 为头像左上角的位置
# x2,y2 为头像右下角的位置
box = (x, y, (x + avatar_size[0]), (y + avatar_size[1]))
# 以下使用到paste(img, box=None, mask=None)方法
#   img 为要粘贴的图片对你
#   box 为图片 头像在 bg 中的位置
#   mask 为蒙板，原理同 ps， 只显示 mask 中 Alpha 通道值大于等于1的部分
bg.paste(avatar, box, mask)

# 要保存图片的路径
img_path = os.path.join('.', 'output', 'round_avatar.jpg')
# 保存图片
bg.save(img_path)
print('保存成功 at {}'.format(img_path))

# GUI环境可以使用下面方式直接预览
# bg.show()




'''
Paltform模块
——————————————
原文链接：https://blog.csdn.net/gatieme/article/details/45674367
platform.system() 获取操作系统类型，windows、linux等
platform.platform() 获取操作系统，Darwin-9.8.0-i386-32bit
platform.version() 获取系统版本信息 6.2.0
platform.mac_ver()
platform.win32_ver() (‘post2008Server’, ‘6.2.9200’, ”, u’Multiprocessor Free’)
'''
import platform

def TestPlatform( ):
    print ("----------Operation System--------")
    #  获取Python版本
    print platform.python_version()

    #   获取操作系统可执行程序的结构，，(’32bit’, ‘WindowsPE’)
    print platform.architecture()

    #   计算机的网络名称，’acer-PC’
    print platform.node()

    #获取操作系统名称及版本号，’Windows-7-6.1.7601-SP1′
    print platform.platform()

    #计算机处理器信息，’Intel64 Family 6 Model 42 Stepping 7, GenuineIntel’
    print platform.processor()

    # 获取操作系统中Python的构建日期
    print platform.python_build()

    #  获取系统中python解释器的信息
    print platform.python_compiler()

    if platform.python_branch()=="":
        print platform.python_implementation()
        print platform.python_revision()
    print platform.release()
    print platform.system()

    #print platform.system_alias()
    #  获取操作系统的版本
    print platform.version()

    #  包含上面所有的信息汇总
    print platform.uname()

def UsePlatform( ):
    sysstr = platform.system()
    if(sysstr =="Windows"):
        print ("Call Windows tasks")
    elif(sysstr == "Linux"):
        print ("Call Linux tasks")
    else:
        print ("Other System tasks")

if __name__ == "__main__" :
    TestPlatform( )
    UsePlatform( )




'''
os/os.path:
________________
https://blog.csdn.net/gatieme/article/details/45674367
https://juejin.im/post/5c57afb1f265da2dda6924a1

>>> import os
>>> dir(os.path)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']

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
Python的标准库中的os模块主要涉及普遍的操作系统功能。可以在Linux和Windows下运行，与平台无关。
os.sep 可以取代操作系统特定的路径分割符。
os.name字符串指示你正在使用的平台。比如对于Windows，它是’nt’，而对于Linux/Unix用户，它是’posix’。
os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
os.listdir()返回指定目录下的所有文件和目录名。
os.remove()函数用来删除一个文件。
os.system()函数用来运行shell命令。
os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’。
os.path.split()函数返回一个路径的目录名和文件名。
os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
os.path.exists()函数用来检验给出的路径是否真地存在


os.getcwd()：获得当前工作目录
os.curdir:返回但前目录（’.’)
os.chdir(dirname):改变工作目录到dirname
os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
os.path.exists(name):判断是否存在文件或目录name
os.path.getsize(name):获得文件大小，如果name是目录返回0L
os.path.abspath(name):获得绝对路径
os.path.normpath(path):规范path字符串形式
os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext():分离文件名与扩展名
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径

'''

# os和os.path模块
# os.listdir(dirname)：列出dirname下的目录和文件
# 在python3中可以使用os.scandir()返回的是一个迭代器
import os
with os.scandir('my_directory') as entries:
    for entry in entries:
        print(entry.name)
        info = entry.stat() #可以获取文件大小和修改时间等文件属性
        print(info.st_mtime)

# 获取目录的另外一个方法：pathlib.Path().iterdir()
from pathlib import Path
entries = Path('my_directory')
for entry in entries.iterdir():
    print(entry.name)
    print(entry.stat().st_time) #pathlib也有stat()方法，作用跟scandir一致,这个日期格式是时间戳
    print('{} 上次修改时间为 {}'.format(entry.name, timestamp2datetime(info.st_mtime))) # 这个格式输出

# from pathlib import Path
# basepath = Path('my_directory')
# files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
# for item in files_in_basepath:
#     print(item.name)

# 格式化字符输出：
b='4'
a='5'
print('a=%s,b=%s'%(a,b))
print('a={},b={}'.format(a,b))

os.mkdir()  #创建单个子目录
os.makedirs()   #创建多个目录，包括中间目录
Pathlib.Path.mkdir()    #创建单个或多个目录

# 如果目录已存在，则不会引起错误:
from pathlib import Path
p = Path('example_directory')
p.mkdir(exist_ok=True)

# 或者：
# from pathlib import Path
# p = Path('example_directory')
# try:
#     p.mkdir()
# except FileExistsError as e:
#     print(e)

#创建级联目录：
from pathlib import Path
p = Path('2018/10/05')
p.mkdir(parents=True, exist_ok=True)

import os
os.makedirs('2018/10/05', mode=0o770) #类似bash: mkdir -p



# 文件名匹配模式：
# _____________
endswith(), startswith() #字符串方法
fnmatch.fnmatch() #可以使用*，？通配符
glob.glob()
pathlib.Path.glob()


import os
import fnmatch
for f_name in os.listdir('some_directory'):
    # if fnmatch.fnmatch(f_name, '*.txt'):
    if fnmatch.fnmatch(f_name, 'data_*_backup.txt'):
        print(f_name)

# glob功能同fnmatch,不同的是：它将以 . 开头的文件视为特殊文件。
import glob
print(glob.glob('*.py'))# 以列表形式返回

import glob
for name in glob.glob('*[0-9]*.txt'): #所有包含数子，后缀为.txt的文件
    print(name)

# 递归搜索：
import glob
for name in glob.iglob('**/*.py', recursive=True): #iglob返回的是一个迭代器，glob是一个列表
    print(name)


from pathlib import Path
p = Path('.')
for name in p.glob('*.p*'):
    print(name)


# os.walk()
import os
for dirpath, dirname, files in os.walk('.'):
   print(f'Found directory: {dirpath}')
   for file_name in files:
       print(file_name)



'''
Sys模块
————————————
sys.argv: 实现从程序外部向程序传递参数。
sys.exit([arg]): 程序中间的退出，arg=0为正常退出。
sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。
sys.setdefaultencoding(): 设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）
sys.getfilesystemencoding(): 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'.
sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。
sys.platform: 获取当前系统平台。
sys.stdin,sys.stdout,sys.stderr stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
'''





# python执行系统之间的区别；
# ----------------------
'''
https://www.cnblogs.com/yunguoxiaoqiao/p/7588725.html
Python3默认编码是unicode；而Python2是ASCII码。Windows环境默认是gbk编码。
Py3 自动把文件编码转为unicode，Python2并不会自动的把文件编码转为unicode存在内存里。需要手动转码。

手动转码规则：

UTF-8 --> decode 解码 --> Unicode
Unicode --> encode 编码 --> GBK / UTF-8 等
使用type可以查看编码形式，unicode是'unicode',gbk和utf-8是'str或bytes'。
'''


# 中文字体直接len,为1，转成utf-8 len会变成3，转换为gbk，len会变成2；
# 而英文字体或者数字，不管怎么转换都是1
name = '耳朵'
print(len(name)) #2
print(len(name.encode('utf-8'))) #6,utf-8是3倍，gbk是2倍



# -*- tkinter -*-
# ------------------



# -*- time -*-
# ------------------
'''
>>> import time
>>> time.time()
1573091348.739672
>>> time.ctime(time.time())
'Thu Nov  7 09:49:25 2019'
>>> dir(time)
['CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'clock', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname', 'tzset']
'''



# 查看模块的官方文档地址
>>> import time
>>> help(time) 
# 查看py文件存放的本地位置
>>> import random
>>> print(random.__file__)



def __init__(self):
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    pass

# python上传https网站的时候，提示ssl失败：
# 方法一（不推荐）：
# requests中加verify=False
# response = requests.post(url=URL, data=data, files=files, cookies = Cookie, headers={'Content-Type':'binary'}, verify=False)
# 方法二（推荐）：
# (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')])")))
# 找证书位置：
# import certifi
# print(certifi.where())



# Python-文件和文件夹的移动、复制、删除、重命名
# 转自：http://blog.csdn.net/woshisangsang/article/details/74360612
# ---------------------------------
#文件、文件夹的移动、复制、删除、重命名 shutil

#导入shutil模块和os模块
import shutil,os

#复制单个文件,目标文件夹需要存在
shutil.copy("src","des")
#复制并重命名新文件
shutil.copy("C:\\a\\2.txt","C:\\b\\121.txt")
#复制整个目录(备份)，目标文件夹需要不存在
shutil.copytree("src","dec")

#删除文件
os.unlink("C:\\b\\1.txt")
os.unlink("C:\\b\\121.txt")
#删除空文件夹
try:
    os.rmdir("C:\\b\\new_a")
except Exception as ex:
    print("错误信息："+str(ex))#提示：错误信息，目录不是空的
#删除文件夹及内容
shutil.rmtree("C:\\b\\new_a")

#移动文件
shutil.move("C:\\a\\1.txt","C:\\b")
#移动文件夹
shutil.move("C:\\a\\c","C:\\b")

#重命名文件
shutil.move("C:\\a\\2.txt","C:\\a\\new2.txt")
#重命名文件夹
shutil.move("C:\\a\\d","C:\\a\\new_d")



# https://www.jianshu.com/p/b9da5fd2e5cf

# 压缩文件
# --------------
import zipfile
# 加载压缩文件，创建ZipFile对象
# class zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# 参数file表示文件的路径或类文件对象(file-like object)
# 参数mode指示打开zip文件的模式，默认值为'r'，表示读已经存在的zip文件，也可以为'w'或'a'，
# 'w'表示新建一个zip文档或覆盖一个已经存在的zip文档，'a'表示将数据附加到一个现存的zip文档中
# 参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。
# 如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。
file_dir = 'D:/text.zip'
zipFile = zipfile.ZipFile(file_dir)

# 01 ZipFile.infolist() 获取zip文档内所有文件的信息，返回一个zipfile.ZipInfo的列表
print(zipFile.infolist())
# 02 ZipFile.namelist() 获取zip文档内所有文件的名称列表
print(zipFile.namelist())
# 03 ZipFile.printdir() 将zip文档内的信息打印到控制台上
print(zipFile.printdir())


# 解压文件
# ----------
import zipfile
import os
zipFile = zipfile.ZipFile(file_dir)
for file in zipFile.namelist():
    zipFile.extract(file, 'd:/Work')
zipFile.close()


'''
python日志封装
--------------
https://blog.csdn.net/cyh1111/article/details/53405795?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight
封装成为单例模式
'''
import os
import logging
import logging.handlers
import threading


class Logger(logging.Logger):
    _instance_lock = threading.Lock()

    def __init__(self, log_path=None):
        """
        初始化
        :param log_path: 日志保存路径
        :return:
        """
        super(Logger, self).__init__(self)
        log_format = "[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[" \
                     "process:%(process)s] - %(message)s "
        data_format = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(log_format, data_format)
        # 控制台输出log
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)
        # 写入文件log
        if log_path is not None:
            log_file_path = os.path.abspath(log_path) + '/logs'
            if not os.path.exists(log_file_path):
                os.makedirs(log_file_path)
            output_handler = logging.handlers.RotatingFileHandler(filename=log_file_path + '/log.txt', encoding='utf-8',
                                                                  maxBytes=10 * 1024 * 1024, backupCount=10)
            output_handler.setLevel(logging.DEBUG)
            output_handler.setFormatter(formatter)
            self.addHandler(output_handler)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)
            return cls._instance
        return cls._instance


if __name__ == '__main__':
    log1 = Logger()
    log2 = Logger()
    log3 = Logger()
    print(id(log1) == id(log2) == id(log3))




'''
json.dumps(), json.loads()
-----------------------
https://blog.csdn.net/lizhixin705/article/details/82344209
'''

1.将数据结构转为json
import json
data = {
    'name' : 'myname',
    'age' : 100,
}
json_str = json.dumps(data)


2.json.loads将一个JSON编码的字符串转换回一个Python数据结构：

data = json.loads(json_str)

3. json.dump() 和 json.load() 来编码和解码JSON数据,用于处理文件。
with open('test.json', 'w') as f:
    json.dump(data, f)
 
with open('test.json', 'r') as f:
    data = json.load(f)



把字符串转为数据结构：
-------------------
# https://blog.csdn.net/weixin_33729196/article/details/94672998


# No.1:通过json:
>>> import json
>>> user_info= '{"name" : "john", "gender" : "male", "age": 28}'
>>> user_dict = json.loads(user_info)
# 局限： key-value必须用双引号的字符串

# No.2:通过eval
>>> user_info = '{"name" : "john", "gender" : "male", "age": 28}'
>>> user_dict = eval(user_info)
# 局限:存在一些安全性问题

# No.3:通过literal_eval
import ast
message = ast.literal_eval(self.content)





单例模式：
-----------------
https://www.jianshu.com/p/6a1690f0dd00





python执行os的命令：
---------------------------------------
# https://www.jb51.net/article/186301.htm


# 1. os.system('cmd')

import os
val = os.system('ls -al')
print (val)


# 2. os.popen('cmd')
#用read(),readlines()读取执行的结果：

val = os.popen('ls -al')
for temp in val.readlines():
    print (temp)


# 3. 使用commands模块，有三个方法可以使用：

（1）commands.getstatusoutput(cmd)，其以字符串的形式返回的是输出结果和状态码，即（status,output）。
（2）commands.getoutput(cmd)，返回cmd的输出结果。
（3）commands.getstatus(file)，返回ls -l file的执行结果字符串，调用了getoutput，不建议使用此方法


# 4. subprocess模块，允许创建很多子进程，创建的时候能指定子进程和子进程的输入、输出、错误输出管道，执行后能获取输出结果和执行状态。
 (1）subprocess.run()：python3.5中新增的函数， 执行指定的命令， 等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
（2）subprocess.call()：执行指定的命令， 返回命令执行状态， 功能类似os.system（cmd）。
（3）subprocess.check_call()：python2.5中新增的函数, 执行指定的命令, 如果执行成功则返回状态码， 否则抛出异常。




os.system()传递参数：
--------------------
# https://blog.csdn.net/njafei/article/details/72764990

os.system("shell command argusFormat" % argus)

# 单个参数
param = "I'm param"
os.system("python haha.py %s" % (param))

# 多个参数
paramA = "I'm paramA"
paramB = "I'm paramB"
os.system("python haha.py %s %s" % (paramA,paramB))


# python格式化字符：

%s    字符串 (采用str()的显示)

%r    字符串 (采用repr()的显示)

%c    单个字符

%b    二进制整数

%d    十进制整数

%i    十进制整数

%o    八进制整数

%x    十六进制整数

%e    指数 (基底写为e)

%E    指数 (基底写为E)

%f    浮点数

%F    浮点数，与上相同

%g    指数(e)或浮点数 (根据显示长度)

%G    指数(E)或浮点数 (根据显示长度)

%%    字符"%"



# python注入shell变量：
--------------------
https://www.cnblogs.com/momoyan/p/9145992.html

python -> shell：
-----------------
# 1.环境变量

import os
var=123 #或var='123'  
os.environ['var']=str(var)  #environ的键值必须是字符串   
os.system('echo $var')  

# 2.字符串连接

import os  
path='/root/a.txt'
var=[1]  
var='bash'  
os.system('echo ' + path)                  #注意echo后有空格   
os.system('echo ' + str(var[0]))  
os.system('echo ' + var + ' /root/c.sh') #注意echo后和/root前有空格    
 

# 3.通过管道
import os  
var='123'  
os.popen('wc -c', 'w').write(var)  
 

# 4.通过文件

output = open('/tmp/mytxt', 'w')  
output.write(S)      #把字符串S写入文件   
output.writelines(L) #将列表L中所有的行字符串写到文件中   
output.close()  

# 5.通过重定向标准备输出

buf = open('/root/a.txt', 'w')  
print >> buf, '123\n', 'abc'  
# 或

print >> open('/root/a.txt', 'w'), '123\n', 'abc' #写入或生成文件   
print >> open('/root/a.txt', 'a'), '123\n', 'abc' #追加  
 


shell -> python：
----------------
# 1.管道

import os  
var=os.popen('echo -n 123').read() 
print var  
 
# 2.

import commands  
var=commands.getoutput('echo abc')       #输出结果   
var=commands.getstatusoutput('echo abc') #退出状态和输出结果  

# 3.文件

input = open('/tmp/mytxt', 'r')  
S = input.read( )      #把整个文件读到一个字符串中   
S = input.readline( )  #读下一行（越过行结束标志）   
L = input.readlines( ) #读取整个文件到一个行字符串的列表中  

input = open('/tmp/mytxt', 'r')  
# 本文转载自：https://blog.csdn.net/blackmanren/article/details/12904603



上传文件模块：
-----------
https://www.jianshu.com/p/9738e53a7db3

pip install requests_toolbelt



from requests_toolbelt import MultipartEncoder

encoder = MultipartEncoder({
            'field': ('file_name', b'{"a": "b"}', 'application/json',
                      {'X-My-Header': 'my-value'})
        })

'''
field：服务端约定的上传文件字段名。一般用到的是file，需要和服务端沟通获取。

file_name: 文件名。一般可以任意写，服务端大多是拿到文件后自己再次命名。

b'{"a":"b"}'：文件内容。例：open('/your/file/path', 'rb')

'application/json'：文件的MimeType。不同文件类型对应的MimeType可以到这里查询。

{'X-My-Header': 'my-value'}：其他内容，可不传。


android和ios的安装文件MIME类型
.apk:
application/vnd.android.package-archive

.ipa:
application/octet-stream.ipa
'''


import requests
from requests_toolbelt import MultipartEncoder


upload_url = 'https://your/upload/url'
payload = {
    'file': ('upload.pdf', open('sync_test.pdf', 'rb'), 'application/pdf')
}
m = MultipartEncoder(payload)


headers = {
    "Content-Type": m.content_type,
    "other-keys": "other-values"
}

r = requests.post(upload_url, headers=headers, data=m)
print(r.json())





上传文件的两种方式：
----------------
https://www.cnblogs.com/shuzf/p/11972116.html

https://blog.csdn.net/xy_best_/article/details/92839653


# 方式一”
from requests_toolbelt import MultipartEncoder
import requests

# from_data上传文件，注意参数名propertyMessageXml
data = MultipartEncoder(fields={'propertyMessageXml': ('filename', open('D:/123.xml', 'rb'), 'text/xml')})
requests.post(url=url,data=data,headers={ 'Content-Type': data.content_type})

#raw上传文件
file = open('D:/123.xml','rb')
requests.post(url=url,data=file.read(),headers={'Content-Type':'text/xml'})

#binary上传文件
files={'file':open('D:/123.xml','rb')}
requests.post(url=url,files=files,headers={'Content-Type':'binary'})



# 方式二：

import requests,glob
from urllib3 import encode_multipart_formdata

def upload_file(url=None,path=None,file_path=None):
    if path:
        for file_path in glob.glob(path + '\*'): #批量文件
            data={}
            data['file'] = (file_path.split("/")[-1], open(file_path, 'rb').read())  # 名称，读文件
            encode_data = encode_multipart_formdata(data)
            res = requests.post(url, headers={'Content-Type':encode_data[1]},data=encode_data[0])
            return res.text
    if file_path:
        data = {}
        data['file'] = (file_path.split("/")[-1], open(file_path, 'rb').read())  # 名称，读文件
        encode_data = encode_multipart_formdata(data)
        res = requests.post(url, headers={'Content-Type': encode_data[1]}, data=encode_data[0])
        return res.text





画图：
---------
'''
https://blog.csdn.net/w576233728/article/details/86538060?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.control

https://blog.csdn.net/jenyzhang/article/details/52046372

https://www.cnblogs.com/onemorepoint/p/7482644.html

https://blog.csdn.net/qq_34859482/article/details/80617391

绘制折线统计图的时候：
marker关键字参数可以和color以及linestyle这两个关键字参数合并为一个字符串

pip install numpy
pip install scipy
sudo apt-get install python-matplotlib
'''



#绘制sin曲线
import numpy as np
import matplotlib.pyplot as plt
 
#设置x,y轴的数值（y=sinx）
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
 
#创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
plt.figure(figsize=(8,4))
 
#在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
plt.plot(x,y1,label="$sin(x)$",color="green",linewidth=2)
plt.plot(x,y2,label="$cos(x)$",color="blue",linewidth=2)

#X轴的文字
plt.xlabel("Time(s)")
#Y轴的文字
plt.ylabel("Volt")
#图表的标题
plt.title("PyPlot First Example")
 
#Y轴的范围
plt.ylim(-1.2,1.2)
 
#显示图示
plt.legend()
#显示图
plt.show()
#保存图
plt.savefig("sinx.jpg")


# 设置默认字体，为了避免中问字体写入的时候有问题，
# 设置过此字体不生效
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False


# 设置尺寸：
# plt.figure(figsize=(8, 8)) # 像素缺省值为80dpi,这而宽度为8*80 = 640px;

# 设置x,y坐标
# x1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
# y1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的y轴坐标

# np.arange(0, 5, 0.1)


# 折线图
# l1 = plt.plot(byte1, speed1, colors1, linewidth=1, label='mainland')
# l2 = plt.plot(byte2, speed2, colors2, linewidth=1, label='taiwan')
# 折线图可以一条一条画，也可以一个语句画
# plt.plot(byte1, speed1, 'ro-', byte2, speed2, 'g+-', x3, y3, 'b^-')


# 柱状图
# width = 0.1
# plt.bar(byte1, speed1, width, color='orange')

# 扇形图
# data = [50, 10, 10]
# labels = ['apple', 'pear', 'orange']
# plt.pie(data, labels=labels, autopct='%1.2f%%')

numpy, pandas
------------
https://blog.csdn.net/cxmscb/article/details/54583415

import pandas as pd

dt = pd.read_csv('you_csv.csv')
print(max(dt['dates']))
print(min(dt['dates']))



关于浅拷贝和深拷贝：
-----------------
https://blog.csdn.net/weixin_44870139/article/details/108273106


gunicorn
----------
https://www.jianshu.com/p/69e75fc3e08e
Gunicorn是一个unix上被广泛使用的高性能的Python WSGI UNIX HTTP Server。
和大多数的web框架兼容，并具有实现简单，轻量级，高性能等特点。

gunicorn + flask：

pip install gunicorn
pip install flask


flask简介：
https://www.jianshu.com/p/6452596c4edb


json.dumps()的坑
----------------
https://www.cnblogs.com/stubborn412/p/3818423.html
print(json.dumps(result, indent='\t', ensure_ascii=False))


python字符串补0方式：
---------------------
https://blog.csdn.net/weixin_42317507/article/details/93411132
https://zhidao.baidu.com/question/144464742.html
'''
原字符串左侧对齐， 右侧补零:
'''
str.ljust(width,'0') 
input: '789'.ljust(32,'0')
output: '78900000000000000000000000000000'


'''
原字符串右侧对齐， 左侧补零:
方法一：
'''
str.rjust(width,'0') 
input: '798'.rjust(32,'0')
output: '00000000000000000000000000000798'
'''
方法二：
'''
str.zfill(width)
input: '123'.zfill(32)
output:'00000000000000000000000000000123'
'''
方法三：
'''
'%07d' % n
input: '%032d' % 89
output:'00000000000000000000000000000089'

>>> '%03x' % 17
'011'
>>> '%03o' % 17
'021'

>>> '%03x' % 123
'07b'
>>> '%03X' % 123
'07B'

>>> '%0.3f' % 3.1215936
'3.122'
>>> '%07.4f' % 3.12159365458
'03.1216'


>>> '%03d' % 12.35364364
'012'
>>> '%3d' % 12.35364364
' 12'

>>> '%03f' % 3.12159365458
'3.121594'
>>> '%3f' % 3.1215936
'3.121594'
>>> '%4f' % 12.35364364
'12.353644'
>>> '%10f' % 12.35364364
' 12.353644'
>>> '%010f' % 12.35364364
'012.353644'
>>> '%012f' % 12.35364364
'00012.353644'

>>> '%-12f' % 12.35364364
'12.353644   '
>>> '%-012f' % 12.35364364
'12.353644   '
>>> '%+012f' % 12.35364364
'+0012.353644'

'''
type意义
d 有符号10进制整数
i 有符号10进制整数
o 无符号8进制整数
u 无符号10进制整数
x 无符号的16进制数字，并以小写abcdef表示
X 无符号的16进制数字，并以大写ABCDEF表示
F/f 浮点数
E/e 用科学表示格式的浮点数
g 使用%f和%e表示中的总的位数表示最短的来表示浮点数 G 同g格式，但表示为指数
c 单个字符
s 字符串
% 显示百分号本身

flag格式：
无 右对齐，左边填充0和空格
- 左对齐，右边填充空格
+ 在数字前增加符号 + 或 -
0 将输出的前面补上0，直到占满指定列宽为止（不可以搭配使用-）
'''

>>> round(12.12345678, 8)
12.12345678
>>> round(12.12345678900, 8)
12.12345679
>>> round(12.12345678900, 10)
12.123456789


format用法详解：
-------------
https://segmentfault.com/a/1190000037571463


>>> '{:-^10}'.format('haha')
'---haha---'
>>> f"{'你说呢':-^20}"
'--------你说呢---------'


格式化打印
----------
https://www.cnblogs.com/lowmanisbusy/p/12683897.html

# 方式1
import pprint
# indent：定义几个空格的缩进
pp = pprint.PrettyPrinter(indent=2)
info = dict(age=50, money=0, a=1, b=dict(h=7, i=8, j=9), c=2, d=3, e=4, f=5, g=6)
pp.pprint(info)

# 方式2
import json
info = dict(age=50, money=0, a=1, b=dict(h=7, i=8, j=9), c=2, d=3, e=4, f=5, g=6)
# indent：定义几个空格的缩进
# separators：定义 "," ":" 前后的空格数量
print(json.dumps(info, indent=1, separators=(', ', ': '), ensure_ascii=False))



copy和deepcopy
---------------------
import copy

copy.deepcopy


csv

import csv
with open(file_path) as csv_file:
    reader = csv.reader(csv_file) #读出来是个每行数据组成的list
    item_list = [{'url': row[0], 'sign':row[1]} for row in reader]

    #读取某一行
    for i, j in enumerate(reader) #i是list reader的每个元素的index, j是list中没个元素的值


with open(file_path) as csv_file:
    reader = csv.DictReader(csv_file) #读出来是每一行为字典，key为每列的头

    for i in csv_file: #如果不用reader去读，那么没一行是str类型



def analyse_data(file_path):
    if not os.path.exists(file_path):
        log.error(f'[file: {file_path}]不存在！')
        return
    item_list = []
    if file_path.endswith('.csv'):
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file)
            item_list = [{'url': row[0], 'sign':row[1]} for row in reader]
    else:
        item = {}
        file_lines = linecache.getlines(file_path)
        for single_line in file_lines:
            if single_line.strip() == "":
                continue
            # ...


def get_data(folder_path, pretty=False):
    if not (os.path.exists(folder_path) and os.path.isdir(folder_path)):
        log.error(f'[folder: {folder_path}] is not exist or is not a folder!')
        return
    output1, output2, output3 = [], [], []
    files = os.popen('ls {}'.format(folder_path)).read().split('\n')[:-1]
    for filename in files:
        modified_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(os.stat(folder_path + "/" + filename).st_mtime))
        log.info('find file: {}, modified time: {}'.format(filename, modified_time))
        sheet1, sheet2, sheet3 = analyse_data('{}/{}'.format(folder_path, filename))
        output1.extend(sheet1.values())
        output2.extend(sheet2)
        output3.extend(sheet3)
    return output1, output2, output3


def make_xlsx(filename, data, headers):
    workbook = xlsxwriter.Workbook("{}.xlsx".format(filename))

    bold = workbook.add_format({'bold': 1})
    tags = list(string.ascii_letters[26:])
    column_tags = tags.copy()
    for t1 in tags:
        for t2 in tags:
            column_tags.append(t1 + t2)
    for i in range(len(headers)):
        worksheet = 'sheet' + str(i)
        worksheet = workbook.add_worksheet(worksheet)
        # 表头
        headings = headers[i]
        worksheet.write_row('A1', headings, bold)
        # 写入数据
        for column_index in range(len(headers[i])):
            worksheet.write_column(column_tags[column_index] + "2", data[i][column_index])
    workbook.close()



def judge_file_type(name):
    try:
        re.match(r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}/\w{2}/\w{3}$', name).group()
    except Exception as e:
        return 'download'
    else:
        return 'upload'





locust:
-----------
https://docs.locust.io/en/latest/quickstart.html
https://blog.csdn.net/luoman876/article/details/105652423

#基础：
https://debugtalk.com/post/head-first-locust-user-guide/
#参数关联：
https://debugtalk.com/post/head-first-locust-advanced-script/

疑难杂症：
在模拟有效并发方面，Locust的优势在于其摒弃了进程和线程，完全基于事件驱动，
使用gevent提供的非阻塞IO和coroutine来实现网络层的并发请求，因此即使是单台压力机也能产生数千并发请求数；
再加上对分布式运行的支持，理论上来说，Locust能在使用较少压力机的前提下支持极高并发数的测试。

'''

1.定义task权重的两种方法：
from locust import TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def test_job1(self):
        self.client.get('/job1')

    @task(2)
    def test_job2(self):
        self.client.get('/job2')
        
---------------------------   
from locust import TaskSet

def test_job1(obj):
    obj.client.get('/job1')

def test_job2(obj):
    obj.client.get('/job2')

class UserBehavior(TaskSet):
    tasks = {test_job1:1, test_job2:2}
    # tasks = [(test_job1,1), (test_job1,2)] # 两种方式等价
'''

from locust import HttpUser, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):   #初始化，只执行一次，和LR中vuser_init功能相同
        self.client.post("/login", {
            "username": "test",
            "password": "123456"
        })

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)  #权重不配置的话，默认比例为1：1
    def about(self):
        self.client.get("/about/")

    def on_stop(self):
        pass

class WebsiteUser(HttpUser):
    tasks = [WebsiteTasks]
    host = "https://debugtalk.com"
    min_wait = 1000  #时间不配置的话默认为 1s， 这儿单位为ms
    max_wait = 5000


if __name__ == '__main__':
    pass


https://docs.locust.io/en/latest/changelog.html#changelog-1-0
no-web改成了headless, -c 换成了-u
HttpLocust换成了HttpUser
task_set换成tasks,且接受一个list

locust -f ./load_test.py --host=https://www.baidu.com
locust -f load_test.py --host=https://www.baidu.com --headless -u 10 -r 2 -t 1m


2.我们在Locust处理值关联时，通过官方库函数re.search就能实现所有需求。
甚至针对html页面，我们也可以采用lxml库，通过etree.HTML(html).xpath来更优雅地实现元素定位。

3.分为 web和no-web模式： --headless
locust -f locustfile.py --no_web -c 1 -n 1


Locust是通过在Terminal中执行命令进行启动的，通用的参数有如下两个：

-H, --host：被测系统的host，若在Terminal中不进行指定，就需要在Locust子类中通过host参数进行指定；
-f, --locustfile：指定执行的Locust脚本文件；


单进程模式：no_web

locust -H https://debugtalk.com -f demo.py --no-web -c1 -n2

如果采用no_web形式，则需使用--no-web参数，并会用到如下几个参数。

-c, --clients：指定并发用户数；
-n, --num-request：指定总执行测试；
-r, --hatch-rate：指定并发加压速率，默认值位1。



web模式：
locust -H https://debugtalk.com -f demo.py
-P, --port：指定web端口，默认为8089


多进程分布式运行：
单机多进程/多机负载
locust -H https://debugtalk.com -f demo.py --master --port=8088
locust -H https://debugtalk.com -f demo.py --slave
locust -H https://debugtalk.com -f demo.py --slave --master-host=<locust_machine_ip>   #如果不在同一台主机上，那么需要指定ip


4.响应指标：
相比于LoadRunner，Locust的结果展示十分简单，主要就四个指标：并发数、RPS、响应时间、异常率。



用go_lang来编写压测工具
---------------------
https://myzhan.github.io/




nonlocal的作用域
---------------
https://www.cnblogs.com/tallme/p/11300822.html


闭包：
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x =0
    def counter():
        nonlocal x
        x = x+1
        return x
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



callable
---------
https://zhuanlan.zhihu.com/p/191419441

>>> callable(int)
True

# python中的方法，函数，类都是可以回调的

class Stu(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        self.run()

    def run(self):
        print('{name} is running'.format(name=self.name))

stu = Stu('小明')
print(callable(stu))    # True
stu()                   # 小明 is running



from random import randint
print(randint(1,3))



# 最值得学习的python库
# ------------------
# http://www.testclass.net/post/2021_python_lib
jsonschema
algorithms
howdoi
you-get

# 自动修正命令
pip install thefuck   # 或者brew install thefuck 


you-get
----------
https://you-get.org/
下载油管，b站视频用的
pip install you-get
brew install you-get

useage
you-get -i 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
you-get https://www.youtube.com/watch\?v\=kA3k8LNHX4Y // 默认下载第一个
you-get --itag=137 https://www.youtube.com/watch\?v\=fnmldw8HpUU  //下载指定tag



String倒序输出：
方法一：通过步长
>>> 'abcdefg'[::-1]
'gfedcba'

方法二：通过list的reverse()
>>> s = 'abcdfeghi'
>>> ''.join(sorted(list(s),reverse=True))
'ihgfedcba'

