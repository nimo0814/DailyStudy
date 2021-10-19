# -*- coding:utf-8 -*-
# @Time  :2021/10/14 3:28 下午
# @AUTHOR :nimo
# @File :shellSort_demo1.py
def shell_sort(nums):
    """
    希尔排序
    :param nums:
    :return:
    """
    n=len(nums)
    d=n//2
    while d>0:
        for i in range(d,n):
            temp=nums[i]
            j=i
            while j>=d and nums[j-d]>temp:
                nums[j]=nums[j-d]
                j-=d
            nums[j]=temp
        d=d//2
if __name__=='__main__':
    nums=[10,6,12,8,9,1,7,2]
    shell_sort(nums)
    print("排序后的nums：{}".format(nums))