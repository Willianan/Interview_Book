# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 15:58
@Project:InterView_Book
@Filename:64_MP3光标位置.py
@description:
题目描述
MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下键才能浏览所有的歌曲。
为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第1首歌。
现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：
歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。
光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。
其他情况下用户按Up键，光标挪到上一首歌曲；用户按Down键，光标挪到下一首歌曲。
  2. 歌曲总数大于4的时候（以一共有10首歌为例）：
特殊翻页：屏幕显示的是第一页（即显示第1 – 4首）时，光标在第一首歌曲上，用户按Up键后，屏幕要显示最后一页
（即显示第7-10首歌），同时光标放到最后一首歌上。同样的，屏幕显示最后一页时，光标在最后一首歌曲上，用户
按Down键，屏幕要显示第一页，光标挪到第一首歌上。
一般翻页：屏幕显示的不是第一页时，光标在当前屏幕显示的第一首歌曲时，用户按Up键后，屏幕从当前歌曲的上一首
开始显示，光标也挪到上一首歌曲。光标当前屏幕的最后一首歌时的Down键处理也类似。
其他情况，不用翻页，只是挪动光标就行。

输入描述:
输入说明：
1 输入歌曲数量
2 输入命令 U或者D

输出描述:
输出说明
1 输出当前列表
2 输出当前选中歌曲
"""

def solve(n,s):
	beg = 1
	if n <= 4:
		lst = [str(i) for i in range(1, n + 1)]
		for i in s:
			if i == 'U' and beg == 1:
				beg = n
			elif i == 'U' and beg != 1:
				beg -= 1
			elif i == 'D' and beg == n:
				beg = 1
			else:
				beg += 1
		print(' '.join(lst))
		print(beg)
	else:
		beg_lst = [i for i in range(1, 5)]
		for i in s:
			if i == 'U' and beg == 1:
				beg = n
				beg_lst = [i for i in range(n - 3, n + 1)]
			elif i == 'D' and beg == n:
				beg = 1
				beg_lst = [i for i in range(1, 5)]
			elif i == 'D' and beg != beg_lst[-1]:
				beg += 1
			elif i == 'D' and beg == beg_lst[-1]:
				beg += 1
				beg_lst = [i for i in range(beg - 3, beg + 1)]
			elif i == 'U' and beg != beg_lst[0]:
				beg -= 1
			else:
				beg -= 1
				beg_lst = [i for i in range(beg, beg + 4)]
		print(' '.join(map(str, beg_lst)))
		print(beg)

if __name__ == "__main__":
	while True:
		try:
			n = int(input())
			s = input()
			solve(n,s)
		except:
			break