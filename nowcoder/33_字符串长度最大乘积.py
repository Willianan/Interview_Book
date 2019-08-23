# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 14:46
@Project:InterView_Book
@Filename:33_字符串长度最大乘积.py
@description:
题目描述
已知一个字符串数组words，要求寻找其中两个没有重复字符的字符串，使得这两个字符串的长度乘积最大，输出这个最大的乘积。如：
words=["abcd","wxyh","defgh"], 其中不包含重复字符的两个字符串是"abcd"和"wxyh"，则输出16
words=["a","aa","aaa","aaaa"], 找不到满足要求的两个字符串，则输出0
输入描述:
Input:

["a","ab","abc","cd","bcd","abcd"]
输出描述:
Output:4
"""


def _judge(w1, w2):
	if len(w1) <= len(w2):
		for i in w1:
			if i in w2:
				return 0
		return len(w1) * len(w2)
	else:
		for i in w2:
			if i in w1:
				return 0
		return len(w1) * len(w2)

if __name__ == "__main__":
	words = eval(input())
	ret = [0] * len(words)
	if len(ret) == 0:
		print(0)
	else:
		for i in range(len(words) - 1):
			temp = 0
			for j in range(i + 1, len(words)):
				_out = _judge(words[i], words[j])
				if _out > temp:
					temp = _out
			ret[i] = temp
		print(max(ret))