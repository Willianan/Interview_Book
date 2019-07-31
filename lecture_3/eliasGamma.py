# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 21:19
@Project:InterView_Book
@Filename:eliasGamma.py
@description:
    Elias Gamma编码算法
"""



'''
题目描述：
	假设A是含有n个元素的整型数组，编写一个函数，将A中每一个元素进行Elias Gamma编码，并将编码后的字符串连成一个字符串。
'''


def intToBinaryString(n):
	s = ""
	while n > 0:
		if n & 1 == 0:
			s = "0" + s
		else:
			s = "1" + s
		n = n >> 1
	return s


def addZeroToHead(s):
	i = len(s)
	while i -1 >0:
		s = "0" + s
		i -= 1
	return s


def elsiasGammaEncode(n):
	s = intToBinaryString(n)
	s = addZeroToHead(s)
	return s


def eliasGammaEncodeArray(array):
	s = ""
	for i in range(len(array)):
		s += elsiasGammaEncode(array[i])
	return s


def getHeadZerosCount(s):
	cnt = 0
	for i in range(int(len(s))):
		if s[i] == '0':
			cnt += 1
		else:
			break
	return cnt

# 把二进制字符串转成对应整数
def binaryStringToInt(s):
	n = 0
	for i in range(len(s)):
		if s[i] == "1":
			n |= 1
		if i < len(s) - 1:
			n = n << 1
	return n


def eliasGammaDecode(s):
	length = getHeadZerosCount(s)
	if length <= 0:
		raise Exception("head zero error")
	s = s[length:]
	binary = s[0:length+1]
	n = binaryStringToInt(binary)
	return n

def eliasGammaDecodeToArray(s):
	array = []
	while len(s) > 0:
		n = eliasGammaDecode(s)
		array.append(n)
		encodeLength = len(elsiasGammaEncode(n))
		s = s[encodeLength:]
	return array



if __name__ == "__main__":
	print(bin(13))
	print(elsiasGammaEncode(13))
	array = [11,12,13]
	print(eliasGammaEncodeArray(array))

	s = eliasGammaEncodeArray(array)
	print(eliasGammaDecodeToArray(s))