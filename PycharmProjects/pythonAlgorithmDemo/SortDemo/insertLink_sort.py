# -*- coding:utf-8 -*-
# @Time  :2021/10/13 8:20 下午
# @AUTHOR :nimo
# @File :insertLink_sort.py
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def insert_link_sort(head):
    sorted_head=ListNode(0)
    p=head
    while p:
        prev=sorted_head
        cur=prev.next
        if not cur:
    # 针对于第一次，第一个元素直接挂到sorted_head后即可
            sorted_head.next=ListNode(p.val)
        else:
            find= False
            while cur:
                if p.val>cur.val:
                    #插入节点值大于当前指向的节点值，将cur和prev之后后移一位再比较
                    cur=cur.next
                    prev=prev.next
                else:
                    #当前节点值大于插入元素的值，在此执行插入操作然后退出循环
                    insert_data=ListNode(p.val)
                    prev.next=insert_data
                    insert_data.next = cur
                    find=True
                    break
            #对于大于所有的值，需要插入到有序链表的末尾
            if not find:
                prev.next=ListNode(p.val)
        p=p.next
    return sorted_head.next


