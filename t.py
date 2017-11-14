#!/usr/bin/env python
# -*- coding: utf-8 -*-


import linecache
import time
now = time.time() #代码开始时间

# 前期准备，整理数据
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')
#tag对应的index
dkeys={data_keys[k]:k for k in xrange(0,len(data_keys))}

# 获取文件的list
file=linecache.getlines('/Users/captain/desktop/t.txt')
# 文件list的二维矩阵,strip()去掉每行末尾的\n字符,拆分符号
lines=[line[1:-2].split('","') for line in file]


# #1.该文本里，有多少个用户
# print len(set([line[dkeys['username']] for line in lines]))

# #2.该文本里，每一个用户的名字
# print list(set([line[dkeys['username']] for line in lines]))

# # 3.该文本里，有多少个2012年11月发布的tweets
# print ''.join([line[dkeys['created_at']] for line in lines]).count('2012-11')#用count
# # 或者
# ctime= [line[dkeys['created_at']] for line in lines]
# print len(filter(lambda x: x.startswith('2012-11'),ctime))#用startswith
# # 或者
# print len(filter(lambda line:line[dkeys['created_at']].startswith('2012-11'),lines))
# '''
# 答案中=33189，而自己算出来=32846，自带编译器算出为33190
# 自己用的分割方法，保留了字符中的双引号，然后用双引号统计结果为32846，少了很多，而用mac自带的文本编译器，atom,sublime搜索出来都为33190，数目都不一致，很奇怪
# 自用分割为：lines=[line.strip().split(',') for line in file]
# '''

# # 4.该文本里，有哪几天的数据
# user_bydate=[line[dkeys['created_at']].split(' ')[0] for line in lines]
# lines_by_created=sorted(list(set(user_bydate)))
# print lines_by_created

# # 5.该文本里，在哪个小时发布的数据最多
# hours=[int(line[dkeys['created_at']][11:13]) for line in lines]
# hours_count=[(h,hours.count(h)) for h in xrange(24)]
# hours_count.sort(key=lambda x: x[1], reverse=True)
# max_hours=hours_count[0][0]
# print max_hours

# # 6.该文本里，输出在每一天发表tweets最多的用户。
# #引用题目4中的数据
# user_bydate=[line[dkeys['created_at']].split(' ')[0] for line in lines]
# lines_by_created=sorted(list(set(user_bydate)))
# #先定义一个空的嵌套字典
# dateline_by_user = {k:dict() for k in lines_by_created}
# # dateline_user={k:"" for k in lines_by_created}#如果要输出一维字典，+这句
# for line in lines:
# 	dateline=line[dkeys['created_at']].split(' ')[0]
# 	username=line[dkeys['username']]
# 	if dateline_by_user[dateline].has_key(username):#如果嵌套字典中的name不存在的话，初始化1，存在就+1
# 		dateline_by_user[dateline][username] += 1
# 	else:
# 		dateline_by_user[dateline][username] = 1

# for k,v in dateline_by_user.items():#对嵌套的字典的value进行排序，并返回最大value的key
# 	us=v.items()
# 	us.sort(key=lambda k:k[1],reverse=True)
# 	dateline_by_user[k] = {us[0][0]:us[0][1]}#这儿输出的是二维字典
# 	# dateline_user[k]=us[0][0]#如果要输出一维字典，+这句
# print dateline_user

# # 7.请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率
# lines_2012_11_03=filter(lambda line: line[dkeys['created_at']].startswith('2012-11-03'),lines)
# hoursline_2012_11_03={str(i):0 for i in xrange(24)}
# for line in lines_2012_11_03:
# 	hour=line[dkeys['created_at']][11:13]
# 	hoursline_2012_11_03[str(int(hour))]+=1
# print sorted(hoursline_2012_11_03.items(), key=lambda x:int(x[0]))

# 8.统计该文本里，来源的相关信息和次数
