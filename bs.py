#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bs4
from bs4 import BeautifulSoup

html = """
<html><head><title>The title: Dormouse's story</title></head>
<meta charset='utf-8'>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/hhahhah" class="sister" id="link1">
		<ul>
			<li>咖啡</li>
			<li>茶</li>
			<li>牛奶</li>
		</ul>
	</a>
	<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie比如这个内容，中文字符测试</a>
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
	and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html, 'lxml')

for i in soup.a.striped_contents:
	print i.strip()
