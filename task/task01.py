# 设计一个函数，传入的参数是一个列表，返回去掉列表中重复元素之后的列表。


def remove_dups1(items):
    return list(set(items))


item = [2, 2, 3, 4, 5, 6, 2, 8, 6, 7, 5, 4]
print(remove_dups1(item))
