# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 15:23
@Project:InterView_Book
@Filename:41_X游戏.py
@description:
题目描述
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，
且和 X 不同的数。要求每位数字都要被旋转。
如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。
0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；
6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

输入描述:
输入正整数N

输出描述:
输出1到N中好数个数
"""


def is_goodnum(x):
	x = str(x)
	no, df = [3, 4, 7], [2, 5, 6, 9]
	no_, df_ = 0, 0
	for num in x:
		if int(num) in no:
			return False
		elif int(num) in df:
			df_ += 1
	return True if df_ > 0 else False


if __name__ == "__main__":
	N = int(input().strip())
	count = 0
	for i in range(1, N + 1):
		i = str(i)
		if '3' in i or '4' in i or '7' in i:
			continue
		elif '2' in i or '5' in i or '6' in i or '9' in i:
			count += 1
		else:
			continue
	print(count)
