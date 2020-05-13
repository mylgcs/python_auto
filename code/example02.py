"""
Python中函数的参数非常灵活，如果在设计函数时不知道函数的调用者会传入多少个参数，
可以使用可变参数，可变参数跟普通参数（位置参数）的区别在于参数名前面有一个*，
位置参数和可变参数可以共存，可变参数必须要放到位置参数的后面，否则会造成代码的二义性

设计一个对多个数求和的函数
"""


# 参数名前带*的参数称为可变参数（调用函数时可以传入0个或任意多个参数）
# 传入的参数会组装成一个元组型的变量，type(nums) ---> tuple
def calc(*nums):
    # print(type(nums), nums)
    total = 0
    for num in nums:
        total += num
    return total


print(calc())
print(calc(1))
print(calc(1, 2))
print(calc(1, 2, 3))
print(calc(1, 2, 3, 4, 5))
print(calc(45, 12, 99, 87, 63, 90, 81))
