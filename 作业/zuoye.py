num = 0
# for i in range(1,101):
#     num += i
# print(num)
# while num < 100:
#     num += 1
# print(num)
# i = 0
# while i < 100:
#   i += 1
#   if i%10 == 2 and i%3==0:
#     print(i)
# num = int(input("请输入一个正整数："))
# count = 0
# while True:
#     count += 1
#     print(num % 10, end='  ')
#     num //= 10
#     if num == 0:
#         break
# print("位数为", count)
# num = int(input('请输入整数:'))
# while True:
#     num = int(input('请输入整数:'))
#     if num == 0:
#         break
# count = 0
# for x in range(101, 200):
#     for n in range(2, x):
#         if x % n == 0:
#             break
#     else:
#         print("素数：", x)
#         count += 1
# print('素数有：',count,'个')
# num = int(input("输入一个数："))
# i = 10
# count = 1
# while num != 0:
#     num //= i
#     if num > 0:
#         count += 1
# print(count)
# len1=3000;
# d=0
# while len1 >= 5:
#     d += 1
#     len1=len1>>1;
# print(d,"天后，绳子小于五米，长为：",len1)
for i in range(100, 1000):
# 使用取模，分别取出百位数、10位数、个位数
# k = i // 10 % 10,需要注意运算符号和运算顺序，不能写为k=i//10%10
    j = i // 100
    k = i // 10 % 10
    l = i % 10
    if i == j ** 3 + k ** 3 + l ** 3:
        print(i)
