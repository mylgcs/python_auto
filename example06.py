""" 
    @Time : 2020/5/19 19:31 @Author : 马炎亮
    @File : example06.py @Software: PyCharm
    从文件中读取列表/字典
"""
import json


def main():
    with open('files/fruits.txt', 'r', encoding='utf-8') as file:
        fruits = json.load(file)
        print(type(fruits), fruits)
    with open('files/person.txt', 'r', encoding='utf-8') as file:
        person = json.load(file)
        print(type(person), person)


if __name__ == '__main__':
    main()
