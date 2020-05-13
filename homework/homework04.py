"""
一个小孩爬楼梯，每次可以爬1个、2个或3个台阶，
编程求出这个小孩爬完10个台阶的楼梯一共有多少种走法。
"""
from functools import lru_cache


# f(n) = f(n - 1) + f(n - 2) + f(n - 3)
# f(10) = f(9) + f(8) + f(7)
# f(10) = [f(8) + f(7) + f(6)] + [f(7) + f(6) + f(5)] + [f(6) + f(5) + f(4)]
@lru_cache()
def go_upstairs(num):
    if num == 0:
        return 1
    if num < 0:
        return 0
    return go_upstairs(num - 1) + go_upstairs(num - 2) + go_upstairs(num - 3)


for n in range(1, 101):
    print(f'{n}: {go_upstairs(n)}')
