# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 11:08
@Project:InterView_Book
@Filename:34_图片整理.py
@description:
题目描述
Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小
（ASCII码值从小到大）排列收好。请大家给Lily帮忙，通过C语言解决。

输入描述:
Lily使用的图片包括"A"到"Z"、"a"到"z"、"0"到"9"。输入字母或数字个数不超过1024。

输出描述:
Lily的所有图片按照从小到大的顺序输出
"""

if __name__ == "__main__":
	while True:
		try:
			s = input()
			tmp = []
			for i in s:
				tmp.append(ord(i))
			tmp.sort()
			n = len(tmp)
			for j in range(n):
				tmp[j] = chr(tmp[j])
			res = ''.join(tmp)
			print(res)
		except:
			break