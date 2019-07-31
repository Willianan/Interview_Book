# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 21:45
@Project:InterView_Book
@Filename:basicDataType8.py
@description:
    整型的二进制乘法
"""



'''
题目描述：
	完成一个函数实现两个无符号整数的乘法运算，函数不能使用加法、乘法，不能使用++或--等操作
'''



def binaryAdd(x,y):
	# advance 表示进位 ，r表示当前相加的比特位在二进制中的位置
	v = 0
	advance = 0
	r = 0
	while x > 0 or y > 0:
		# 取当前最低位的比特位值
		i = x & 1
		j = y & 1
		x = x >> 1
		y = y >> 1
		b = i ^ j
		if b == 1:
			# 两个比特位的值不同，因此异或结果为1
			if advance == 1:
			# 存在进位，两个比特位相加的结果再加上进位后值为0，同时产生一个进位
				b = 0
		else:
			if i & j == 1:
				# 两个比特位的值都是1
				if advance == 1:
					# 进位为1， 相加结果为1，并产生一个进位
					b = 1
				else:
					b = 0
					advance = 1
			else:
					b = 1
					advance = 0
		b = b << r
		v |= b
		r += 1
	if advance == 1:
		v |= (advance << r)
	return v


def binaryMultiply(a,b):
	stack = []
	s = 0
	while b > 0:
		if b & 1 == 1:
			stack.append(a << s)
		else:
			stack.append(0)
		b = b >> 1
		s += 1
	while len(stack) > 1:
		x = stack.pop()
		y = stack.pop()
		z = binaryAdd(x,y)
		stack.append(z)
	return stack.pop()

if __name__ == "__main__":
	a = 0b1101
	b = 0b1011
	print("{0} + {1} = {2}".format(bin(a),bin(b),bin(a+b)))
	v = binaryAdd(a,b)
	print("result from binary add is {0}".format(bin(v)))
	v = binaryMultiply(63,7)
	print(v)