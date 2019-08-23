# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 14:54
@Project:InterView_Book
@Filename:48_从单向链表中删除指定值的节点.py
@description:
题目描述
输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。
链表结点定义如下：
struct ListNode
{
int       m_nKey;
ListNode* m_pNext;
};
详细描述：
本题为考察链表的插入和删除知识。
链表的值不能重复
构造过程，例如
1 <- 2
3 <- 2
5 <- 1
4 <- 5
7 <- 2
最后的链表的顺序为 2 7 3 1 5 4
删除 结点 2
则结果为 7 3 1 5 4

输入描述:
1 输入链表结点个数
2 输入头结点的值
3 按照格式插入各个结点
4 输入要删除的结点的值

输出描述:
输出删除结点后的序列，每个数后都要加空格
"""


if __name__ == "__main__":
	while True:
		try:
			s = input().split()
			num = int(s[0])
			res = [s[1]]
			for i in range(num - 1):
				a = s[2 + i * 2]
				b = s[3 + i * 2]
				res.insert(res.index(b) + 1, a)
			rm = s[-1]

			res.remove(rm)
			print(' '.join(res) + ' ')
		except:
			break