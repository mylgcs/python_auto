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
num = int(input("输入一个数："))
i = 10
count = 1
while num != 0:
    num //= i
    if num > 0:
        count += 1
print(count)

