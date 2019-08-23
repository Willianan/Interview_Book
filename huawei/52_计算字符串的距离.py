# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:09
@Project:InterView_Book
@Filename:52_计算字符串的距离.py
@description:
题目描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需
的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，
删除一个字符。编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。
Ex：
字符串A:abcdefg
字符串B: abcdef
通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。
要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
请实现如下接口
/*  功能：计算两个字符串的距离
 *  输入： 字符串A和字符串B
 *  输出：无
 *  返回：如果成功计算出字符串的距离，否则返回-1
 */
     public   static   int  calStringDistance (String charA, String  charB)
    {
        return  0;
    }

输入描述:
输入两个字符串

输出描述:
得到计算结果
"""


def editDistance(str1, str2):
	len1 = len(str1) + 1
	len2 = len(str2) + 1
	dp = [[0 for i in range(len2)] for j in range(len1)]
	for i in range(len1):
		dp[i][0] = i
	for j in range(len2):
		dp[0][j] = j
	for i in range(1, len1):
		for j in range(1, len2):
			dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
	return dp[-1][-1]


if __name__ == "__main__":
	while True:
		try:
			print(editDistance(input(), input()))
		except:
			break