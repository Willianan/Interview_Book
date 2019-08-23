# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:35
@Project:InterView_Book
@Filename:44_员工考勤记录.py
@description:
题目描述
给定一个字符串来代表一个员工的考勤纪录，这个纪录仅包含以下两个字符：
'A' : Absent，缺勤,'P' : Present，到场
如果一个员工的考勤纪录中不超过两个'A'(缺勤),那么这个员工会被奖赏。
如果你作为一个员工，想在连续N天的考勤周期中获得奖赏，请问有多少种考勤的组合能够满足要求

输入描述:
考勤周期的天数N（正整数）

输出描述:
这N天里能获得奖赏的考勤组合数
"""

if __name__ == "__main__":
	n = int(input().strip())
	print(1 + (n ** 2 + n) // 2)