"""
一个小孩爬楼梯，每次可以爬一个丶2个或3个台阶
编程求出这个小孩爬完10个台阶的楼梯一共有多少种走法。
"""
from functools import lru_cache

@lru_cache()
def go_upstairs(num):
    if num == 0:
        return 1
    if num < 0:
        return 0
    return go_upstairs(num - 1) + go_upstairs(num - 2) + go_upstairs(num - 3)

for n in range(1,101):
     print(f'{n}:{go_upstairs(n)}')
#print(go_upstairs(10))