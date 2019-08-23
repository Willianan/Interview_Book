# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-20 16:56
@Project:InterView_Book
@Filename:8_合并表记录.py
@description:
题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）
"""


if __name__ == "__main__":
	count = int(input())
	c = {}
	for _ in range(count):
		k, v = [i for i in map(lambda x: int(x), input().split(' '))]
		c[k] = c.setdefault(k, 0) + v
	for k, v in c.items():
		print(k, v)