# 1 判断数数
#   7  从2到7-1  每一个数都被7整除，如果都除不尽就是素数，否则只要有一个除尽了就不是素数
#     %  模运算   判断是否整除  7 % 2 == 0   7 // 3

# 2 从101-200打印数数


#判断素数
# n = 11
# i = 2
# while i < n:
#     if n % i == 0:  # 除尽了，不是素数
#         break
#     i += 1
# else:
#     print("%d是素数"%n)
# n = 101
# total = 0  # 统计个数
# while n <= 200:
#     # 判断一个数是不是素数
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         total += 1
#         print(n,end=' ')
#     n += 1
# total = 0
# for n in range(101,201):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         total += 1
#         print(n,end=' ')
# print("\n共有%d个素数"%total)

# 判断水仙花数
# 一个三位数，每一个数字的立方和等于这个数本身
# n = 153
# 个位  n % 10
# 十位  n // 10 % 10
# 百位  n // 100

# for n in range(100,1000):
#     if (n % 10) ** 3 + (n//10%10) ** 3 + (n//100) ** 3 == n:
#         print(n)
# 343
# n = eval(input("请输入一个整数："))
# total = 0
# while n:
#     n //= 10
#     total += 1
#
# print(total)