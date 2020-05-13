# 完美数的函数

def is_perfect(num):
    total = 1
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            total += factor
            factor2 = num // factor
            if factor != factor2:
                total += 2
    return total == num
