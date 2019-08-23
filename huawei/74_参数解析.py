# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:16
@Project:InterView_Book
@Filename:74_参数解析.py
@description:
题目描述
在命令行输入如下命令：
xcopy /s c:\ d:\，
各个参数如下：
参数1：命令字xcopy
参数2：字符串/s
参数3：字符串c:\
参数4: 字符串d:\
请编写一个参数解析程序，实现将命令行各个参数解析出来。
解析规则：
1.参数分隔符为空格
2.对于用“”包含起来的参数，如果中间有空格，不能解析为多个参数。
比如在命令行输入xcopy /s “C:\program files” “d:\”时，参数仍然是4个，
第3个参数应该是字符串C:\program files，而不是C:\program，注意输出参数时，
需要将“”去掉，引号不存在嵌套情况。
3.参数不定长
4.输入由用例保证，不会出现不符合要求的输入

输入描述:
输入一行字符串，可以有空格

输出描述:
输出参数个数，分解后的参数，每个参数都独占一行
"""


if __name__ == "__main__":
	mm = input().split()
	cm = mm[1:]
	l = []
	for i in range(len(cm)):
		if '\\' not in cm[i] and '/' not in cm[i]:
			l.append(cm[i - 1] + cm[i])
		else:
			l.append(cm[i])
	print(len(l) + 1)
	print(mm[0])
	for j in l:
		print(j)