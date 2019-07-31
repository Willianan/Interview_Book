# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 20:55
@Project:InterView_Book
@Filename:basicDataType6.py
@description:
    数字与字符串相互转化，简单题目的隐藏陷阱
"""

'''
题目描述：
	写一个函数，实现数字不同进制间的转换。函数第1个输入参数是数字字符串s，第2个是一个整数b1，代表数字当前进制，第3个参数是整数b2，
	代表要转换的进制。其中1 < b1,b2 <= 16
'''


# 把是表示的数字字符串转换成b进制数
def strToInt(s,b):
	val = 0
	base = 1
	i = len(s) - 1
	while i >= 0:
		c = s[i]
		v = 0
		# 把字符转换成对应的数字
		if '0' <= c and c <= '9':
			v = ord(c) - ord('0')
		# 如果超过9，判断其是否属于十六进制的"A"到"E"之间
		if c >= 'A' and c <= 'E':
			v = 10 + ord(c) - ord('A')
		if i < len(s) - 1:
			'''
			每读取一个数字就要乘以相应进位
			'''
			base *= b
		val += v * base
		i -= 1
	return val


def intToStr(v,b):
	s = ""
	c = "0"
	while v >0:
		d = v % b
		if d >= 0 and d <= 9:
			c = chr(ord('0') + d)
		elif d >= 10:
			c = chr(ord('A') + d - 10)
		s += c
		v = int(v / b)
	return s

if __name__ == "__main__":
	print(strToInt("1234",10))
	v = 1234
	print("binary form of {0} is {1}".format(v,bin(v)))
	print("binary form of {0} by calling intToStr is {1}".format(v,intToStr(v,2)))