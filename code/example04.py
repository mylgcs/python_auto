"""
集合是可变类型，可以通过集合的方法来添加删除元素
集合底层使用哈希存储，所以元素在内存中不是连续放置的而是离散存储的
集合的方法
- 添加元素：add / update
- 删除元素：discard / remove / pop / clear
- 判断两个集合有无公共元素: isdisjoint
"""
# 创建一个空集合
set1 = set()
# print(set1)
# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.add(55)
print(set1)
# 相当于两个集合求并集元素放入set1
# set1 = set1 | {1, 10, 100, 1000}
set1.update({1, 10, 100, 1000})
print(set1)    # {33, 1, 100, 55, 1000, 10}

# 通过discard方法删除指定元素
set1.discard(100)
set1.discard(99)
print(set1)    # {1, 10, 33, 55, 1000}
# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常
if 10 in set1:
    set1.remove(10)
print(set1)    # {33, 1, 55, 1000}

# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())
print(set1)

# clear方法可以清空整个集合
set1.clear()
print(set1)    # set()
