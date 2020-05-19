""" 
    @Time : 2020/5/19 19:29 @Author : 马炎亮
    @File : example05.py @Software: PyCharm
    除了字符串和字节串，列表和字典对象也可以写入文件
    将列表/字典写入文件
"""
import json


def main():
    fruits = ['apple', 'banana', 'grape', 'orange', 'pitaya']
    with open('files/fruits.txt', 'w', encoding='utf-8') as file:
        json.dump(fruits, file)
    person = {'name': 'Hao LUO', 'age': 40, 'gender': 'Male'}
    with open('files/person.txt', 'w', encoding='utf-8') as file:
        json.dump(person, file)


if __name__ == '__main__':
    main()
