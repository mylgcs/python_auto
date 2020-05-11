# 写一个函数，求出列表中数值类元素（int、float）的平均值。

def calc_avg(item):
    total,counter = 0,0
    for i in item:
        if type(i) in (int,float):
            total += i
            counter += 1
    return  total / counter
item = [8,10,25,60,90,100,110]
print(calc_avg(item))