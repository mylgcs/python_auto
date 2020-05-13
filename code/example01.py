"""
每个Python文件就是一个模块（module），模块可以管理函数，同名的函数可以放到不同的模块下
每个文件夹就是一个包（package），包可以管理模块，同名的模块可以放到不同的包下
每个Python包中通常都有一个__init__.py文件，使用模块和包可以解决程序中命名冲突的问题

导入包和模块的语法：
# from 模块 import 函数 [as 别名]
from random import sample
print(sample('abcdefg', 3))

# import 模块 [as 别名]
import random
print(random.sample('abcdefg', 3))

# from 包[.子包] import 模块 [as 别名]
from homework.sub import homework09
from homework.sub import homework10
homework09.greet('骆昊')
homework10.greet('骆昊')

# from 包[.子包].模块 import 函数 [as 别名]
from homework.sub.homework09 import greet as say_hello
from homework.sub.homework10 import greet as say_goodbye

say_hello('骆昊')
say_goodbye('骆昊')

说明：不推荐使用 from ... import * 这样的语法！用什么就导入什么更好！
"""
# from homework.sub import homework09 as h09
# from homework.sub import homework10 as h10
from homework.sub.homework09 import is_prime, greet as say_hello
from homework.sub.homework10 import is_palindrome, greet as say_goodbye


def is_palindromic_prime(num):
    """判断一个数是不是回文素数"""
    return is_prime(num) and is_palindrome(num)


say_hello('骆昊')
say_goodbye('骆昊')

print(is_palindromic_prime(12321))
print(is_palindromic_prime(121))
print(is_palindromic_prime(97))
print(is_palindromic_prime(11))
