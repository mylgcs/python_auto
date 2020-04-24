# 列表的定义
# list1 = [38,89,3.4,'ok']
# list2 = []  # 空列表
# list3 = list("hello")

# print(list1,type(list1))
# print(list3,type(list3))

# 元素的存取

"""
     -8   -7   -6   -5  -4   -3  -2  -1   从右向左的下标排列顺序： -1,-2,-3
    [10,  20,  30,  40,  50,  60, 70, 80]
      0    1    2   3     4    5   6   7   从左向右下标从0开始，0,1,2,3

# 元素存取的方式：  列表名[下标]
"""
list1 = [10,  20,  30,  40,  50,  60, 70, 80]
# 读取下标为0的元素
# print(list1[0])
# 读取最右边的元素
# print(list1[-1],list1[7])

# 下标不能越界
# print(list1[8])   # IndexError: list index out of range
# len 可以获取列表元素个数
# print(len(list1))

# 修改元素
# list1[0] = 90
# print(list1)

# 遍历 访问（读取或修改）列表的每一个元素；
# 依次访问列表的每一个访问
# 1.通过下标遍历
# for index in range(0,len(list1)):
#     print(list1[index])
# 从右向左
# -1 -9
# for index in range(-1,-len(list1)-1,-2):
#     print(list1[index])
# range(start,end,step)    value = start + i * step  (i=0,1,2)
# index = -1 + 0 * (-1)
# index = -1 + 1 * (-1)  = -2
# index = -1 + 2 * (-1)  = -3
# ...
# index = -1 + 7*(-1) = -8

# 遍历元素： 不能通过value修改列表元素
for value in list1:
    value += 100  # value是变量，不是列表元素，通过value不能修改列表元素
    print(value)
print(list1)

# value = list1[0]
# value = 1900
# print(value,list1[0])
