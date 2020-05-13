# 练习3：写一个函数，实现对传入的整数进行质因子分解的操作，返回所有质因子的列表。

def list_prime_factors(num):
    factors, factor = [], 2
    while num > 1:
        if num % factor == 0:
            factors.append(factor)
            num //= factor
        else:
            factor += 1
    return factors


print(list_prime_factors(255))
