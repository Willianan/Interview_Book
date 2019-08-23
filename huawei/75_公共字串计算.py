# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:20
@Project:InterView_Book
@Filename:75_公共字串计算.py
@description:
题目描述
计算两个字符串的最大公共字串的长度，字符不区分大小写
详细描述：
接口说明
原型：int getCommonStrLength(char * pFirstStr, char * pSecondStr);
输入参数：
     char * pFirstStr //第一个字符串
     char * pSecondStr//第二个字符串

输入描述:
输入两个字符串

输出描述:
输出一个整数
"""


def findcommonlengthsubstr(str1, str2):
	str1 = str1.lower()
	str2 = str2.lower()
	row = len(str1) + 1
	col = len(str2) + 1
	pre_max = [0] * col
	ret = 0
	for i in range(1, row):
		cur_max = [0] * col
		for j in range(1, col):
			cur_max[j] = pre_max[j - 1] + 1 if str1[i - 1] == str2[j - 1] else 0
			ret = max(ret, cur_max[j])
		pre_max = cur_max
	return ret


if __name__ == "__main__":
	str1 = input()
	str2 = input()
	print(findcommonlengthsubstr(str1, str2))