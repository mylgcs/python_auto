# 某公司有三种类型的员工，分别是部门经理、程序员和销售员。
# 其中，部门经理每月固定月薪15000元；程序员计时支付月薪，每小时200元；销售员按照1800元底薪加上销售额5%的提成支付月薪。
# 设计一个工资计算系统，录入员工信息，计算员工的月薪。
from abc import abstractmethod, ABCMeta

class Employee(object, metaclass=ABCMeta):
    """员工"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Managr(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000


class Programmer(Employee):
    """程序员"""
    def __init__(self, name):
        self.working_hour = 0
        super().__init__(name)

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """销售员"""
    def __init__(self, name):
        self.sales = 0
        super().__init__(name)

    def get_salary(self):
        return 1800 + self.sales * 0.05

def main():
    emps = [
        Managr('曹操'), Programmer('荀彧'), Programmer('郭嘉'),
        Salesman('典韦'), Salesman('曹仁'), Programmer('张辽')
    ]
    for emp in emps:
        if isinstance(emp,Programmer):
            emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
        elif isinstance(emp,Salesman):
            emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
        print(f'{emp.name}本月工资为: {emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()