# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:33
@Project:InterView_Book
@Filename:29_回文子串.py
@description:
题目描述
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
("回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。)
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
可用C++,Java,C#实现相关代码逻辑

输入描述:
输入一个字符串S 例如“aabcb”(1 <= |S| <= 50), |S|表示字符串S的长度。

输出描述:
符合条件的字符串有"a","a","aa","b","c","b","bcb"
所以答案:7
"""

if __name__ == "__main__":
	s = input()
	n = len(s)
	numbers = 0
	for i in range(n):
		for j in range(i + 1, n + 1):
			string = s[i:j]
			if string == string[::-1]:
				numbers += 1
	print(numbers)