# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:29
@Project:InterView_Book
@Filename:26_字符串排序.py
@description:
题目描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
       如，输入： Type   输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
     如，输入： BabA   输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
     如，输入： By?e   输出： Be?y
样例：
    输入：
   A Famous Saying: Much Ado About Nothing(2012/8).
    输出：
   A  aaAAbc   dFgghh :  iimM   nNn   oooos   Sttuuuy  (2012/8).
"""

if __name__ == "__main__":
	while True:
		try:
			S = input()
			s = []
			res = [0] * len(S)
			for i, v in enumerate(S):
				if v.isalpha():
					s.append(v)
				else:
					res[i] = v
			s.sort(key=lambda x: x.lower())  # x.lower()为x的小写形式
			for i, v in enumerate(res):
				if not v:
					res[i] = s[0]
					s.pop(0)
			print(''.join(res))
		except:
			break