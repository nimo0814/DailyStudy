# -*- coding:utf-8 -*-
# @Time  :2021/10/18 4:20 下午
# @AUTHOR :nimo
# @File :climbStairsDemo.py
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。
你有多少种不同的方法可以爬到楼顶呢？注意：给定 n 是一个正整数。
"""
def climb_stairs(n):
    #终止条件
    if n<=2:
        return n
    #递推公式和返回预定结果
    return climb_stairs(n-1)+climb_stairs(n-2)

def climbStairs(self,n:int):
    if n<=2:
        return n
    s=[1,2]
    for _ in range(3,n+1):
        s[0],s[1]=s[1],s[0]+s[1]
        return s[1]