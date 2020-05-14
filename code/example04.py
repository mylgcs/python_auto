"""
多态

工资结算系统：三种类型的员工，部门经理、销售员、程序员
部门经理固定月薪15000元
程序员计时支付工资，每小时200元
销售员底薪1800元，销售额提成5%
根据录入的员工信息，为每个员工结算月薪
"""
from abc import abstractmethod, ABCMeta


# 抽象类（不能创建对象的类，专门用于继承）
class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    # 抽象方法（留给子类去实现的方法）
    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000


class Programmer(Employee):
    """程序员"""

    def get_salary(self):
        pass


class Salesman(Employee):
    """销售员"""

    def get_salary(self):
        pass
