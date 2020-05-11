# 写一个函数，传入两个正整数，返回两个数的最大公约数。

def gcd(x,y):
    while y % x != 0:
        x,y = y % x,x
    return x
print(gcd(x=8,y=97))