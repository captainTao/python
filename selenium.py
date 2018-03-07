#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
selenium定位方法
http://www.testclass.net/selenium_python/find-element/

Selenium提供了8种定位方式。
    1. id
    2. name
    3. class name
    4. tag name
    5. link text
    6. partial link text
    7. xpath
    8. css selector

这8种定位方式在Python selenium中所对应的方法为：
    1. find_element_by_id()
    2. find_element_by_name()
    3. find_element_by_class_name()
    4. find_element_by_tag_name()
    5. find_element_by_link_text()
    6. find_element_by_partial_link_text()
    7. find_element_by_xpath()
    8. find_element_by_css_selector()


定位方法的用法
假如我们有一个Web页面，通过前端工具（如，Firebug）查看到一个元素的属性是这样的。

<html>
  <head>
  <body link="#0000cc">
    <a id="result_logo" href="/" onmousedown="return c({'fm':'tab','tab':'logo'})">
    <form id="form" class="fm" name="f" action="/s">
      <span class="soutu-btn"></span>
        <input id="kw" class="s_ipt" name="wd" value="" maxlength="255" autocomplete="off">
我们的目的是要定位input标签的输入框。

通过id定位
dr.find_element_by_id("kw")


通过name定位:
dr.find_element_by_name("wd")

通过class name定位:
dr.find_element_by_class_name("s_ipt")

通过tag name定位:
dr.find_element_by_tag_name("input")


通过xpath定位，xpath定位有N种写法，这里列几个常用写法:

dr.find_element_by_xpath("//*[@id='kw']")
dr.find_element_by_xpath("//*[@name='wd']")
dr.find_element_by_xpath("//input[@class='s_ipt']")
dr.find_element_by_xpath("/html/body/form/span/input")
dr.find_element_by_xpath("//span[@class='soutu-btn']/input")
dr.find_element_by_xpath("//form[@id='form']/span/input")
dr.find_element_by_xpath("//input[@id='kw' and @name='wd']")


通过css定位，css定位有N种写法，这里列几个常用写法:

dr.find_element_by_css_selector("#kw")  #类似于JQ里面的写法
dr.find_element_by_css_selector("[name=wd]")
dr.find_element_by_css_selector(".s_ipt")
dr.find_element_by_css_selector("html > body > form > span > input")
dr.find_element_by_css_selector("span.soutu-btn> input#kw")
dr.find_element_by_css_selector("form#form > span > input")


接下来，我们的页面上有一组文本链接。

<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
<a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>
通过link text定位:

dr.find_element_by_link_text("新闻")
dr.find_element_by_link_text("hao123")


通过link text定位:

dr.find_element_by_partial_link_text("新")
dr.find_element_by_partial_link_text("hao")
dr.find_element_by_partial_link_text("123")


'''



//////////////////////////////////////////////////////////////



import unittest
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.title)
driver.find_element_by_id("kw").clear() #清楚文本

#尺寸
size = driver.find_element_by_id("kw").size
print(size)

#文本
text = driver.find_element_by_id("kw").text
print(text)

#是否可见
result = driver.find_element_by_css_selector("#kw").is_displayed()
print(result)

driver.find_element_by_id("kw").send_keys("输入内容") #模拟按键输入内容
driver.find_element_by_id("kw").submit()
driver.find_element_by_id("su").click()

driver.set_window_size(200,100) #设置宽高

driver.forward() #前进
driver.back() #后退

driver.refresh() #刷新

driver.quit()




"""
鼠标事件：
在 WebDriver 中， 将这些关于鼠标操作的方法封装在 ActionChains 类提供。

ActionChains 类提供了鼠标操作的常用方法：

perform()： 执行所有 ActionChains 中存储的行为；

context_click()： 右击；

double_click()： 双击；

drag_and_drop()： 拖动；

move_to_element()： 鼠标悬停。

"""

#引入ActionChains类
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
above = driver.find_element_by_link_text("设置")

#对找到的对应元素进行悬停操作
ActionChains(driver).move_to_element(above).perform()
driver.quit()



#键盘事件：


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("seleniumm")

#删除多于一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#追加
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u'教学') #中文字符用unicode模式，或者decode('GBK')模式

#输入框中，文本ctrl +a 全选内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

#输入框中，文本ctrl +x 剪切内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

#输入框中，文本ctrl +x 粘贴内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

#回车代替单击操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
driver.find_element_by_id("kw").send_keys(Keys.F10)
time.sleep(5)

driver.quit()




#获取断言信息：

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

print('Before search================')

# 打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

print('After search================')

# 再次打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

# 获取结果数目
user = driver.find_element_by_class_name('nums').text
print(user)

sleep(5) #如果导入time,则用time.sleep(5)
driver.quit()






#设置元素等待

#显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 1, 0.5).until(
                      EC.presence_of_element_located((By.ID, "kw")), message= '响应时间正常！'
                      )
element.send_keys('selenium')

sleep(3)
driver.quit()

'''
WebDriverWait类是由WebDirver 提供的等待方法。
在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。
具体格式如下：
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

driver ：浏览器驱动。
timeout ：最长超时时间，默认以秒为单位。
poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。


WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。
 * until(method, message=‘’) 调用该方法提供的驱动程序作为一个参数，直到返回值为True。 
 * until_not(method, message=‘’) 调用该方法提供的驱动程序作为一个参数，直到返回值为False。

在本例中，通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在。
'''





'''
隐式等待:
WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0

implicitly_wait()默认参数的单位为秒，本例中设置等待时长为10秒。
首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。其次，它并不针对页面上的某一元素进行等待。
当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。
假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime, sleep

driver = webdriver.Firefox()

# 设置隐式等待为10秒
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()


