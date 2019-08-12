# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-02 16:19
@Project:InterView_Book
@Filename:Array4.py
@description:
    大型整数相乘
"""


"""
题目描述：
	假定有两个字符串表示的整型数，要求写一个函数，实现两个数字字符串的相乘，函数返回值也是字符串
"""


import math


class StringMultiply:
	def __init__(self,strX,strY):
		# 先将两个数字字符串的长度补齐
		# 两个数字字符串长度一致时才好进行分解运算
		self.x = strX
		self.y = strY
		if len(strX) < len(strY):
			for i in range(len(strY) - len(strX)):
				self.x = "0" + self.x
		if len(strY) < len(strX):
			for i in range(len(strX) - len(strY)):
				self.y = "0" + self.y


	def doMultiply(self,x,y):
		if x is None or y is None:
			return "0"
		if len(x) == 0 or len(y) == 0:
			return "0"
		if len(x) == 1 and len(y) == 1:
			vx = ord(x[0]) - ord('0')
			vy = ord(y[0]) - ord('0')
			vz = vx * vy
			return str(vz)
		'''
		将字符串切分成两半，两两做运算后再将结果整合在一起
		'''
		halfX = math.ceil(len(x) / 2)
		halfY = math.ceil(len(y) / 2)

		xh = x[0:halfX]
		xl = x[halfX:]
		yh = y[0:halfY]
		yl = y[halfY:]

		p1 = self.doMultiply(xh,yh)
		for i in range(len(xl) + len(yl)):
			p1 += "0"
		p2 = self.doMultiply(xh,yl)
		for i in range(len(xl)):
			p2 += "0"
		p3 = self.doMultiply(xl,yh)
		for i in range(len(yl)):
			p3 += "0"
		p4 = self.doMultiply(xl,yl)

		# 做字符串加法把结果整合起来
		r = self.stringAdd(p1,p2)
		r = self.stringAdd(r,p3)
		r = self.stringAdd(r,p4)
		return r

	def stringAdd(self,strX,strY):
		x = strX
		y = strX
		if len(strX) < len(strY):
			for i in range(len(strY) - len(strX)):
				x = "0" + x
		if len(strY) < len(strX):
			for i in range(len(strX) - len(strY)):
				y = "0" + y
		k = len(x) - 1
		advance = 0
		result = ""
		while k >= 0:
			vx = ord(x[k]) - ord('0')
			vy = ord(y[k]) - ord('0')
			vz = vx + vy + advance
			# 记录进位
			advance = int(vz / 10)
			# 将个数结果转换为字符
			z = vz % 10
			c = chr(ord('0') + z)
			result = c + result
			k -= 1
		# 最后还有进位的话,在最高位添加一个1
		if advance == 1:
			result = chr(ord('0') + advance) + result
		return result


	def getResult(self):
		return self.doMultiply(self.x,self.y)



if __name__ == "__main__":
	s1 = "1234"
	s2 = "5678"
	sm = StringMultiply(s1,s2)
	print(int(s1) * int(s2))
	print(sm.getResult())

	s3 = "1234"
	s4 = "567"
	sm1 = StringMultiply(s3,s4)
	print(int(s3) * int(s4))
	print(sm1.getResult())