# 用字典来保存学生的信息，学生信息包括：
# 学号（id）、姓名（name）、性别（sex）、语文成绩（verbal）、数学成绩（math）、联系电话（tel），
# 用一个列表保存6个学生的信息，如下所示，编写代码完成下面的操作。
students = [
    {'id': 1001, 'name': '周伟',  'sex': None, 'verbal': 90, 'math': 90, 'tel': '13512345670'},
    {'id': 1002, 'name': '赵刚',  'sex': True, 'verbal': 56, 'math': 80, 'tel': '13512345678'},
    {'id': 1003, 'name': '李强',  'sex': True, 'verbal': 48, 'math': 70, 'tel': '13512345680'},
    {'id': 1004, 'name': '刘毅',  'sex': None, 'verbal': 92, 'math': 60, 'tel': '13512345688'},
    {'id': 1005, 'name': '孙坚',  'sex': True, 'verbal': 85, 'math': 50, 'tel': '13512345698'},
    {'id': 1006, 'name': '王小美',  'sex': False, 'verbal': 37, 'math': 40, 'tel': '13512345699'},
]

# 输出语文成绩不及格学生的人数（假设成绩为百分制，及格分数为60分）。

print(len([stu for stu in students if stu['verbal'] < 60]))

# 输出数学成绩不及格学生的学号、姓名和成绩（假设成绩为百分制，及格分数为60分）。
students2 = [stu for stu in students if stu['math'] < 60]
for stu in students2:
    print(stu['id'],stu['name'],stu['math'])

# 输出联系电话尾号为8的学生的学号和姓名。
students3 = [stu for stu in students if stu['tel'][-1] == '8']
for stu in students3:
    print(stu['id'], stu['name'])

# 删除学生列表中性别为None的学生。
students4 = [stu for stu in students if stu['sex'] is not None]
print(students4)

# 输出男学生和女学生的平均成绩（包括语文和数学两门课程）
male_scores = [stu['verbal'] + stu['math'] for stu in students if stu['sex']]
print(f'男学生平均成绩: {sum(male_scores) / len(male_scores) / 2:.1f}分')
female_scores = [stu['verbal'] + stu['math'] for stu in students if not stu['sex']]
print(f'女学生平均成绩: {sum(female_scores) / len(female_scores) / 2:.1f}分')
