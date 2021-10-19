# -*- coding:utf-8 -*-
# @Time  :2021/10/13 7:40 下午
# @AUTHOR :nimo
# @File :insort_demo01.py
def insert_sort(nums):
    """
    插入排序
    """
    if not nums:
        return False
    for i in range(1,len(nums)):
        t=nums[i]
        #从i-1位置开始往前找
        for j in range(i-1,-1,-1):
            k=j
            #如果nums[j]大于t，继续往前，直到找到小于等于t的数
            if nums[j]<=t:
                k=k+1
                break
            #每次找到的nums[j]大于t，则将当前值向后移动一位
            nums[j+1]=nums[j]
        #此时找到t的位置，并将t放到对应位置
        nums[k]=t
    return True

if __name__=='__main__':
    nums=[8,7,12,3,2,11,10,]
    insert_sort(nums)
    print('排序后的nums：{}'.format(nums))