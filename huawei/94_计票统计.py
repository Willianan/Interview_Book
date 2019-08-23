# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 16:41
@Project:InterView_Book
@Filename:94_计票统计.py
@description:
题目描述
请实现接口：
unsigned int  AddCandidate (char* pCandidateName);
功能：设置候选人姓名
输入： char* pCandidateName 候选人姓名
输出：无
返回：输入值非法返回0，已经添加过返回0 ，添加成功返回1
Void Vote(char* pCandidateName);
功能：投票
输入： char* pCandidateName 候选人姓名
输出：无
返回：无
unsigned int  GetVoteResult (char* pCandidateName);
功能：获取候选人的票数。如果传入为空指针，返回无效的票数，同时说明本次投票活动结束，释放资源
输入： char* pCandidateName 候选人姓名。当输入一个空指针时，返回无效的票数
输出：无
返回：该候选人获取的票数
void Clear()
// 功能：清除投票结果，释放所有资源
// 输入：
// 输出：无
// 返回

输入描述:
输入候选人的人数，第二行输入候选人的名字，第三行输入投票人的人数，第四行输入投票。

输出描述:
每行输出候选人的名字和得票数量。
"""

while 1:
	try:
		num = 0
		d = {}
		n = int(input())
		m = input().split()
		rs = int(input())
		tp = input().split()
		for i in tp:
			d.setdefault(i, 0)
			d[i] = d[i] + 1
		for j in m:
			if j in d.keys():
				print(j + " : " + str(d[j]))
			else:
				print(j + " : 0")
		for k in d.keys():
			if k not in m:
				num = num + int(d[k])
		print("Invalid : " + str(num))
	except:
		break
