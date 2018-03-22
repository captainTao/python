#!/usr/bin/env python
# -*- coding: utf-8 -*-



'''
装饰器：
http://www.cnblogs.com/weke/articles/5744793.html
https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
'''
# 举例：给函数加一个输出的log:
def outer(func):
    def log():
        print('out log')
        func()
    return log
@outer
def f1():
    print('函数f1')
@outer
def f2():
    print('函数f2')
@outer
def f3():
    print('函数f3')
f1()
# out log
# 函数f1




# 返回值为None的装饰器：
def outer(func):
    def log():
        print('out log')
        func()
    return log
 
 
@outer
def f1():
    print('函数f1')
f1()


# 装饰器的函数参数是万能的，即使func的函数：也就是什么参数都是可以接受的，见实现的过程：
def outer(func):
    def log(*args,**kwargs):
        r=func(*args,**kwargs)
        return r
    return log
@outer
def add(a,b,c):
    return a+b+c


# 参数为函数的一种形式，见实现的代码：
def outer(func):
    def log(*args,**kwargs):
        r=func(*args,**kwargs)
        return r
    return log
  
def result(a,b):
    print(a+b)
 
@outer
def add(sum):
    '''函数的参数为函数'''
    return sum
add(result(2,3)) # 5



# 后台登录系统：
import  sys 
LOGIN_USER={"is_login":False}
 
def admin():
    '''后台管理系统'''
    if LOGIN_USER['is_login']:
        print('欢迎%s访问无涯后台管理系统'%LOGIN_USER['current_user'])
    else:
        print('请先登录系统，谢谢！')

def login(username,password):
    if username=='admin' and password=='admin':
        LOGIN_USER['is_login']=True
        LOGIN_USER['current_user']=username
        admin()
    else:
        print('用户名或者密码错误')

def order():
    if LOGIN_USER['is_login']:
        print('欢迎%s访问无涯后台管理系统'%LOGIN_USER['current_user'])
    else:
        print('请先登录系统，谢谢！')
 

def main():
    while True:
        f=input('1、后台管理系统 2、查看订单 3、登录 4、退出系统\n')
        if f=='1':
            admin()
        elif f=='2':
            order()
        elif f=='3':
            username=input('请输入用户名:\n')
            password=input('请输入密码:\n')
            login(username,password)
        elif f=='4':
            sys.exit(1)
main()



#上面功能模块用装饰器重构后：(登录步骤用装饰器)
import  sys 
LOGIN_USER={"is_login":False}
def wuya(func):
    def inner():
        if LOGIN_USER['is_login']:
            r=func()
            return r
        else:
            print('请先登录系统，谢谢！')
    return inner
 
def f1():
    print('欢迎%s访问无涯后台管理系统'%LOGIN_USER['current_user'])
 
 
@wuya
def admin():
    '''后台管理系统'''
    f1()
 
def login(username,password):
    if username=='admin' and password=='admin':
        LOGIN_USER['is_login']=True
        LOGIN_USER['current_user']=username
        admin()
    else:
        print('用户名或者密码错误')
  
@wuya
def order():
    f1()
 
def main():
    while True:
        f=input('1、后台管理系统 2、查看订单 3、登录 4、退出系统\n')
        if f=='1':
            admin()
        elif f=='2':
            order()
        elif f=='3':
            username=input('请输入用户名:\n')
            password=input('请输入密码:\n')
            login(username,password)
        elif f=='4':
            sys.exit(1)
main()




'''------------------------------------------------------------'''

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2013-12-25'

>>> now()
call now():
2013-12-25


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

>>> now()
execute now():
2013-12-25


和两层嵌套的decorator相比，3层嵌套的效果是这样的：
>>> now = log('execute')(now)

但此时：
>>> now.__name__
'wrapper'

为了避免签名错误，所以代码应该如下：@functools.wraps(func)的作用就是解决__name__属性被更改的状况


import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator



'''
小结：
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
Python的decorator可以用函数实现，也可以用类实现。
decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

'''

1.请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
2.再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：
@log('execute')
def f():
    pass


源码参考：
# 不带参数：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
now()
print now.__name__

# 带参数：
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')
today()
print(today.__name__)

>>>
call now():
2015-3-25
now
DEBUG today():
2015-3-25
today


题目1：
import functools

def log(func):
    @functools.wraps(func)  # wrap '__name__'
    def wrapper(*args, **kw):
        print("begin call [%s]" % (func.__name__))
        func_tmp = func(*args, **kw)
        print("end call [%s]" % (func.__name__))
        return func_tmp

    return wrapper


@log  # 借助Python的@语法，把decorator置于函数的定义处
def hello():
    print("hello")

hello()

>>>
begin call [hello]
hello
end call [hello]

'''''思考一下能否写出一个@log的decorator，使它既支持：@log 
                                                def f(): 
                                                pass 
又支持：@log('execute') 
        def f(): 
        pass '''  

import functools  
  
def log(text):  
    def decorator(func):  
        @functools.wraps(func) # wrap '__name__'  
        def wrapper(*args, **kw):  
            if (None != text):  
                print("[%s]begin call [%s]" % (text, func.__name__))  
                func_tmp = func(*args, **kw)  
                print("[%s]end call [%s]" % (text, func.__name__))  
            else:  
                print("begin call [%s]" % (func.__name__))  
                func_tmp = func(*args, **kw)  
                print("end call [%s]" % (func.__name__))  
            return func_tmp   
        return wrapper  
  
    if isinstance(text, str):  
        return decorator  
    else:  
        strtmp = text  
        text = None  
        return decorator(strtmp)  
 
@log  
def hello():  
    print("hello")  
hello() 


@log('>>>world')  
def hello():  
    print("hello")  
hello() 




#网友解答：
import functools
def log(args):
    text = "just call"
    def decoration(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text,func.__name__)
            result = func(*args, **kw)
            return result
        return wrapper
    if hasattr(args, '__call__'): # 这儿没看懂
        #返回decoration内层函数wrapper
        return decoration(args)
    else:
        text = args
        #直接返回decoration
        return decoration
@log
def f1():
    pass
@log("excute")
def f2():
    pass
f1()
f2()


# 自我解答
import functools
def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        #functools.wraps的意义等同wrapper.__name__ = func.__name__，即：把函数的属性名重新赋值一次
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log()
def now():
    print '2013-12-24'
now()
@log('execute')
def tomorrow():
    print '2013-12-25'
tomorrow()

