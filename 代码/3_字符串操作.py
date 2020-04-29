#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: 3_字符串操作.py
@time: 2020/4/26 8:54 上午
'''
# str1 = 'a fox jumped over the ox fence'

# 字符串操作一般都是从左向右找，下标默认都是大于等于0

# 从左向右找，找到第一个相等的子串结束，返回子串第一个的下标
# 如果没有相等的子串，则返回-1
# res = str1.find('ox11')
# print(res)
# 求子串个数
# num = str1.count("o")
# print(num)

# 字符串替换  产生新串
# res = str1.replace('ox','mm',1)
# print(res)
# print(str1)

# 字符串的分割和组合
# 以指定分隔符分割字符串，返回一个列表
# str1 = 'a fox jumped  over the ox fence'
# res = str1.split(' ')
# print(res)

# list1 = ['I','am','a','student']
# # '分隔符'.join(列表) 列表元素必须是字符串
# res = ' '.join(list1)
# print(res)

# s2="""
# 1111
# 2222
# 3333
# """
# res = s2.splitlines()
# print(res)




str1 = 'afox你'
# 字符串判断 python支持utf8，汉字也算字母
# print(str1.isalpha())

# 字符串是否由数字构成
# print("12223".isnumeric())
# print("12223".isdigit())
# print("12223".isdecimal())

# isdigit可以判断字节字符串
# print(b"12223".isdigit())

# 可以检测汉字的一，壹
# print("壹".isnumeric())

# 以...开头
# print("http://www.baidu.com".startswith("http"))

# 字符串转换
print("sdkkLKKdfjdf".lower())
print("sdkkLKKdfjdf".upper())
print("sdkkLKKdfjdf".swapcase())

s1 = "   dsddd      "
# print(len(s1))
# print(len(s1.lstrip()))
# print(len(s1.rstrip()))
# print(len(s1.strip()))

# 字符转utf8的编码 utf8的编码转字符
print(ord("中"))   #字符转utf8的编码
print(chr(20013)) #utf8的编码转字符




