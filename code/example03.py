"""
继承 ---> 从已经有的类创建新类的过程，提供继承信息的叫父类（超类、基类），
得到继承信息的叫子类（派生类）。继承是实现代码复用的方式,继承关系是一种is-a关系。
a student is a person. a teacher is a person.
"""


class Person:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def eat(self):
        print(f'{self.name}正在吃饭')

    def walk(self):
        print(f'{self.name}正在行走')

    def sleep(self):
        print(f'{self.name}正在睡觉')


class Artist(Person):

    def play_piano(self):
        print(f'{self.name}正在弹钢琴')

    def play_violin(self):
        print(f'{self.name}正在拉小提琴')


class Monk(Person):

    def chant(self):
        print(f'{self.name}正在念经')

    def knock_the_bell(self):
        print(f'{self.name}正在敲钟')


# Python中允许多重继承（一个类可以有多个父类）
# 但是实际开发时应该尽可能避免使用多重继承，因为可能会让代码变得混乱
class Student(Artist, Monk):
    """学生"""

    def __init__(self, stuid, name, nationality):
        self.id = stuid
        super().__init__(name, nationality)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


class Teacher(Person):
    """老师"""

    def __init__(self, name, nationality, title):
        self.title = title
        super().__init__(name, nationality)

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}')


def main():
    student = Student(1001, '王大锤', '湖南长沙')
    student.eat()
    student.study('Python程序设计')
    student.play_piano()
    student.play_violin()
    student.chant()
    student.knock_the_bell()
    teacher = Teacher('白元芳', '四川成都', '教授')
    teacher.sleep()
    teacher.teach('数据库系统设计')
    teacher.walk()
    # MRO - Method Resolution Order
    print(Student.mro())
    student.fly()


if __name__ == '__main__':
    main()
