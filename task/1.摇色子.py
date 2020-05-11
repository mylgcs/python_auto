# 写一个函数实现摇色子的功能，传入色子的个数，返回所有色子的点数总和。
import random

def roll_dice(num):
    total = 0
    for _ in range(num):
        total += random.randint(1,6)
    return total
print(roll_dice(4))
