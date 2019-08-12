# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 14:31
@Project:InterView_Book
@Filename:String2.py
@description:
    游程编码
"""

'''
题目描述
	游程编码(Run-length encoding,RLE)是一种在线高效的压缩算法，它的简单做法主要是
	将连续出现的字符转换成重复出现的次数和该字符的组合。
	假定要编码的字符串只包含26个字母，不包含数字等非字母字符，要求编写出编解码算法
'''


def RLEncode(strings):
	encodeStr = []
	last = strings[0]
	count = 0
	for i in range(len(strings)):
		# 遍历每个字符，统计它连续出现的次数
		if strings[i] == last:
			count += 1
		else:
			encodeStr.append(str(count))
			encodeStr.append(last)
			count = 1
			last = strings[i]
	# 统计最后一个字符及其出现次数，这里容易遗漏的边界条件
	encodeStr.append(str(count))
	encodeStr.append(last)
	return " ".join(encodeStr)


def RLEDecode(s):
	decodeStr = []
	i = 0
	digitCount = 0
	while i < len(s):
		# 统计数字字符的个数，它们表示后面字符要出现的次数
		if s[i].isdigit() is True:
			digitCount += 1
			i += 1
		else:
			# 把数字字符转换为数字
			digitString = s[i - digitCount:i]
			print(digitString)
			count = int(digitString)
			c = s[i]
			# 根据次数添加字符
			for j in range(count):
				decodeStr.append(c)
			i += 1
			digitCount = 0
	return "".join(decodeStr)


if __name__ == "__main__":
	strings = "aaabcccaa"
	s1 = RLEncode(strings)
	strings = "11a1b3c2a"
	s2 = RLEDecode(s1)
	print(s2)
