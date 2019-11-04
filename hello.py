#!/usr/bin/env python3.x
# -*- coding: utf-8 -*-



re
===================================
https://blog.csdn.net/Winterto1990/article/details/47361955
https://so.csdn.net/so/search/s.do?q=python%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%20re&t=blog&u=Winterto1990
https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

>>> import re
>>> dir(re)
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']


re.match(pattern, string, flags)  #返回值: 为真或者假。
re.search(pattern, string, flags)  #返回值：如果查找到则返回查找到的值，否则返回为None




re.compile
---------------
import re
content='Where are you from? You look so hansome.'
regex=re.compile(r'\w*som\w*')
m=regex.search(content)
if m:
    print (m.group(0))  #中间的0的意义没懂？ https://blog.csdn.net/Winterto1990/article/details/47361955
else:
    print ("Not found")



MatchObject 实例有几个方法和属性；
重要的如下：
group() 返回被 RE 匹配的字符串
start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置


re = requests.post(CMS_URL+SUBMIT_URL, data=pay_load, cookies=CMS_COOKIES)
re.raise_for_status()  #re的状态，正常的话返回none，否则抛异常
print (re.text)
re_json = re.json()

re.json()返回的类型为dict
re.text 返回的类型为string



字符拼接的方法：
https://www.cnblogs.com/blogsxyz/p/9019836.html
    1. str1+str2
    2. ''.join(Array)
    >>> b = ['1','2','3']
    >>> b.join('')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'list' object has no attribute 'join'
    >>> ''.join(b)
    '123'
    
    3. ,拼接
    4. format拼接


返回多个值：
实质是返回一个tuple
https://www.cnblogs.com/wllhq/p/8119347.html





python requests：
POST request payload形式的请求：
---------------------------------
https://blog.csdn.net/zwq912318834/article/details/79930423
https://blog.csdn.net/pittpakk/article/details/81218566




定时器：
----------------------
https://www.jianshu.com/p/403bcb57e5c2
https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/
https://juejin.im/post/5c8918f5f265da2dd6393633


阻塞函数sleep:
-------------
from datetime import datetime
import time
# 每n秒执行一次
def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
        time.sleep(n)

timer(5)


阻塞函数sched:
-------------
import sched
import time
schedule = sched.scheduler(time.time, time.sleep)
schedule.enter(3, 0, sticker_publish, (platform, pid, name,))
schedule.run()


import sched
import time
from datetime import datetime
# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二参数可以在定时未到达之前阻塞
schdule = sched.scheduler(time.time, time.sleep)
# 被周期性调度触发函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,))
# 默认参数60s
def main(inc=60):
    # enter四个参数分别为：间隔事件,优先级（用于同时到达两个事件同时执行的顺序），被调度触发的函数
    # 给该触发器函数的参数（tuple形式）
    schedule.enter(0, 0, pirntTime, (inc,))
    schedule.run()
# 5秒输出一次
main(5)


schedule
--------------
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


APScheduler定时框架:应该也是阻塞
-----------------------------
pip install apscheduler
APScheduler 四个组件分别为：触发器(trigger)，作业存储(job store)，执行器(executor)，调度器(scheduler)。


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# 输出时间
def job():
    print(datetime.now().strtime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, "cron"， day_of_week="1-5", hour=6, minute=30)
'''
APScheduler 有三种内建的 trigger:
date: 特定的时间点触发
interval: 固定时间间隔触发
cron: 在特定时间周期性地触发

job store：
APScheduler 默认使用 MemoryJobStore，可以修改使用 db 存储方案

executor 有两种：
ProcessPoolExecutor
ThreadPoolExecutor

'''
schduler.start()

# background

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=5)
sched.start()



Sqlalchemy
-----------

非阻塞函数Timer：
-------------
from datetime import datetime
from threading import Timer
# 打印时间函数
def prinTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime,(inc,))
    t.start()

printTime(2)

停掉计时器用cancel()
t.cancel()

#10s后执行
from datetime import datetime
from threading import Timer
def hello(): 
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
t = Timer(10.0, hello) 
t.start()



pillow:
-------------
from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB",(50,50),"white")
draw_table = ImageDraw.Draw(im=image)
draw_table.text(xy=(0, 0), text=u'仰', fill='#000000', font=ImageFont.truetype('./SimHei.ttf', 50))
 
image.show()  # 直接显示图片
image.save('满月.png', 'PNG')  # 保存在当前路径下，格式为PNG

'''
# 图片中文字居中：
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

python执行系统之间的区别；
----------------------
https://www.cnblogs.com/yunguoxiaoqiao/p/7588725.html
Python3默认编码是unicode；而Python2是ASCII码。Windows环境默认是gbk编码。
Py3 自动把文件编码转为unicode，Python2并不会自动的把文件编码转为unicode存在内存里。需要手动转码。

手动转码规则：

UTF-8 --> decode 解码 --> Unicode
Unicode --> encode 编码 --> GBK / UTF-8 等
使用type可以查看编码形式，unicode是‘unicode’,gbk和utf-8是‘str或bytes’。






'''
判断操作系统类型
——————————————
原文链接：https://blog.csdn.net/gatieme/article/details/45674367
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
os.path.existe()函数用来检验给出的路径是否真地存在
os和os.path模块
os.listdir(dirname)：列出dirname下的目录和文件
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
————————————————
原文链接：https://blog.csdn.net/gatieme/article/details/45674367
'''



'''
Sys模块
————————————
sys.argv: 实现从程序外部向程序传递参数。
sys.exit([arg]): 程序中间的退出，arg=0为正常退出。
sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。
sys.setdefaultencoding(): 设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding(‘utf8’)，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）
sys.getfilesystemencoding(): 获取文件系统使用编码方式，Windows下返回’mbcs’，mac下返回’utf-8’.
sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。
sys.platform: 获取当前系统平台。
sys.stdin,sys.stdout,sys.stderr stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
'''



'''
Paltform模块
————————————
platform.system() 获取操作系统类型，windows、linux等
platform.platform() 获取操作系统，Darwin-9.8.0-i386-32bit
platform.version() 获取系统版本信息 6.2.0
platform.mac_ver()
platform.win32_ver() (‘post2008Server’, ‘6.2.9200’, ”, u’Multiprocessor Free’)
————————————————
原文链接：https://blog.csdn.net/gatieme/article/details/45674367
'''



try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass