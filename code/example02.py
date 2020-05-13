"""
把对象造出来通过给对象发消息达到解决问题的目标 ----> 面向对象程序设计
"""
import math


class Circle:
    """圆"""

    def __init__(self, radius):
        self.radius = radius

    def calc_perimeter(self):
        """计算周长"""
        return 2 * math.pi * self.radius

    def calc_area(self):
        """计算面积"""
        return math.pi * self.radius ** 2


# 1. 定义类（数据抽象和行为抽象）
class Rectangle:
    """矩形类"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calc_perimeter(self):
        """计算周长"""
        return (self.width + self.height) * 2

    def calc_area(self):
        """计算面积"""
        return self.width * self.height


def main():
    # 2. 创建矩形的对象（构造器语法）
    r1 = Rectangle(5, 4)
    r2 = Rectangle(height=15, width=3)
    r3 = Rectangle(width=100, height=50)

    # 3. 给对象发消息（通过对象的引用使用访问成员运算符）
    print(f'矩形1的周长: {r1.calc_perimeter()}')
    print(f'矩形2的周长: {r2.calc_perimeter()}')
    print(f'矩形2的面积: {r2.calc_area()}')
    print(f'矩形3的面积: {r3.calc_area()}')

    # 2. 创建圆的对象（构造器语法）
    c = Circle(8.5)
    # 3. 给对象发消息（通过对象的引用使用访问成员运算符）
    print(f'圆的周长: {c.calc_perimeter():.3f}')
    print(f'圆的面积: {c.calc_area():.3f}')


if __name__ == '__main__':
    main()
