"""
定义判断回文数的函数
"""


# def is_panlindrome(num):
#     return str(num) == str(num)[::-1]


def is_palindrome(num):
    total, temp = 0, num
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10   # temp //= 10
    return total == num


def greet(name):
    print(f'Goodbye, {name}!')


# print(is_palindrome(12321))
# print(is_palindrome(121))
# print(is_palindrome(11))
# print(is_palindrome(123))
