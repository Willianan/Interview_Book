# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 20:14
@Project:InterView_Book
@Filename:basicDataType5.py
@description:
    判断矩形交集
"""



import matplotlib.pyplot as plt
import matplotlib.patches as patches
'''
题目描述：
	给定两个坐标轴对齐的矩形，判断它们是否相交；如果相交，给出它们相交所形成的矩形
'''

class Rectangle(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.w = width
		self.h = height

	def isInterset(self,r):
		if self.x <= r.x + r.w and r.x <= self.x + self.w and self.y <= r.y + r.h and r.y <= self.y + self.h:
			return True
		return False
	def intersetRectangle(self,r):
		if self.isInterset(r):
			return Rectangle(max(self.x,r.x),max(self.y,r.y),min(r.x+r.w,self.x+self.w)-max(r.x,self.x),
			                 min(r.y+r.h,self.y+self.h)-max(r.y,self.y))
		return None

if __name__ == "__main__":
	S = Rectangle(0.1,0.1,0.5,0.5)
	R = Rectangle(0.2,0.2,0.6,0.5)
	fig = plt.figure()
	ax = fig.add_subplot(111,aspect='equal')
	ax.add_patch(patches.Rectangle((S.x,S.y),S.w,S.h,facecolor='red'))
	ax.add_patch(patches.Rectangle((R.x, R.y), R.w, R.h, facecolor='blue'))
	if S.isInterset(R) is True:
		interset = S.intersetRectangle(R)
		print("x:{0},y:{1},w:{2},h:{3}".format(interset.x,interset.y,interset.w,interset.h))
		ax.add_patch(patches.Rectangle((interset.x,interset.y),interset.w,interset.h,facecolor='green'))
		fig.savefig("rectangle1.png",dpi=90,bbox_inches='tight')
		plt.show()