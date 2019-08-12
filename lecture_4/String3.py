# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-08 15:13
@Project:InterView_Book
@Filename:String3.py
@description:
    字符串中单词的逆转
"""

'''
题目描述：
	给定一个字符串，它由若干单词组成，每个单词以空格分开。对字符串进行交换，使得字符串
	中单词的次序发生逆转
	要求编写算法实现该转换，同时算法的空间复杂度必须是O(1)
'''


class WordReverse:
	def __init__(self,sentence):
		self.sentence = sentence

	def reverseWordInSentence(self):
		# 先通过字符倒转的方式把整个句子里的所有字符倒转
		self.reverseByChar(0,len(self.sentence)-1)
		begin = 0
		end = 0
		while end < len(self.sentence):
			# 查找空格，分割出每个单词字符串
			while end < len(self.sentence) and self.sentence[end] != " ":
				end += 1
			# 翻转每个单词字符串
			self.reverseByChar(begin,end-1)
			begin = end + 1
			end = begin
		return self.sentence

	def reverseByChar(self, begin, end):
		# 把字符串里的字符前后倒转
		if begin < 0 or end > len(self.sentence):
			return
		sentenceList = list(self.sentence)
		while begin < end:
			c = sentenceList[begin]
			e = sentenceList[end]
			sentenceList[begin] = e
			sentenceList[end] = c
			begin += 1
			end -= 1
		self.sentence = "".join(sentenceList)





if __name__ == "__main__":
	s = "Alice like Bob"
	rs = WordReverse(s)
	s1 = rs.reverseWordInSentence()
	print(s1)