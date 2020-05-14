"""
魔术方法：
__str__ / __repr__ / __lt__
"""


class Student:
    """学生"""

    def __init__(self, stuid, name):
        self.id = stuid
        self.name = name

    # string
    def __str__(self):
        return f'{self.id}: {self.name}'

    # representation
    def __repr__(self):
        return f'{self.id}: {self.name}'

    # less than
    def __lt__(self, other):
        return self.name < other.name

    # great than or equal to
    def __ge__(self, other):
        return self.name >= other.name

    def study(self, course_name):
        """学习
        :param course_name: 学习的课程名称
        """
        print(f'{self.name}正在学习{course_name}')

    def eat(self):
        """吃饭"""
        print(f'{self.name}正在吃饭')

    def sleep(self):
        """睡觉"""
        print(f'{self.name}正在睡觉')


def main():
    """主函数"""
    stu1 = Student(1001, 'Wang Dachui')
    print(stu1)
    stu2 = Student(1002, 'Bai Yuanfang')
    print(stu2)
    students = [stu1, stu2]
    print(students)
    print(ord('王'), ord('白'))
    print(stu1 < stu2)
    stu3 = Student(1003, 'Zhu Yuanzhang')
    print(stu2 < stu1 < stu3)
    print(stu2 >= stu1)
    # for code in range(0x4e00, 0x9fa6):
    #     print(chr(code), end='')


if __name__ == '__main__':
    main()
