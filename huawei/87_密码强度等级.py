# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 14:54
@Project:InterView_Book
@Filename:87_密码强度等级.py
@description:
题目描述
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
       一、密码长度:
       5 分: 小于等于4 个字符
       10 分: 5 到7 字符
       25 分: 大于等于8 个字符
       二、字母:
       0 分: 没有字母
       10 分: 全都是小（大）写字母
       20 分: 大小写混合字母
       三、数字:
       0 分: 没有数字
       10 分: 1 个数字
       20 分: 大于1 个数字
       四、符号:
       0 分: 没有符号
       10 分: 1 个符号
       25 分: 大于1 个符号
       五、奖励:
       2 分: 字母和数字
       3 分: 字母、数字和符号
       5 分: 大小写字母、数字和符号
       最后的评分标准:
       >= 90: 非常安全
       >= 80: 安全（Secure）
       >= 70: 非常强
       >= 60: 强（Strong）
       >= 50: 一般（Average）
       >= 25: 弱（Weak）
       >= 0:  非常弱
对应输出为：
  VERY_WEAK,
   WEAK,
   AVERAGE,
   STRONG,
   VERY_STRONG,
   SECURE,
   VERY_SECURE
       请根据输入的密码字符串，进行安全评定。
       注：
       字母：a-z, A-Z
       数字：-9
符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)
!"#$%&'()*+,-./     (ASCII码：x21~0x2F)
:;<=>?@             (ASCII<=><=><=><=><=>码：x3A~0x40)
[\]^_`              (ASCII码：x5B~0x60)
{|}~                (ASCII码：x7B~0x7E)
接口描述：
 Input Param String pPasswordStr:    密码，以字符串方式存放。
 Return Value 根据规则评定的安全等级。

 public static Safelevel GetPwdSecurityLevel(String pPasswordStr)
 {
     /*在这里实现功能*/
  return null;
 }

输入描述:
输入一个string的密码

输出描述:
输出密码等级
"""


class solution:
	def stringsLength(self, strings):
		lengthScore = 0
		if len(strings) <= 4:
			lengthScore += 5
		elif 5 <= len(strings) <= 7:
			lengthScore += 10
		else:
			lengthScore += 25
		return lengthScore

	def otherScore(self, strings):
		score = 0
		alpha_list = []
		digit_list = []
		symbol_list = []
		for i in strings:
			if i.isalpha():
				alpha_list.append(i)
			if i.isdigit():
				digit_list.append(i)
			else:
				symbol_list.append(i)
		l = [0, 0]
		for i in alpha_list:
			if ord(i) in range(97, 123):
				l[0] = 1
			if ord(i) in range(65, 91):
				l[1] = 1
		sum = l[0] + l[1]
		if sum == 1:
			score += 10
		if sum == 2:
			score += 20
		if len(digit_list) == 1:
			score += 10
		if len(digit_list) > 1:
			score += 20
		if len(symbol_list) == 1:
			score += 10
		if len(symbol_list) > 1:
			score += 25
		if len(alpha_list) != 0 and len(digit_list) != 0:
			score += 2
		elif len(alpha_list) != 0 and len(digit_list) != 0 and len(symbol_list) != 0:
			score += 3
		elif sum == 2 and len(digit_list) != 0 and len(symbol_list) != 0:
			score += 5
		else:
			pass
		return score

	def score(self, strings):
		return self.stringsLength(strings) + self.otherScore(strings)

	def printScore(self,score):
		if score >= 90:
			print('VERY_SECURE')
		elif score >= 80:
			print('SECURE')
		elif score >= 70:
			print('VERY_STRONG')
		elif score >= 60:
			print('STRONG')
		elif score >= 50:
			print('AVERAGE')
		elif score >= 25:
			print('WEAK')
		else:
			print('VERY_WEAK')


if __name__ == "__main__":
	solve = solution()
	while True:
		try:
			s = input()
			score = solve.score(s)
			solve.printScore(score)
		except:
			break
