"""
字典的方法
- 删除元素：pop / popitem / clear
- 更新元素：update
- del
"""
person1 = {
    'name': '王大锤', 'e_contact': '王二锤', 'sex': True,
    'age': 55, 'height': 175, 'weight': 65,
    'office': '科华北路62号', 'home': '中同仁路8号',
    'tel': '13122334455', 'e_tel': '13800998877'
}
print(person1.pop('e_contact'))
print(person1)
print(person1.popitem())
print(person1.popitem())
del person1['home']
print(person1)
person1.update({'salary': 12000, 'has_car': True})
print(person1)
person1.clear()
print(person1)
