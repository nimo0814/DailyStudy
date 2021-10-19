# -*- coding:utf-8 -*-
# @Time  :2021/10/18 4:34 下午
# @AUTHOR :nimo
# @File :isSametree_demo.py
"""
给定两个二叉树，编写一个函数来检验它们是否相同。如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
"""
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    return p.val==q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
