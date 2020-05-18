# 定义一个类来表示平面上的点，提供移动点和计算到另外一个点距离的方法。


class Point:
    """平面的点"""

    def __init__(self, y, x):
        self.y = y
        self.x = x


    def __repr__(self):
        return f'({self.y},{self.x})'


    def move_to(self, y, x):
        """移动到"""
        self.y = y
        self.x = x

    def move_by(self, dx, dy):
        """移动了"""
        self.y += dx
        self.x += dy

    def distance(self, other):
        return ((self.y - other.y) ** 2 + (self.x - other.x) ** 2) ** 0.5

def main():
    point = Point(100,30)
    point1 = Point(0,0)
    print(point)
    print(point1)
    print(point.distance(point1))
    point.move_to(1,2)
    print(point)
    point1.move_by(-1,-2)
    print(point1)



if __name__ == '__main__':
    main()