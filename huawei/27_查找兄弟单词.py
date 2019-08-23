# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:34
@Project:InterView_Book
@Filename:27_查找兄弟单词.py
@description:
题目描述
实现一个可存储若干个单词的字典。用户可以：
在字典中加入单词
查找指定单词在字典中的兄弟单词个数
查找指定单词的指定序号的兄弟单词，指定序号指字典中兄弟单词按字典顺序排序后的序号(从1开始)
输入描述:
先输入字典中单词的个数，再输入n个单词作为字典单词。
输入一个单词，查找其在字典中兄弟单词的个数
再输入数字n

输出描述:
根据输入，输出查找到的兄弟单词的个数
"""


if __name__ == "__main__":
	while True:
		try:
			s = input().strip().split()
			num = int(s[0])
			bro_search_num = int(s[-1])
			word_list = []
			for i in range(1, num + 1):
				word_list.append(s[i])
			bro_search_word = s[i + 1]
			result = []
			for word in word_list:
				if word == bro_search_word or len(word) != len(bro_search_word):
					continue
				letter = list(word)
				for l in bro_search_word:
					if l in letter:
						letter.remove(l)
				if len(letter) == 0:
					result.append(word)
			result.sort()
			print(len(result))
			if bro_search_num <= len(result):
				print(result[bro_search_num - 1])
		except:
			break