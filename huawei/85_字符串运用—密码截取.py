# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 14:32
@Project:InterView_Book
@Filename:85_字符串运用—密码截取.py
@description:
题目描述
Catcher 是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无
关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
（注意：记得加上while处理多个测试用例）

输入描述:
输入一个字符串

输出描述:
返回有效密码串的最大长度
"""


def get_count(str_in):
	if str_in == str_in[::-1]:
		return len(str_in)
	count = 0
	for ii in range(0, len(str_in) - 1):
		if ii - count - 1 >= 0 and str_in[ii - count - 1:ii + 1] == str_in[ii - count - 1:ii + 1][::-1]:
			count += 2
		if ii - count >= 0 and str_in[ii - count:ii + 1] == str_in[ii - count:ii + 1][::-1]:
			count += 1
	return count


if __name__ == "__main__":
	while True:
		try:
			str_in = input().strip()
			if str_in:
				print(get_count(str_in))
		except:
			break
