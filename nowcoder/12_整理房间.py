# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 9:48
@Project:InterView_Book
@Filename:12_整理房间.py
@description:
题目描述
又到了周末，小易的房间乱得一团糟。他希望将地上的杂物稍微整理下，
使每团杂物看起来都紧凑一些，没有那么乱。地上一共有n团杂物，每团杂物都包含4个物品。
第i物品的坐标用(ai,bi)表示，小易每次都可以将它绕着(xi,yi)逆时针旋转90度，这将消耗
他的一次移动次数。如果一团杂物的4个点构成了一个面积不为0的正方形，我们说它是紧凑的。
因为小易很懒，所以他希望你帮助他计算一下每团杂物最少需要多少步移动能使它变得紧凑。

输入描述:
第一行一个数n(1 <= n <= 100)，表示杂物的团数。
接下来4n行，每4行表示一团杂物，每行4个数ai, bi，xi, yi, (-104 <= xi, yi, ai, bi <= 104)，
表示第i个物品旋转的它本身的坐标和中心点坐标。

输出描述:
n行，每行1个数，表示最少移动次数。
"""


def func(inputPoint):
	rotatePoint = [[] for i in range(4)]

	for i in range(4):
		x1, y1, a, b = inputPoint[i]
		rotatePoint[i].append([x1, y1])
		for j in range(3):
			x = a + b - y1
			y = b - a + x1
			rotatePoint[i].append([x, y])
			x1, y1 = x, y
	# print(rotatePoint)

	for i in range(len(rotatePoint[0])):
		x1, y1 = rotatePoint[0][i]
		for j in range(len(rotatePoint[1])):
			x2, y2 = rotatePoint[1][j]
			for m in range(len(rotatePoint[2])):
				x3, y3 = rotatePoint[2][m]
				for t in range(len(rotatePoint[3])):
					x4, y4 = rotatePoint[3][t]
					vec1 = [x1 - x2, y1 - y2]
					vec2 = [x1 - x3, y1 - y3]
					vec3 = [x1 - x4, y1 - y4]
					if vec1[0] * vec2[0] + vec1[1] * vec2[1] == 0:  # 向量积为0，垂直
						if vec1[0] * vec3[0] + vec1[1] * vec3[1] == vec2[0] * vec3[0] + vec2[1] * \
								vec3[1] and vec1[0] * vec3[0] + vec1[1] * vec3[1] != 0:
							# print("1:",(x1,y1),(x2,y2),(x3,y3),(x4,y4))
							return (i + j + m + t)
					else:
						if (vec1[0] * vec3[0] + vec1[1] * vec3[1] == 0 and vec1[0] * vec2[0] + vec1[1] * vec2[1] ==
						    vec3[0] * vec2[0] + vec3[1] * vec2[1] and vec3[0] * vec2[0] + vec3[1] * vec2[1] != 0) \
								or (
								vec2[0] * vec3[0] + vec2[1] * vec3[1] == 0 and vec1[0] * vec2[0] + vec1[1] * vec2[1] ==
								vec3[0] * vec1[0] + vec3[1] * vec1[1] and vec3[0] * vec1[0] + vec3[1] * vec1[1] != 0):
							# print("2:",(x1,y1),(x2,y2),(x3,y3),(x4,y4))

							return (i + j + m + t)
	return -1


inputPoint = []
n = int(input())
for i in range(n):
	inputPoint.append(list(map(int, input().split(" "))))
	inputPoint.append(list(map(int, input().split(" "))))
	inputPoint.append(list(map(int, input().split(" "))))
	inputPoint.append(list(map(int, input().split(" "))))

	# inputPoint = [[1, 1, 0, 0], [-2, 1, 0, 0], [-1, 1, 0, 0], [1, -1, 0, 0]]

	res = func(inputPoint[:])
	print(res)
	inputPoint = []