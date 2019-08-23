# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 9:46
@Project:InterView_Book
@Filename:19_简单错误记录.py
@description:
题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理：
1、 记录最多8条错误记录，循环记录，对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。

输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：
"""

import sys

if __name__ == "__main__":
	out = []
	num = {}

	while True:
		input_ = sys.stdin.readline()[:-1]
		if input_ == '':
			break
		record, lines = input_.split()  # 才处理空格，数字
		if '\\' in record:
			name = record.split('\\')[-1][-16:]
		else:
			name = record[-16:]
		item = name + ' ' + lines
		if item not in num:
			num[item] = 1
			out.append(item)
		else:
			num[item] += 1

	for item in out[-8:]:
		sys.stdout.write(item + ' ' + str(num[item]) + '\n')
