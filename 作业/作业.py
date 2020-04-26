# list1 = [1,2,3,4,5,6,7,8,9,10]
# a = int(input('请输入要查找的元素：'))
#
# if a in list1:
#     print('查找的元素存在')
# else:
#     print('查找的元素不存在')
# list1 =
# a = 0
# for i in list1:
#     if i % 2 == 0:
#         a += i
# print(a)
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1.remove(max(list1))
# list1.remove(min(list1))
# a = sum(list1)
# print(a/8)
# list1 = [1, 1, 3, 1, 5, 1, 7, 8, 9, 10]
# nums =  [1, 1, 1, 2, 3, 4, 8]
# for num in nums[:]:
# 	if num == 1:
# 		nums.remove(1)
# print(nums)
# year, month, day = eval(input("请输入年月日，用逗号隔开:"))
# runnian = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# pinnian = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     days = sum(runnian[:month - 1]) + day
# else:
#     days = sum(pinnian[:month - 1]) + day
# print("这是第%d天" % (days))

# import random
# list1=[]
# for i in range(1,11):
#     list1.append(random.randint(50,300))
# print(list1)
#
# newList1=[]
# for i in list1:
#     if i not in newList1:
#         newList1.append(i)
# print(newList1)
#
# for i in range(0,len(newList1)-1):
#     for j in range(0,len(newList1)-1-i):
#         if newList1[j] < newList1[j+1]:
#             newList1[j],newList1[j+1]=newList1[j+1],newList1[j]
# print(newList1)
# x = eval(input())
# print(type(x))
# num = True
# nums = [1, 2, 3,1, 4, 2, 1 ,3, 7, 3, 3]
# index = 0 # 记录次数最多元素的下标
# max1 = nums.count(nums[index]) #记录最多次数
# for i in range(len(nums)):
#     if nums.count(nums[i]) > max1:
#         index = i
#         max1 = nums.count(nums[i])
# print(nums[index])

# names = ['张三', '李四', '大黄', '张三']
# reult = []
# for value in names:
#     if value not in reult:
#         reult.append(value)
# print(reult)