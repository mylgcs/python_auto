
# a  = 12  #10进制
# print(a + 1) #13
#
#
# b = 0b11101  #2进制
# print(b+1) # 30
#
# #其它进制转成10进制
#
#
#
# c = 0o12  #八进制
# print(c+1) # 11
#
# d = 0x1F
# print(d+1) #32

# a = 12
#
# print(bin(a)) # 转成2进制
# print(oct(a))
# print(hex(a))
# x = (input())
# print(type(x))
height = float(input('请输入你的身高(米):'))
weight = float(input('请输入你的体重(公斤):'))
x = weight / height ** 2
if 18.5 < x < 24.9:
    print('身材正常')
else:
    print('身材不正常')

# 请输入你的身高(米):1.92
# 请输入你的体重(公斤):93
# 身材不正常