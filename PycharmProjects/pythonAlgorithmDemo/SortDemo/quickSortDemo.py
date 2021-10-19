# -*- coding:utf-8 -*-
# @Time  :2021/10/15 10:11 上午
# @AUTHOR :nimo
# @File :quickSortDemo.py
def get_num_position(nums,left,right):
    #默认基准值为第一个
    base=nums[left]
    while left<right:
        #从最右边向左直到找到小于基准值的数
        while left<right and nums[right]>=base:
            right-=1
        #将小于基准数的值放到右边，left原来的位置放的是基准值（base）
        nums[left]=nums[right]
        #然后从左向右遍历，直到找到大于基准值的数
        while left<right and nums[left]<=base:
            left+=1
        #然后将left位置上的值放到right位置上，right位置上的值原本为base值
        nums[right]=nums[left]
    #left=right的位置上就是基准值
    nums[left]=base
    return  left

def quick_sort(nums,start,end):
    """
    快速排序算法
    """
    if start>=end:
        return
    pos =get_num_position(nums,start,end)
    #左边递归下去，直到排好序
    quick_sort(nums,start,pos-1)
    #右边递归下去，直到拍好序
    quick_sort(nums,pos+1,end)

if __name__=='__main__':
    nums=[8,7,9,6,11,3,12,20,9,5,1,10]
    quick_sort(nums,0,len(nums)-1)
    print('排序后的nums:{}'.format(nums))