# 引模块
import random


def generate_code(lenght=4):
    """生成长度为length的验证码，验证码由数字和英文字母构成"""
    # 构造一个所有候选字符的序列（字符串）
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 使用random模块的choices函数实现有放回随机抽样
    selected_chars = random.choices(all_chars, k=lenght)
    # 使用字符串的join方法对列表元素进行拼接
    return ''.join(selected_chars)


# print(generate_code())
for _ in range(10):
    print(generate_code(lenght=6))
