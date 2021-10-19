# -*- coding:utf-8 -*-
# @Time  :2021/10/15 4:48 下午
# @AUTHOR :nimo
# @File :quickSortDemo2.py
import random
def get_base(nums,left,right):
    index=random.randint(left,right)
    if index!=left:
        nums[left],nums[index]=nums[index],nums[left]
    return nums[left]

def get_base_middle(nums,left,right):
    if left==right:
        return nums[left]
    mid=(left+right)>>1

    if nums[mid]>nums[right]:
        nums[mid],nums[right]=nums[right],nums[mid]

    if nums[mid]>nums[left]:
        nums[left],nums[mid]=nums[mid],nums[left]

    return  nums[left]

def get_num_position(nums,left,right):
    base=get_base(nums,left,right)
    while left<right:
        while left < right and nums[right] >= base:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= base:
            left += 1
        nums[right] = nums[left]
        # 基准数的位置，并返回该位置值
    nums[left] = base
    return left
