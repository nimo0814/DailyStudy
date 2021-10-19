# -*- coding:utf-8 -*-
# @Time  :2021/10/14 3:09 下午
# @AUTHOR :nimo
# @File :choose_sort_link.py
def choose_sort_link(head):
    """
    排序链表
    :param head:
    :return:
    """
    first=head
    while first.next:
        p=first
        min_val=p.val
        #指向最小节点的位置
        k=p
        while p:
            if p.val<min_val:
                min_val=p.val
                k=p
            p=p.next
        #交换最小位置和遍历的起始位置的值
        first.val,k.val=min_val,first.val
        first=first.next
    return head