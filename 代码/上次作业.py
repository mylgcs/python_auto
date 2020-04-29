#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: 上次作业.py
@time: 2020/4/24 11:41 下午
'''
from random import randint

"""
1.不使用列表的index函数，自己写程序查找指定元素
要查找的元素从键盘输入
默认从左向右查找，找到第一个元素就停止
"""
# list1 = [20,34,12,67,45,90]
# num = eval(input("请输入要查找的数："))
# for i in range(len(list1)):
#     if list1[i] == num:
#         print("找到了，下标为："+str(i))
#         break
# else:
#     print("没有该元素")

"""
2.自定义一个数字列表，求列表中所有偶数元素的和
"""
# list1 = [51, 43, 88, 67, 94, 72, 90, 97, 99, 77]
# total = 0
# for value in list1:
#     if value % 2 == 0:
#         total += value
# print(total)

"""
3.B哥去参加青年歌手大奖赛,有10个评委打分，去掉一个最高一个最低，求平均分
"""
# list1 = [51, 43, 88, 67, 94, 72, 90, 97, 99, 77]
# print("平均分为：",(sum(list1)-max(list1)-min(list1))/(len(list1)-2))

"""
4.给定一个列表：将列表中指定的某个元素全部删除
"""
# list1 = [51, 43, 88, 67, 94, 72, 43, 97, 99, 77]
# num = eval(input("请输入要删除的数："))
# while num in list1:
# #     list1.remove(num)
# 也可以
# for i in range(len(list1)-1,-1,-1):
#     if list1[i] == num:
#         list1.pop(i)

""""
5.输入某年某月某日，判断这一天是这一年的第几天
   - 要考虑闰年
"""
# month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# while 1:
#     year,month,day = eval(input("请输入年月日，以逗号隔开："))
#     if month <1 or month > 12 or day < 1 or day > month_days[month]:
#         print("你输入的日期不合理，请重新输入")
#     else:
#         break
# leap = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and month > 2
# totals = sum(month_days[:month]) + day + leap
# print(totals)

"""
6.生成50-300之间可重复的 10个数据 存放于列表中, 保证列表中元素的顺序，对列表进行排重,并对列表使用排序算法进行降序排序

"""
# list1 = []
# for i in range(10):
#     list1.append(randint(50,300))
# list1.sort(reverse=True)
# print(list1)

"""
7.已知一个数字列表，获取列表中出现次数最多的元素
例如：nums = [1, 2, 3,1, 4, 2, 1 ,3, 7, 3, 3]   ->  打印: 3 
 """
# nums = [1, 2, 3,1, 4, 2, 1 ,3, 7, 3, 3]
# index = 0  # 记录次数最多元素的下标
# max1 = nums.count(nums[index]) # 最多次数
# for i in range(len(nums)):
#     if nums.count(nums[i]) > max1:
#         index = i   # 记录当前元素的下标
#         max1 = nums.count(nums[i])
# print(nums[index])

"""
8.已知一个列表中保存的全是学生的姓名，要求去掉重复的名字 例如：
names = ['张三', '李四', '大黄', '张三']  -> 
names = ['张三', '李四', '大黄']  
"""
# names = ['张三', '李四', '大黄', '张三']
# result = []
# for value in names:
#     if value not in result:
#         result.append(value)
# print(result)