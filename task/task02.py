# 在练习1的基础上，定义一个类来表示平面上的线段，提供长度属性和判断两条线段（对应的直线）是否平行的方法，重叠（共线）也算平行。

from task import task01

class Line:
    """线段"""

    def __init__(self,start,end):
        self.start = start
        self.end = end

    @property
    def length(self):
        """长度"""

        return self.start.distance(self.end)