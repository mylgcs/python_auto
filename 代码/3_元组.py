#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    不可变的序列，元素不能修改，其他同列表操作一样
@author:  
@contact: 
@file: 3_元组.py
@time: 2020/4/24 9:47 上午
'''

# 1.定义
# t1 = 1,2,3
# t2 = (1,2,3)
# t3 = (1,)  # 只有一个元素的元组，逗号不能省略
# t4 = tuple([2,3,4])
#
# print(type(t1),type(t2),type(t3),type(t4))
# print(t4)

t1 = (10, 20, 30)
# 下标用法和列表相同
# 元素不能修改
# print(t1[0],t1[-1])

# 遍历
# for value in t1:
#     print(value)

# for i in range(len(t1)):
#     print(t1[i])

# 通用操作
# res = (1,2,3) + t1

# * 重复
# res = (0,1)*10
# 元素个数
# res = len(t1)

# 切片
# t1 = (10,20,30,40,50)
# print(t1[:4]) # (10,20,30,40)
# print(t1[1:-1:2])
# 统计函数
# print(sum(t1),max(t1))

# 成员判断，in ,not in
# print(20 in t1)

# 查找
# print(t1.index(20))
# print(t1.count(20))

# 序列解包
# 解包就是把元组的元素赋值给变量
# a, b = (3, 4)
# 3赋值给a，5赋值给b，其余元素赋值给_
# a,*_, b = (3, 6,4, 5)
# print(a,_,b)

# a, b = [2,5]
# print(a,b)

# a,b,*_ = 3,4,9,8,6
# print(a,b,_)
# t1 = 1,2,3,4
# *_,a,b = t1
# print(_,a,b)
# print(t1)

# a, b = 3, 4
# # a,b = (b,a)
# # print(a,b)
t1 = 1,2,3,4
# a,b = t1[:2]
# print(a,b)
a, b = t1[:2],t1[2:]
print(a,b)



