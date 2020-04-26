#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: 2_列表操作.py
@time: 2020/4/24 8:42 上午
'''
# list1 = [10, 20, 30, 40, 50, 60,50]
# 列表的增加元素
# append在末尾追加一个元素
# list1.append(90)
# list1.append([1,3])

# extend 在列表末尾追加多个元素，参数可以是列表
# list1.extend([80,70])
# list1.extend(100)  # error 'int' object is not iterable

# insert 在任意位置插入元素,原来的元素会往后移
# list1.insert(0,110)

# 删除元素
# pop(i) 删除指定下标的元素, 返回被删除的元素
# res = list1.pop(0)
# res = list1.pop() # 删除末尾元素

# remove 按元素的值删除, 从左向右删除第一个等于指定值的元素
# list1.remove(50)

# clear 清空列表
# list1.clear()

# 切片删除  ,可以删除任何连续的元素
# list1[:2] = []

list1 = [10, 20, 30, 40,30, 50, 60,50]
# 查找
# index 从左向右查找第一个等于指定值的元素的下标
# index(x,start=0,end=len(list))
res = list1.index(30)

# 查找所有值等30的元素的下标
# result = []
# for i in range(len(list1)):
#     if list1[i] == 30:
#         result.append(i)
#
# print(result)
# res = list1.index(30)
# print(res)
# print(list1.index(30,res+1))

# count 找出列表中有多少个值等x的元素
res = list1.count(30)
print(res)
# 从list1中删除值等30的元素全部删除

# 不要在遍历中直接删除元素
# for i in range(len(list1)):
#     list1.pop(i)
# print(list1)

# for value in list1:
#     if value == 30:
#         list1.remove(value)
# print(list1)
# while 30 in list1:
# #     list1.remove(30)
# # print(list1)

# 列表反转
# print(list1)
# list1.reverse()
# print(list1)

# 列表排序
# print(list1)
# # print(type(list1))
# list1.sort() # 从小到大排序
# print(list1)
# # reverse默认等于False 从小到大排序
# # reverse=True从大到小排序
# list1.sort(reverse=True)
# print(list1)

# 二维列表
list1 = [[1,2,3],[4,5,6]]

# 元素访问
# print(list1[0])
# 取元素要用到两个[]
# print(list1[1][0])
for elem in list1:
    for value  in elem:
        print(value)



