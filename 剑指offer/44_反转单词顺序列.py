# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-28 19:28
@Project:InterView_Book
@Filename:44_反转单词顺序列.py
@description:
题目描述
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例
如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的
句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""


class Solution:
	def ReverseSentence(self, s):
		# write code here
		if not s:
			return s
		strings1 = s.split()
		if len(strings1) == 0:
			return s
		else:
			strings2 = []
			for ch in strings1:
				strings2.append(ch)
				strings2.append(" ")
			strings2.reverse()
			return " ".join(strings2).strip()



if __name__ == "__main__":
	s = input()
	solution = Solution()
	print(solution.ReverseSentence(s))