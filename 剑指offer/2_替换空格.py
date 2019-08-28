# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 21:43
@Project:InterView_Book
@Filename:2_替换空格.py
@description:
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

class solution:
	def replaceSpace(self,s):
		return "%20".join(s.plit(" "))
