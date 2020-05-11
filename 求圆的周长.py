"""
函数返回多个值的情况
"""
import math

# def perimeter(raduis):
#     return 2 * math.pi * raduis
#
# print(perimeter(9))

def calc_circle(raduis):
    return 2 * math.pi, math.pi * raduis ** 2

r = float(input('请输入圆的半径: '))

peri, area = calc_circle(r)
print(f'圆的周长: {peri:.4f}')
print(f'圆的面积: {area:.4f}')