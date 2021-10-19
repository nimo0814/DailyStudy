# -*- coding:utf-8 -*-
# @Time  :2021/10/14 10:34 上午
# @AUTHOR :nimo
# @File :chooseSort_demo1.py
def choose_sort(nums):
    """
    选择排序
    :param nums:
    :return:
    """
    for i in range(len(nums)-1):
        min_val=nums[i]
        #标记最小值位置
        k=i
        for j in range(i+1,len(nums)):
            #每次遍历，找到本轮剩余元素的最小值，同时记录相应位置
            if nums[j]<min_val:
                min_val=nums[j]
                k=j
        #每次遍历数组后找到最小值，交换当前位置与本轮最小值的位置
        if k!=i:
            nums[i],nums[k]=nums[k],nums[i]

if __name__=='__main__':
    nums=[8,7,12,3,2,11,10,]
    choose_sort(nums)
    print('排序后的nums：{}'.format(nums))