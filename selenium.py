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





'''
//////////////////////////////////////////////////////////////
'''

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

driver.find_element_by_id("kw").send_keys(u"输入内容") #模拟按键输入内容
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
frame/iframe
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






'''
文件上传：

对于通过input标签实现的上传功能，可以将其看作是一个输入框，即通过send_keys()指定本地文件路径的方式实现文件上传。

创建upfile.html文件，代码如下：

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <link href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" />
    <title>test upload_file</title>
</head>
<body>
  <div class="row-fluid">
    <div class="span6 well">
    <h3>upload_file</h3>

      <input type="file" name="file" />
      <input type="text" name="text" id="mycolor" value="选择文件..."  style="color: gray; font-size: 10px; font-style: italic; width: 300px;" />
    </div>
  </div>
</body>
<script src="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.js"></script>
</html>


接下来通过send_keys()方法来实现文件上传。
'''



from selenium import webdriver
# import os
from time import sleep
driver = webdriver.Chrome()
# file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get("file:///Users/captain/Desktop/test.html")

# 定位上传按钮，添加本地文件
# driver.find_element_by_name("file").click()  #如果选择文件的弹窗，怎么切换到弹窗呢？？alert方法查找不到元素
driver.find_element_by_name("file").send_keys('/Users/captain/desktop/100.txt') 
#上传文件只能用send_keys()，如果用click(),会设计到操作系统层面，找不到元素
# driver.find_element_by_name("file").send_keys('/Users/captain/desktop/00')
sleep(3)
driver.quit()





'''
cookie操作:

有时候我们需要验证浏览器中cookie是否正确，因为基于真实cookie的测试是无法通过白盒和集成测试进行的。
WebDriver提供了操作Cookie的相关方法，可以读取、添加和删除cookie信息。

WebDriver操作cookie的方法：

get_cookies()： 获得所有cookie信息。

get_cookie(name)： 返回字典的key为“name”的cookie信息。

add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

delete_all_cookies()： 删除所有cookie信息。

下面通过get_cookies()来获取当前浏览器的cookie信息。
'''


# 下面通过get_cookies()来获取当前浏览器的cookie信息。

from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie= driver.get_cookies()
# 将获得cookie的信息打印
print(cookie)
sleep(3)

driver.quit()


'''
从执行结果可以看出，cookie数据是以字典的形式进行存放的。知道了cookie的存放形式，接下来我们就可以按照这种形式向浏览器中写入cookie信息。
'''

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 向cookie的name 和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()

'''
输出结果：
======================== RESTART: =========================
YOUDAO_MOBILE_ACCESS_TYPE -> 1
_PREF_ANONYUSER__MYTH -> aGFzbG9nZ2VkPXRydWU=
OUTFOX_SEARCH_USER_ID -> -1046383847@218.17.158.115
JSESSIONID -> abc7qSE_SBGsVgnVLBvcu
key-aaaaaaa -> value-bbbbbb
从执行结果可以看到，最后一条cookie信息是在脚本执行过程中通过add_cookie()方法添加的。
通过遍历得到所有的cookie信息，从而找到key为“name”和“value”的特定cookie的value。

'''





'''

调用JavaScript代码:

虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。
在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了execute_script()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：

window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。
方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。
<!-- window.scrollTo(左边距,上边距); -->
window.scrollTo(0,450);
'''


from selenium import webdriver
from time import sleep

# 访问百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# 设置浏览器窗口大小
driver.set_window_size(500, 500)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)  #之行js内容
sleep(3)

driver.quit()



'''
截图：
自动化用例是由程序去执行的，因此有时候打印的错误信息并不十分明确。
如果在脚本执行出错的时候能对当前窗口截图保存，那么通过图片就可以非常直观地看出出错的原因。
WebDriver提供了截图函数
get_screenshot_as_file()来截取当前窗口。

'''


from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的保存位置
# driver.get_screenshot_as_file("D:\\baidu_img.jpg")
driver.get_screenshot_as_file("/Users/captain/desktop/baidu_img.jpg")
driver.quit()


# 脚本运行完成后打开D盘，就可以找到baidu_img.jpg图片文件了。



'''
关闭：
在前面的例子中我们一直使用quit()方法，其含义为退出相关的驱动程序和关闭所有窗口。
除此之外，WebDriver还提供了close()方法，用来关闭当前窗口。
例多窗口的处理，在用例执行的过程中打开了多个窗口，我们想要关闭其中的某个窗口，这时就要用到close()方法进行关闭了。

close() 关闭单个窗口

quit() 关闭所有窗口
'''




