# -*- coding:utf-8 -*-
# @Time  :2021/10/15 5:20 下午
# @AUTHOR :nimo
# @File :quickSort_update.py
#改造前面的插入排序算法
from quickSortDemo2 import get_num_position
def insert_sort(nums,start,end):
    if not nums:
        return False
    for i in range(start+1,end+1):
        t=nums[i]
        for j in range(i-1,start-1,-1):
            k=j
            if nums[j]<=t:
                k=k+1
                break
            nums[j+1]=nums[j]
        nums[k]=t
    return True

def quick_sort(nums,start,end):
    if (end-start+1<10):
        #在排序的数组小到一定程度时，使用插入排序
        insert_sort(nums,start,end)
        return
    pos=get_num_position(nums,start,end)
    quick_sort(nums,start,pos-1)
    quick_sort(nums,pos+1,end)