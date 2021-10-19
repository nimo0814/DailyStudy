# -*- coding:utf-8 -*-
# @Time  :2021/10/13 8:02 下午
# @AUTHOR :nimo
# @File :insertSort_demo2.py
from bisect import bisect

def insert_sort2(nums):
    """
    插入排序：使用二分法实现元素快速插入
    """
    if not nums:
        return False
    for i in range(1,len(nums)):
        k=bisect(nums[:i],nums[i])
        nums[k],nums[k+1:i+1]=nums[i],nums[k:i]
    return True

if __name__=='__main__':
    nums=[8,7,12,3,2,11,10,]
    insert_sort2(nums)
    print('排序后的nums：{}'.format(nums))