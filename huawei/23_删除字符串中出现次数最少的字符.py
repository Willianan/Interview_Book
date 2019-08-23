# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:03
@Project:InterView_Book
@Filename:23_删除字符串中出现次数最少的字符.py
@description:
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。
"""


if __name__ == "__main__":
	while True:
		try:
			strings = input()
			array = []
			for i in strings:
				array.append(strings.count(i))
			result = []
			min_array = min(array)
			for (i, j) in zip(strings, range(len(array))):
				if array[j] != min_array:
					result.append(i)
			print(''.join(result))
		except:
			break