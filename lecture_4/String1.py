# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 9:40
@Project:InterView_Book
@Filename:String1.py
@description:
    字符串的旋转
"""



'''
题目描述
	A是含有n个元素的数组，如果可以申请到足够大内存，那么把A从位置i开始旋转是比较简单的。要求设计一个时间复杂度为O(N)、空间
	复杂度为O(1)的算法，实现字符串A从给定位置开始旋转
'''

def roundString(str):
	begin = 0
	end = len(str) - 1
	ss = list(str)
	while begin < end:
		# 交换begin和end指向的字符
		temp = ss[begin]
		ss[begin] = ss[end]
		ss[end] = temp
		begin += 1
		end -= 1
	return ''.join(ss)


# 将给定字符串从位置i开始旋转
def rotateString(str,i):
	# i将字符串分成两部分，第一部分含有开头i个元素，后半部分含有n-1个元素
	# 先将整个字符串旋转
	s = roundString(str)
	# 全部倒转后前n-i个字符对应上面的后半部分，后面的i个字符对应前面的前半部分
	# 对这两部分分别进行倒转
	s1 = roundString(s[0:len(s)-i])
	s2 = roundString(s[len(s)-i:])
	# 倒转后合在一起是原来字符从位置i旋转后的结果
	return s1+s2


if __name__ == "__main__":
	str = "abcdefg"
	i = 4
	str = rotateString(str,i)
	print(str)