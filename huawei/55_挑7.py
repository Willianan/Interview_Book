# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:19
@Project:InterView_Book
@Filename:55_挑7.py
@description:
题目描述
输出7有关数字的个数，包括7的倍数，还有包含7的数字（如17，27，37...70，71，72，73...）的个数
（一组测试用例里可能有多组数据，请注意处理）

输入描述:
一个正整数N。(N不大于30000)

输出描述:
不大于N的与7有关的数字个数，例如输入20，与7有关的数字包括7,14,17.
"""


if __name__ == "__main__":
	while True:
		try:
			a, res = int(input()), 0
			for i in range(7, a + 1):
				if "7" in str(i) or i % 7 == 0:
					res += 1
			print(res)
		except:
			break