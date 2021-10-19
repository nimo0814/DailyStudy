# -*- coding:utf-8 -*-
# @Time  :2021/10/18 5:01 下午
# @AUTHOR :nimo
# @File :threeSum_demo.py
def three_sum(nums,target,count):
    res=[]
    #终止条件
    if not nums:
        return res

    if count==1 and target in nums:
        return [[target]]
    elif count==1 and target not in nums:
        return res

    #包含num[0]
    t1=three_sum(nums[1:],target-nums[0],count-1)
    #不包含nums[0]
    t2=three_sum(nums[1:],target,count)
    if t1:
        for i in range(len(t1)):
            t=[nums[0]]
            t.extend(t1[i])
            res.append(t)
    if t2:
        for j in range(len(t2)):
            res.append(t2[j])

    return res