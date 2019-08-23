# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:58
@Project:InterView_Book
@Filename:32_字符串运用-密码截取.py
@description:
题目描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一
些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

输入描述:
输入一个字符串

输出描述:
返回有效密码串的最大长度
"""


def longestPalindrome(s):
	res = 0
	n = len(s)
	for i in range(n - 1):
		if s[i] == s[i + 1]:
			begin = i
			end = i + 1
			while (begin >= 0 and end < n and s[begin] == s[end]):
				begin -= 1
				end += 1
			res = max(res, end - begin - 1)
		if s[i - 1] == s[i + 1]:
			begin = i - 1
			end = i + 1
			while (begin >= 0 and end < n and s[begin] == s[end]):
				begin -= 1
				end += 1
			res = max(res, end - begin - 1)
	return res


if __name__ == "__main__":
	while True:
		try:
			s = input().strip()
			print(longestPalindrome(s))
		except:
			break
