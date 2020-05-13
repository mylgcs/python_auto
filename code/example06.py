"""
函数的递归调用 - 一个函数直接或间接的调用自身
1. 收敛条件 - 什么时候停止递归
2. 递归公式 - 找到递归公式才能使用递归
定义求阶乘的函数，阶乘的定义：N! = N * (N - 1)!
"""


def fac(n):
    if n in (0, 1):
        return 1
    return n * fac(n - 1)


# 5 * fac(4)
# 5 * 4 * fac(3)
# 5 * 4 * 3 * fac(2)
# 5 * 4 * 3 * 2 * fac(1)
# 5 * 4 * 3 * 2 * 1 * 1
#print(fac('hello'))


# 求0-9的阶乘
for n in range(10):
    print(f'{n}: {fac(n)}')
