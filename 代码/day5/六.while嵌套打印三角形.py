#
# i = 0
# while i < 5:
#     i += 1
#     print('*'*i)

# 外边的while 控制的是行数 内循环控制列数

# x = 0
#
# while x < 9:    #这个while控制行数
#     x += 1    #x = 1
#     y = 0
#     while y < x:
#         y += 1
#         print("*",end='  ')
#     print()


# 1 x= 0  x<9  x=1     y=0  y<x  y<1   打印*  end后面 ' '  y=1  判断 y<x 不满足条件
#第一行打印结束

# x=1 1<9  x=2       y=0 y<x  y<2  打印*  end后面' '   y=1  继续判断 y<x  1<2 满足 继续打印 *
#第二行打印两个** 结束


# 第三行 打印是三个*

# 1行 1个* 打印完第一行再打印第二行


# 九九乘法口诀表

# 1*1=1
# 2*1=2 2*2=4
#
# x = 1
#
# while x <= 9:
#     y=1
#     while y<=x:
#         print("%d*%d=%d"%(y,x,y*x),end='  ')
#         y+=1
#     print()  #换行
#     x+=1


# x = 0
#
# while x < 9:    #这个while控制行数
#     x += 1
#     y = 0
#     while y < x:
#         y += 1
#         print("*",end='  ')
#     print()#换行


#*
#**
#***


#外边控制行 里边控制列

j=0
while j < 10:
    j += 1 # 1

    i = 0
    while i < 8:
        i += 1 #i=1 # i=2 i=3 i=4 i=5 i=6  i=7
        print("*",end='  ') # * * * * * * *
    print() #换行


# 10行 8列


