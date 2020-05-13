
"""
定义求最大公约数的函数
"""


# def gcd(x, y):
#     if x > y:
#         x, y = y, x
#     for i in range(x, 0, -1):
#         if x % i == 0 and y % i == 0:
#             return i


def gcd(*, x, y):
    while y % x != 0:
        x, y = y % x, x
    return x


# 27 15 ---> 15 27 ---> 12 15 ---> 3 12 ---> 3
print(gcd(y=27, x=15))
# 14 15 ---> 1 14 ---> 1
print(gcd(x=14, y=15))
# 12 60 ---> 12
print(gcd(y=12, x=60))
