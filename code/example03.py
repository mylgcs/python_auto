"""
集合的运算
"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
# 方法一: 使用 & 运算符
print(set1 & set2)                # {2, 4, 6}
# 方法二: 使用intersection方法
print(set1.intersection(set2))    # {2, 4, 6}

# 并集
# 方法一: 使用 | 运算符
print(set1 | set2)         # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二: 使用union方法
print(set1.union(set2))    # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
# 方法一: 使用 - 运算符
print(set1 - set2)              # {1, 3, 5, 7}
# 方法二: 使用difference方法
print(set1.difference(set2))    # {1, 3, 5, 7}

# 对称差
# 方法一: 使用 ^ 运算符
print(set1 ^ set2)                        # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2))    # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1 | set2) - (set1 & set2))      # {1, 3, 5, 7, 8, 10}

# 判断子集
print(set2 <= set1)     # False
# 判断超集
print(set1 > set2)      # False
