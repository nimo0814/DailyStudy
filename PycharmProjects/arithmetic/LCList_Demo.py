# -*- coding:utf-8 -*-
# @Time  :2021/11/3 11:05 上午
# @AUTHOR :nimo
# @File :LCList_Demo.py
from LList_Demo import LNode,LinkedListUnderflow
class LCList:
    def __init__(self):
        self._rear=None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p=LNode(elem)
        if self._rear is None:
            p.next=p
            self._rear=p

        else:
            p.next=self._rear.next
            self._rear.next=p

    def append(self,elem):
        self.prepend(elem)
        self._rear=self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p=self._rear.next
        if self._rear is p:
            self._rear=None
        else:
            self._rear.next=p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p=self._rear.next
        while True:
            print(p.elemm)
            if p is self._rear:
                break
            p=p.next