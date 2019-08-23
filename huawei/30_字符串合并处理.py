# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-21 10:50
@Project:InterView_Book
@Filename:30_字符串合并处理.py
@description:
题目描述
按照指定规则对输入的字符串进行处理。

详细描述：
将输入的两个字符串合并。
对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标意思是字符在字符串中的位置。
对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，
则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。如字符为‘4’，
为0100b，则翻转后为0010b，也就是2。转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。
举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
接口设计及说明：

/*
功能:字符串处理
输入:两个字符串,需要异常处理
输出:合并处理后的字符串，具体要求参考文档
返回:无
*/
void ProcessString(char* str1,char *str2,char * strOutput)
{
}

输入描述:
输入两个字符串

输出描述:
输出转化后的结果
"""


def convert(s):
	ssc = dic[int(bin(dic.index(s.upper())).replace("0b", "").rjust(4, "0")[::-1], 2)]
	return ssc

if __name__ == "__main__":
	dic = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	while True:
		try:
			sss = input().replace(" ", "")  # s是输入的合并后的字符串
			# 奇偶个数的字符串分别排序
			ss_1 = sorted(sss[::2])  # 偶数部分
			ss_2 = sorted(sss[1::2])  # 奇数部分
			ss1 = ''.join(ss_1)
			ss2 = ''.join(ss_2)
			ssw = '0123456789abcdefABCDEF'
			ss = ''
			for i in range(len(ss1)):
				if (ss1[i] in ssw):
					ss += convert(ss1[i])
				else:
					ss += ss1[i]
				if len(ss2) != i:  # 注意偶数串可能比奇数串长一个字符
					if ss2[i] in ssw:
						ss += convert(ss2[i])
					else:
						ss += ss2[i]
			print(ss)
		except:
			break