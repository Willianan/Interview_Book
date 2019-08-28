# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 20:08
@Project:InterView_Book
@Filename:48_不用加减乘除做加法.py
@description:
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""


class Solution:
	def Add(self, num1, num2):
		# write code here
		array = []
		array.append(num1)
		array.append(num2)
		return sum(array)
