# 引模块
import random

# 给函数的参数赋默认值（带默认值的参数）
def roll_dice(num = 2):
    # 摇num颗色子返回总的点数
    total = 0
    for _ in range(num):
        face = random.randint(1,6)
        total += face
    return total

print(roll_dice())