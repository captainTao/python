#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
refer to :
http://www.mamicode.com/info-detail-1224080.html


'''

urllib and urllib2 区别：


# urllib2的优势：
urllib2.urlopen可以接受一个Request对象或者url，（在接受Request对象时候，并以此可以来设置一个URL 的headers）
urllib.urlopen只接收一个url

# urllib2的优势：
urllib 有urlencode,urllib2没有，这也是为什么总是urllib，urllib2常会一起使用的原因


r = Request(url=‘http://www.mysite.com‘)
r.add_header(‘User-Agent‘, ‘awesome fetcher‘)
r.add_data(urllib.urlencode({‘foo‘: ‘bar‘})
response = urllib2.urlopen(r)     #post method



urllib:
'''--------------------------------------'''
>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_asciire', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', '_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', '_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 'addinfo', 'addinfourl', 'always_safe', 'base64', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'noheaders', 'os', 'pathname2url', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 'quote_plus', 're', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test1', 'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 'urlopen', 'urlretrieve']


#1 url.urlopen()

>>> import urllib
>>> f = urllib.urlopen('http://www.google.com.hk/')
print help(f) 
['close', 'code', 'fileno', 'fp', 'getcode', 'geturl', 'headers', 'info', 'next', 'read', 'readline', 'readlines', 'url']
-         read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
-         info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
-         getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
-         geturl()：返回请求的url

# urlencode不能直接处理unicode对象，所以如果是unicode，需要先编码，有unicode转到utf8
urllib.urlencode (u‘bl‘.encode(‘utf-8‘))



import urllib
resp = urllib.urlopen('https://www.baidu.com/')
print resp.getcode(), resp.geturl(), resp.info(), resp.headers, resp.url
# resp.url和resp.geturl()结果一样
# resp.headers和resp.info()结果一样


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



#2. urllib.urlretrieve()
#  urlretrieve多数适用单纯的只下载的功能或者显示下载的进度等
import urllib
f=urllib.urlretrieve('http://www.baidu.com/',filename='/Users/captain/desktop/baidu.html')






urllib2:
# 提供一些复杂的接口用于处理： 基本认证，重定向，Cookies等
'''--------------------------------------'''
>>> import urllib2
>>> dir(urllib2)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'FTPHandler', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPRedirectHandler', 'HTTPSHandler', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'StringIO', 'URLError', 'UnknownHandler', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_cut_port_re', '_have_ssl', '_opener', '_parse_proxy', '_safe_gethostbyname', 'addinfourl', 'base64', 'bisect', 'build_opener', 'ftpwrapper', 'getproxies', 'hashlib', 'httplib', 'install_opener', 'localhost', 'mimetools', 'os', 'parse_http_list', 'parse_keqv_list', 'posixpath', 'proxy_bypass', 'quote', 'random', 'randombytes', 're', 'request_host', 'socket', 'splitattr', 'splithost', 'splitpasswd', 'splitport', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'sys', 'time', 'toBytes', 'unquote', 'unwrap', 'url2pathname', 'urlopen', 'urlparse', 'warnings']


#1 
urllib2.urlopen(url[, data][, timeout])
# 可选的参数timeout，阻塞操作以秒为单位，如尝试连接（如果没 有指定，将使用设置的全局默认timeout值）。实际上这仅适用于HTTP，HTTPS和FTP连接。

import urllib
import urllib2
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord','location‘': 'Northampton', 'language': 'Python' }
data = urllib.urlencode(values)      
req = urllib2.Request(url, data)   #send post
response = urllib2.urlopen(req)
page = response.read()







# https://blog.csdn.net/dolphin_h/article/details/45296353

#get方法：

# 百度是通过http://www.baidu.com/s?wd=XXX 来进行查询的，这样我们需要将{‘wd’:’xxx’}这个字典进行urlencode
#coding:utf-8  
import urllib   
import urllib2    
url = 'http://www.baidu.com/s'   
values = {'wd':'D_in'}     
data = urllib.urlencode(values)  
print data   
url2 = url+'?'+data  
response = urllib2.urlopen(url2)    
the_page = response.read()   
print the_page  


#post方法：

import urllib  
import urllib2  
url = 'http://www.someserver.com/cgi-bin/register.cgi'  
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' #将user_agent写入头信息  
values = {'name' : 'who','password':'123456'}      #post数据  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)                   #对post数据进行url编码  
req = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(req)  
the_page = response.read()  


#urllib2带cookie的使用

#coding:utf-8  
import urllib2,urllib  
import cookielib    
url = r'http://www.renren.com/ajaxLogin'  #r代表只读
   
#创建一个cj的cookie的容器  
cj = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
#将要POST出去的数据进行编码  
data = urllib.urlencode({"email":email,"password":password})  
r = opener.open(url,data)  
print cj  





#get
import urllib
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

# 传入的参数为None:
import urllib
import urllib2

url = 'https://www.baidu.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'}
request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
print response.read()




httplib简单用法:
#---------------------------------------#
#!/usr/bin/env python      
# -*- coding: utf-8 -*-      
import httplib    
import urllib    
    
def sendhttp():    
    data = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})       
    headers = {"Content-type": "application/x-www-form-urlencoded",    
               "Accept": "text/plain"}    
    conn = httplib.HTTPConnection('bugs.python.org')    
    conn.request('POST', '/', data, headers)    
    httpres = conn.getresponse()    
    print httpres.status    
    print httpres.reason    
    print httpres.read()               
                  
if __name__ == '__main__':      
    sendhttp()  





urlib保存返回的文件：
'''
过程：
1、加载模块urllib,beautifulsoup。urllib提供网络服务解析，beautifullsoup提供对网页结构进行解析的功能。
2、加载网页
3、用beautifulsoup加载解析
'''


import urllib.request   
from bs4 import BeautifulSoup
url="http://google.cn/"  
response=urllib.request.urlopen(url)    #返回文件对象
page=response.read()  
#直接将URL保存为本地文件：


import urllib.request  
url="http://www.xxxx.com/1.jpg"
urllib.request.urlretrieve(url,r"d:\temp\1.jpg")
#当然你可以将返回的对象交给soup处理
soup=BeautifulSoup(response)
#运行soup


'''
保存文件
'''
def save_url_file(url, filepath):
    import urllib, urllib2
    response = urllib.urlopen(url)
    with open(filepath, 'w') as f:
        f.write(response.read())
url = 'https://movie.douban.com/'
filepath = '/Users/captain/desktop/beautfulSoup.html'
save_url_file(url, filepath)
