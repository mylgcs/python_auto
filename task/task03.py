# 一个小孩爬楼梯，每次可以爬1个、2个或3个台阶，编程求出这个小孩爬完10个台阶的楼梯一共有多少种走法。

def fac(n):
    if n in (0,1):
        return 1
    return n * fac(n - 1)

for n in range(10):
    print(f'{n}: {fac(n)}')