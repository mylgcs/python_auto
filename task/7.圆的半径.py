# 写一个函数，传入圆的半径，返回圆的周长和面积。

import math

def calc_circle(radius):
    return 2 * math.pi * radius , math.pi * radius * radius

r = float(input('请输入圆的半径: '))

peri , area = calc_circle(r)

print(f'圆的周长:{peri:.4f}')
print(f"圆的面积:{area:.4f}")