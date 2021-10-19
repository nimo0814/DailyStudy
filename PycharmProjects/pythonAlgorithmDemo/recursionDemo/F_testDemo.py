# -*- coding:utf-8 -*-
# @Time  :2021/10/18 4:16 下午
# @AUTHOR :nimo
# @File :F_testDemo.py
def F(n):
    if n==1:
        return 1
    return n*F(n-1)