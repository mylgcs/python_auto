
# 逻辑运算符    and     == 值相等  = 赋值
# num = int(input("请输入"))
# print("同时被3和7整除",num % 3 == 0 and num % 7 == 0  )
# print("同时被3和7整除",num % 21 == 0  )
#
# print('结果:',(num % 3 == 0 or num %7 == 0) and (num % 21 != 0))

# year = int(input("请输入年份:"))
#
# print('是否是闰年:',(year % 4 ==0 and year % 100 != 0) or (year % 400 ==0 ))

# n = 15678
# h = n // 3600
# m = n % (3600) // 60
# s = n % 60
#
# print(h,'小时',m,'分',s,'秒')
# num = int(input('请输入成绩:'))
# if num <= 70:
#     print('真笨，不及格')
# elif num >= 80:
#     print('小子挺聪明，恭喜你及格了')
# i = 0
# while i < 100:
#     i += 2
#     print(i)
# result=int(input("请输入年龄："))
# if 18 > result >0:
#     print("未成年")
# elif result<=150:
#     print("成年")
# else:
#     print("这不是人")
age = int(input('请输入年龄:'))
if 18 > age > 0:
    print("未成年")
elif 150 > age >= 18:
    print('成年')
else:
    print('不是人')