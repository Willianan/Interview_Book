# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 17:26
@Project:InterView_Book
@Filename:77_火车进站.py
@description:
题目描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号。
要求以字典序排序输出火车出站的序列号。

输入描述:
有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。

输出描述:
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。
"""


def handle(pre_station, in_station, after_station):
	if not pre_station and not in_station:  # 所有车均已出栈
		result.append(" ".join(after_station))
	else:
		if in_station:  # 先出栈
			after_station.append(in_station.pop())
			handle(pre_station, in_station, after_station)
			in_station.append(after_station.pop())
		if pre_station:  # 再入栈
			in_station.append(pre_station.pop(0))
			handle(pre_station, in_station, after_station)
			pre_station.insert(0, in_station.pop())
	return result


if __name__ == "__main__":
	number = int(input())
	pre_station = [a for a in input().split()]
	result = []
	handle(pre_station, [], [])
	result.sort()
	for item in result:
		print(item)
