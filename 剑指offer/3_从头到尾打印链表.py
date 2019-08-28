# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 21:49
@Project:InterView_Book
@Filename:3_从头到尾打印链表.py
@description:
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]