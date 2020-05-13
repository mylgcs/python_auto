# 找出10000以内的所有完美数。
from task.module1 import is_perfect

for num in range(1, 10000):
    if is_perfect(num):
        print(num)


