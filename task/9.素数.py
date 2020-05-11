# 写一个函数，判断传入的正整数是不是素数，返回布尔值。

def is_prime(num):
    for facter in range(2, int(num ** 0.5) + 1):
        if num % facter == 0:
            return False
    return num != 1
print(is_prime(66))