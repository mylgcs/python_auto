# 写一个函数，生成指定长度的验证码，验证码由英文字母和数字构成。
import random

def gen_vccode(lenght = 4):
    all_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected_chars = random.choices(all_char,k=lenght)
    return ''.join(selected_chars)

print(gen_vccode())