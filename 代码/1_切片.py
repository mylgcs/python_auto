#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: 1_切片.py
@time: 2020/4/24 8:16 上午
'''
# list1 = [1,2,3,4,5,6,7,8,9]
# 切片: 获取一个子列表
"""
[start:end:step]
获取下标从start开始到end结束中间的元素，会产生一个新的列表
step：步长，默认值是1；如果大于0，从左向右取；
                    如果小于0，从右向左取

"""
list1 = [1,2,3,4,5,6,7,8,9]
# print(list1[0:5])   # [1, 2, 3, 4, 5]
# print(list1[0:5:2])  # [1, 3, 5]
# print(list1[:5:2])  # [1, 3, 5]
# print(list1[5:])
# print(list1[5:90])
# list2 = list1[:]  # 获取一个源列表的副本
# print(id(list1),id(list2))
# print(list1[2:7:3]) #[3, 6]
# print(list1[2:-3])
# print(list1[-6:5])
# print(list1[-6:2])

# 从右向左切
# print(list1[6:1:-1]) #[7, 6, 5, 4, 3]
# print(list1[6:1:-2]) #[7, 5, 3]
# print(list1[::-1])
# print(list1[1:6:-1])

