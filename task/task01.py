# 写一个函数，实现对传入的多个参数中的数值元素求中位数的操作。

"""
说明：中位数（Median）又称中值，统计学中的专有名词，是按顺序排列的一组数据中居于中间位置的数，对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。
如果观察值有偶数个，通常取最中间的两个数值的平均数作为中位数。
"""

def find_median(*args):
    nums = [arg for arg in args if type(arg) in (int,float)]
    nums_len,mid=len(nums),len(nums) // 2
    nums.sort()
    if nums_len % 2:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2

print(find_median(2,3,4,5,6,7,8,7,8,9,10))