# -*- coding:utf-8 -*-
# @Time  :2021/10/14 9:14 下午
# @AUTHOR :nimo
# @File :testDemo.py
import random
import datetime
from shellSort_demo1 import shell_sort
from insertSort_demo2 import  insert_sort2
if __name__=='__main__':
    nums=[random.randint(10,10000) for i in range(10000)]
    start=datetime.datetime.now()
    #shell_sort(nums)
    insert_sort2(nums)
    end=datetime.datetime.now()
    print('Running time: %s Seconds' %(end-start))