# while True:
#     print('*')

# break：用来结束整个循环
#continue 用来结束本轮循环，开启下一轮循环

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# while True:
#     answer = input('咱们出对象呗')
#     if answer == '好':
#         break


# continue  结束当前这一次循环 重新判断条件 开启下一次循环

i = 0
sum = 0 #存和
while i < 100:
    i += 1  # i=1   i=3
    if i % 2 == 0:  #
        # i += 1  #表示继续往下走
        continue  #如果是偶数  那么退出这一次 继续下一次的循环 如果continue 后边的循环体不执行

    sum += i  # sum =1
print(sum)



