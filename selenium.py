#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 
有时候我们定位不到元素还有其它的原因，下面说明几种：  
1.Frame/Iframe原因定位不到元素： 
2.Xpath描述错误原因：
解决办法：编写好Xpath路径，chrome的F12-&gt;html，ctrl+F进行查找，看是否能查找到。
3.页面还没有加载出来，就对页面上的元素进行的操作： 解决办法：导入time模块设置等待时间。 
4.动态id定位不到元素
解决办法：如果是动态的id，最好不要使用，转而使用xpath或其它方式定位 
5.二次定位，如弹出框登录 解决办法：先定位到弹出框，再定位到弹出框内的元素。
6.不可见元素定位 [emoji:00a0] [emoji:00a0] [emoji:00a0]如上百度登录代码，通过名称为tj_login查找的登录元素，
有些是不可见的，所以加一个循环判断，找到可见元素（is_displayed()）点击登录即可。 

'''


selenium定位方法
http://www.testclass.net/selenium_python/find-element/

组元素就是在element变成elements就ok了；

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






//////////////////////////////////////////////////////////////


#常用方法：
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



# 组元素就是在element变成elements就ok了；


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')

# 循环遍历出每一条搜索结果的标题
for t in texts:
    print(t.text)

driver.quit()



'''
多表单切换：
在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，
WebDriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。
这时就需要通过switch_to.frame()方法将当前定位的主体切换为frame/iframe表单的内嵌页面中

'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.126.com")
sleep(3)

# switch_to.frame() 默认可以直接取表单的id 或name属性。
# 如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("dologin").click()

# 可以通过switch_to.default_content()跳回最外层的页面
driver.switch_to.default_content()
sleep(3)

driver.quit()





'''
新窗口切换：
WebDriver提供了switch_to.window()方法，可以实现在不同的窗口之间切换。

在本例中所涉及的新方法如下：
current_window_handle：获得当前窗口句柄。
window_handles：返回所有窗口的句柄到当前会话。
switch_to.window()：用于切换到相应的窗口，与上一节的switch_to.frame()类似，前者用于不同窗口的切换，后者用于不同表单之间的切换。
'''


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('okusername111')
        driver.find_element_by_name("phone").send_keys('13456786540')
        # driver.find_element_by_name('password').send_keys('kusernameK@111')
        # driver.find_element_by_name('verifyCode').send_keys('3432')
        driver.find_element('注册').click()
        time.sleep(2)
        # ……

driver.quit()




'''
警告框处理：

在WebDriver中处理JavaScript所生成的alert、confirm以及prompt十分简单，
具体做法是使用 switch_to.alert() 方法定位到 alert/confirm/prompt，然后使用text/accept/dismiss/ send_keys等方法进行操作。

text：返回 alert/confirm/prompt 中的文字信息。

accept()：接受现有警告框。

dismiss()：解散现有警告框。

send_keys(keysToSend)：发送文本至警告框。keysToSend：将文本发送至警告框。

'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)  #前面有隐式等待，为什么需要这需要加延时？

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()

driver.quit()




'''
下拉框选择：
Select类用于定位select标签。 select_by_value() 方法用于定位下接选项中的value值。

'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

# 鼠标悬停至“设置”链接
driver.find_element_by_link_text('设置').click()
sleep(2)

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('50')  # 显示50条
sleep(2)
# ……

driver.quit()
