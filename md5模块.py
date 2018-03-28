#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
refer to:
https://blog.csdn.net/u013943420/article/details/75727894

'''

# python两种生成md5的方法
一. 使用md5包

import md5

src = 'this is a md5 test.'   
m1 = md5.new()   
m1.update(src)   
print m1.hexdigest()   



二. 使用hashlib

import hashlib   

m2 = hashlib.md5()   
m2.update(src)   
print m2.hexdigest()   
推荐使用第二种方法。


///////////////////////////////////////////////////////////////////////////////////

#python 2.7
import md5    
m = md5.new()    
m.update("Nobody inspects the spammish repetition")    
md5value=m.hexdigest()  
print md5value
print len(md5value) # 32


import md5
src = 'this is a md5 test.'
m1 = md5.new()
m1.update(src.encode(encoding='utf-8')) #如果遇到中文字符需要encoding
print(m1.hexdigest())



# python3.x已经把md5 module移除了。要想用md5得用hashlib module,

import hashlib  
m = hashlib.md5()  
#参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误  
m.update(b"password")  
psw = m.hexdigest()  
print(psw)  
''''' 
中文字符在Python中是以unicode存在的,同一个字符串在不同的编码体系下有不同的值,所以在hash前要进行编码， 
个人建议转为gb2312,因为对比发现，我下载的一个工具算出的md5值是与gb2312编码后算出的md5值一样。 
（！网上md5的工具很多，是不是所有的md5工具都是这样的，未去考证，有兴趣的可以研究一下） 
'''  
# import hashlib    
data='我是'    
m = hashlib.md5(data.encode(encoding='gb2312'))    
print(m.hexdigest()) 



import hashlib
# 待加密信息
str = 'this is a md5 test.'

# 创建md5对象
hl = hashlib.md5()
# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))   #这儿转换为utf-8
print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())


///////////////////////////////////////////////////////////////////////////////////


'''
refer to:
https://blog.csdn.net/u013943420/article/details/75727894

'''

0e开头的MD5字符串python脚本生成代码:

# -*- coding: utf8 -*-
import hashlib

payload = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#payload = "qwertyuiopasdfghjklzxcvbnm"
# payload = "0123456789"

def calcMd5(s):
	MD5 = hashlib.md5(s.encode()).hexdigest()
	if MD5[0:2] == "0e" and MD5[2:32].isdigit():
		print(s,MD5)

def getStr(payload,s,slen):
	if len(s) == slen:
		#Custom string
		calcMd5(s)
		return s	
	for j in range(len(payload)):
		sl= s+payload[j]
		getStr(payload,sl,slen)


if __name__ == '__main__':
	getStr(payload,'',9)