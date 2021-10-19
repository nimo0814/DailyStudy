# -*- coding:utf-8 -*-
# @Time  :2021/10/15 4:20 下午
# @AUTHOR :nimo
# @File :testquickSort01.py
import datetime
import random
#from quickSortDemo import quick_sort,get_num_position
from quickSortDemo import quick_sort
from quickSortDemo2 import get_num_position
import sys
sys.setrecursionlimit(1000000)

if __name__=='__main__':
    #nums=[random.randint(10,10000) for i in range(6000)]
    nums=[i for i in range(6000)]
    start=datetime.datetime.now()
    quick_sort(nums,0,len(nums)-1)
    end=datetime.datetime.now()
    print('Running time:%s Seconds' %(end-start))

