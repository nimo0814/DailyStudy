# -*- coding:utf-8 -*-
# @Time  :2021/10/11 10:58 上午
# @AUTHOR :nimo
# @File :bubbleSort_demo.py
def bubble_sort(nums):
    """
    冒泡排序算法
    输入：nums，无序列表
    执行完后会变成有序列表
    """
    #在这里添加一个交换的标记
    swapped=False
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-i-1):
            #如果当前元素比下一个元素大，则交换两个元素，保证左边的比右边的元素要小
            if nums[j]>nums[j+1]:
                #交换相邻元素
                nums[j],nums[j+1]=nums[j+1],nums[j]
                #出现了元素交换则标记
                swapped=True
        #如果一次循环都没有交换过数据，说明数据本身是有序的，则直接返回不用继续冒泡
        if not swapped:
            break


if __name__=='__main__':
    nums=[8,7,12,3,2,11,10,6]
    bubble_sort(nums)
    print('排序后的nums：{}'.format(nums))