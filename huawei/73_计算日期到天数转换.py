# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:04
@Project:InterView_Book
@Filename:73_计算日期到天数转换.py
@description:
题目描述
根据输入的日期，计算是这一年的第几天。
详细描述：
输入某年某月某日，判断这一天是这一年的第几天？。
接口设计及说明：
 /*****************************************************************************
 Description   : 数据转换
 Input Param   : year 输入年份
                Month 输入月份
                Day 输入天
 Output Param  :
 Return Value  : 成功返回0，失败返回-1（如：数据错误）
 *****************************************************************************/
 public static int iConverDateToDay(int year, int month, int day)
 {
     /* 在这里实现功能，将结果填入输入数组中*/
     return 0;
 }
 /*****************************************************************************
 Description   :
 Input Param   :
 Output Param  :
 Return Value  : 成功:返回outDay输出计算后的第几天;
                 失败:返回-1
 *****************************************************************************/
 public static int getOutDay()
 {
  return 0;
 }

输入描述:
输入三行，分别是年，月，日

输出描述:
成功:返回outDay输出计算后的第几天;
失败:返回-1
"""


if __name__ == "__main__":
	while True:
		try:
			[year, month, day] = map(int, input().split())
			number = 0
			if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
				day_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
			else:
				day_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
			for i in range(0, month - 1):
				number += day_per_month[i]
			number += day
			print(number)
		except:
			break