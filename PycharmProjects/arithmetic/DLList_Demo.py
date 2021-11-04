# -*- coding:utf-8 -*-
# @Time  :2021/11/3 11:47 上午
# @AUTHOR :nimo
# @File :DLList_Demo.py
from LList1_Demo import LList1,LinkedListUnderflow
class DLNode:
    def __init__(self,elem,prev=None,next=None):
        self.elem=elem
        self.prev=prev
        self.next=next
class DLList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self,elem):
        p=DLNode(elem,None,self._head)
        if self._head is None:
            self._rear=p
        else:
            p.next.prev=p
        self._head=p

    def append(self,elem):
        p=DLNode(elem,self._rear,None)
        if self._head is None:
            self._head=p
        else:
            p.prev.next=p
        self._rear=p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e=self._head.elem
        self._head=self._head.next
        if self._head is not None:
            self._head.prev=None
        return e
    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e=self._rear.elem
        self._rear=self._rear.prev
        if self._rear is not None:
            self._head=None
        else:
            self._rear.next=None
        return e

