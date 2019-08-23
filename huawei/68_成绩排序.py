# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 16:22
@Project:InterView_Book
@Filename:68_成绩排序.py
@description:
题目描述
查找和排序
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
      都按先录入排列在前的规则处理。
   例示：
   jack      70
   peter     96
   Tom       70
   smith     67
   从高到低  成绩
   peter     96
   jack      70
   Tom       70
   smith     67
   从低到高
   smith     67
   Tom       70
   jack      70
   peter     96

输入描述:
输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开

输出描述:
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开
"""

import sys

if __name__ == "__main__":
	while True:
		try:
			num = int(sys.stdin.readline().strip())  # 人数
			flag = int(sys.stdin.readline().strip())  # 正序
			value_list = []
			for i in range(0, num):
				item = [each for each in sys.stdin.readline().strip().split()]
				item[1] = int(item[1])
				value_list.append(item)
			if flag == 0:
				sortlist = sorted(value_list, key=lambda x: x[1], reverse=True)
			else:
				sortlist = sorted(value_list, key=lambda x: x[1], reverse=False)
			for each in sortlist:
				print(str(each[0]) + ' ' + str(each[1]))
		except:
			# print e.message
			break