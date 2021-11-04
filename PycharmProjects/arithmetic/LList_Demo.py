# -*- coding:utf-8 -*-
# @Time  :2021/11/3 10:05 上午
# @AUTHOR :nimo
# @File :LList_Demo.py
class LNode:
    """
    定义链表节点类
    """
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

class LinkedListUnderflow(ValueError):
    pass

class LList:
    def __init__(self):
        self._head=None
    def is_empty(self):
        return self._head is None

    def prepend(self,elem):
        """
        在表头插入数据
        :param elem:
        :return:
        """
        self._head=LNode(elem,self._head)

    def pop(self):
        """
        删除表头节点并返回该节点数据元素
        :return:
        """
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e=self._head.elem
        self._head=self._head.next
        return  e

    def append(self,elem):
        """
        链表后端插入数据
        :param elem:
        :return:
        """
        if self._head is None:
            self._head=LNode(elem)
            return
        p=self._head
        while p.next is not None:
            p=p.next
        p.next=LNode(elem)

    def pop_last(self):
        """
        删除表中最后的元素
        :return:
        """
        if self._head is None:#链表为空时
            raise LinkedListUnderflow("in pop_last")
        p=self._head
        if p.next is None:#表中只有一个元素
            e=p.elem
            self._head=None
            return e
        while p.next.next is not None:#循环，直到p.next是最后节点
            p=p.next
        e=p.next.elem
        p.next=None
        return e

    def find(self,pred):
        """
        找到满足给定条件的表元素
        :param pred:
        :return:
        """
        p=self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p=p.next

    def printall(self):
        p=self._head
        while p is not None:
            print(p.elem,end='')
            if p.next is not None:
                print(', ',end='')
            p=p.next
        print('')

    def for_each(self,proc):
        p=self._head
        while p is not None:
            proc(p.elem)
            p=p.next

mlist1=LList()#先创建一个空表
for i in range(10):#通过循环在表首端加入9个元素
    mlist1.prepend(i)
for i in range(11,20):#通过循环在表尾端加入9个元素
    mlist1.append(i)
mlist1.printall()#顺序输出表里所有元素



