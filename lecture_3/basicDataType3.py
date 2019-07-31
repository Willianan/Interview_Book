# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 16:28
@Project:InterView_Book
@Filename:basicDataType3.py
@description:
    使用二进制求解最大公约数
"""


'''
题目描述：
	两个整数x、y,它们的最大公约数d必须满足d|x,而且d|y.其中符号“|”表示整除
'''

def gcd(a,b):
	# 如果a能被b整除，那么b就是两个数的最大公约数
	if a % b == 0:
		return b
	d = a % b
	# a,b的最大公约数等于b,d的最大公约数
	return gcd(b,d)


def module(a,b):
	T = []
	t = 0
	# 先求T[n-1]
	while (b << t) <= a:
		t += 1
	t -= 1
	T.append(t)
	# 求取T[n-2],T[n-3].....T[0]
	a_prime = a - (b << T[len(T) - 1])
	while a_prime >= b:
		while (b << t) > a_prime:
			t -= 1
		T.append(t)
		a_prime = a_prime - (b << T[len(T) - 1])
	'''
	k = 2 << T[n-1] + 2 << T[n-2] + ... + 2 << T[0]
	a = k * b + d
	d = a - k * b = a - (b << T[n-1] + b << T[n-2] + ... + b<<T[0])
	'''
	d = a
	for i in range(len(T)):
		d -= (b << T[i])
	# d 就是两数相除余数
	return d
def binaryGcd(a,b):
	# 如果a能整除b，那么b就是两数的最大公约数
	if module(a,b) == 0:
		return b
	d = module(a,b)
	return binaryGcd(b,d)
if __name__ == "__main__":
	a = 128
	b = 48
	print("the greatest common divisor of {0} and {1} is: {2}".format(a,b,gcd(a,b)))
	print("the greatest common divisor of {0} and {1} is: {2}".format(a, b,binaryGcd(a,b)))