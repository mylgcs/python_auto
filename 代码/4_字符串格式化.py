#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: 4_字符串格式化.py
@time: 2020/4/26 9:41 上午
'''
# % 占位符
"""
%d 整数
%f 实数
%s 字符串
"""
# res = "我叫%s,今年%d岁了，我有%f钱" % ('tom',21,3455.5)
# print(res)

# format格式化方法
# res = "我叫{},今年{}岁了，我有{}钱".format('tom',21,3455.5)
# res = "我叫{:>10},今年{:03}岁了，我有{:<10.2f}钱".format('tom',21,3455.5)
# print(res)
a = 10
print(f"{a}")  # 3.7之后的简洁占位符