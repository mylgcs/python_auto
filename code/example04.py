"""
Lambda函数 - 只有一行代码而且没有名字的函数（匿名函数）
Lambda函数就是把一个简单函数写成表达式的形式

处理数据：过滤（filter） ---> 映射（map） ---> 归约（reduce）

Python中的函数的参数可以用*进行分隔，
*前面的参数称为位置参数，调用函数传入参数时只需要对号入座即可
*后面的参数称为命名关键字参数，调用函数传入参数时必须写成"参数名=参数值"的形式
"""
# from random import sample, choices
#
# print(sample('0123456789', 6))
# print(choices('0123456789', k=6))
#
# fruits = ['banana', 'grape', 'pear', 'zoo', 'watermelon']
# fruits2 = sorted(fruits, key=len, reverse=True)
# print(fruits2)
#
# nums = [1, 27, 2, 36, 88, 5, 100, 47, 31]
# nums.sort(key=str)
# print(nums)
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))))
# print([num ** 2 for num in nums if num % 2 == 0])


def calc(init_value, fn, *nums):
    result = init_value
    for num in nums:
        result = fn(result, num)
    return result


add = lambda x, y: x + y
mul = lambda x, y: x * y


print(calc(0, add, 1, 2))
print(calc(0, lambda x, y: x + y, 1, 2, 3))
print(calc(1, mul, 1, 2, 3, 4, 5))
print(calc(1, lambda x, y: x * y, 45, 12, 99, 87, 63, 90, 81))
