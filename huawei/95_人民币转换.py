# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 16:53
@Project:InterView_Book
@Filename:95_人民币转换.py
@description:
题目描述
考试题目和要点：
1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、
捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。（30分）
2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，
如￥ 532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。（30分）
3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，
如￥6007.14，应写成“人民币陆仟零柒元壹角肆分“。

输入描述:
输入一个double数

输出描述:
输出人民币格式
"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
numberList = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
integralUnit = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
fractionUnit = ['角', '分']


def solveF(f, res):
	if int(f) == 0:
		res.append("整")
	else:
		for i in range(len(f)):
			if int(f[i]) != 0:
				res.append(numberList[int(f[i])])
				res.append(fractionUnit[int(i)])
	return res


while True:
	try:
		a = input()
		if '.' in a:
			a = a.split('.')
		else:
			a = (a + '.00').split('.')
		y = a[0]
		f = a[1]
		res = ['人民币']
		y = y[::-1]  # 反过来
		for i in range(len(y))[::-1]:  # 从i=len(y)-1开始，一直到0
			if int(y[i]) == 0:
				res.append(numberList[0])
			else:
				res.append(numberList[int(y[i])])
				res.append(integralUnit[i])

		res = solveF(f, res)
		res = ''.join(res)
		while ('零零' in res):
			res = res.replace('零零', '零')
		res = res.replace('壹拾', '拾')
		res = res.replace('人民币零', '人民币')
		print(res)
	except:
		break