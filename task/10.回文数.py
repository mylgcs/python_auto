#  练习10：写一个函数，判断传入的正整数是不是回文数，返回布尔值。
# 说明：12321是一个回文数，因为从左向右和从右向左读，结果是一样的。

def is_palindrome(num):
    total,temp = 0,num
    while temp > 0:
        total *= 10
        total += temp%10
        temp //= 10
    return num == total

print(is_palindrome(121))