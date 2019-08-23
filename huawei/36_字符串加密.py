# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 11:24
@Project:InterView_Book
@Filename:36_字符串加密.py
@description:
题目描述
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：
首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保
留第1个，其余几个丢弃。现在，修改过的那个单词属于字母表的下面，如下所示：
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y
上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固
定于顶上那行，并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该
保留)。因此，使用这个密匙，Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。
请实现下述接口，通过指定的密匙和明文得到密文。
详细描述：
接口说明
原型：
voidencrypt(char * key,char * data,char * encrypt);
输入参数：
char * key：密匙
char * data：明文
输出参数：
char * encrypt：密文
返回值：
void

输入描述:
先输入key和要加密的字符串

输出描述:
返回加密后的字符串
"""


def encryption(s):
	encryl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
	          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	encryd = []
	index = []
	for i in range(len(s[0])):
		if (s[0][i].lower() not in encryd) and (s[0][i].upper() not in encryd):
			encryd.append(s[0][i])
	for j in encryl:
		if (j.lower() not in encryd) and (j.upper() not in encryd):
			encryd.append(j)
		else:
			continue
	for k in range(len(s[1])):
		for x in range(len(encryl)):
			if s[1][k] == encryl[x].lower() or s[1][k] == encryl[x].upper():
				index.append(x)
			else:
				continue
	nencry = ''
	for i in range(len(index)):
		if s[1][i].islower():
			nencry += encryd[index[i]].lower()
		if s[1][i].isupper():
			nencry += encryd[index[i]].upper()
	print(nencry)




if __name__ == "__main__":
	while True:
		try:
			s = []
			for i in range(2):
				s.append(input())
			encryption(s)
		except:
			break