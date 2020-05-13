# 设计一个函数，传入的参数是一个列表，返回去掉列表中重复元素之后的列表，列表中的元素需要保持原来的顺序。

def remove_dups2(items):
    items2 = []
    seen = set()
    for item in items:
        if item not in seen:
            items2.append(item)
            seen.add(item)
    return items2


list1 = [1,2,8,1,5,8,3,2,4,1,9,1,2,5,5]

print(remove_dups2(list1))