
#如果循环条件不具备，循环正常结束 会执行else 语句块
#如果循环的过程中break 退出了 则不走else

#大于1的自然数
# num = int(input("请输入一个整数:"))
# i = 2
# while i < num:
#
#     if num % i == 0: # 除尽了,不是素数
#         break  #break 退出所有循环   不执行else
#     i += 1   # 1 和 本身 之外没有别的除数了 这才是素数
#     #从2开始
#
#
#     #检查从2到它本身 是否有别的除数  如果有 这个数就不是素数
#
# else:
#     print("是素数")


# #计算1-100的和
sum = 0

i = 1
while i<= 100:
    sum += i
    i+=1
print(sum,i) # 5050 101

# sum = 0
# i = 1
# if i<=100:  #这里满足条件执行下面的代码块  就不会再回来判断是否满足条件
#     sum += i
#     i+=1
# print(sum,i) # 1 2
#
#
# sum = 0
# i = 1
# while i<=100:  #这里满足条件执行下面的代码块  回来还会判断一次是否满足条件
#     sum += i
#     i+=1
# print(sum,i) # 1 2


while True:
    print("泽宇老弟")


