
# a = 66
# b = 88
# if a>b:
#     print(a)
# print("="*50)
#
# if b>a:
#     print(b)

# score = 66
# score1 = 88
# if score>score1:
#     print(score)
# else:
#     print(score1)
#
# print("%"*50)

# text = int(input("请输入一个整数:"))
# if text % 3 == 0:
#     print("能整除")
# else:
#     print("不能整除")


# < 18.5 偏瘦
# 18.5-24.9 正常
#24.9 -27 偏胖
# 27以上  肥胖

weight = float(input("请输入体重(kg):"))
height = float(input("请输入身高(m):"))

bmi = weight/height ** 2

if bmi < 18.5:
    print("需要长点肉了")
elif bmi < 24.9:
    print("标准身材")
elif bmi < 27:
    print("标准身材")
else:
    print("你这样的谁要啊")
print("~"*30)





