# -*- coding:utf-8 -*-
# @Time  :2021/11/3 10:42 上午
# @AUTHOR :nimo
# @File :LList1_Demo.py
from random import randint

from LList_Demo import LList,LNode,LinkedListUnderflow


class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear=None

    def prepend(self,elem):
        if self._head is None:
            self._head=LNode(elem,self._head)
            self._rear=self._head
        else:
            self._head=LNode(elem,self._head)

    def append(self,elem):
        if self._head is None:
            self._head=LNode(elem,self._head)
            self._rear=self._head
        else:
            self._rear.next=LNode(elem)
            self._rear=self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p=self._head
        if p.next is None:
            e=p.elem
            self._head=None
            return e
        while p.next.next is not None:
            p=p.next
        e=p.next.elem
        p.next=None
        self._rear=p
        return e

mlist1=LList1()
mlist1.prepend(99)
for i in range(11,20):
    mlist1.append(randint(1,20))




