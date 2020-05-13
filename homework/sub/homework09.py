"""
定义判断素数的函数
"""


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num != 1


def greet(name):
    print(f'Hello, {name}!')


# 打印1-99之间的素数
# for n in range(1, 100):
#     if is_prime(n):
#         print(n, end=' ')
