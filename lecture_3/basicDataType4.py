# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-07-31 16:52
@Project:InterView_Book
@Filename:basicDataType4.py
@description:
    素数判定
"""


"""
题目描述：
	素数判定，给定一个正整数n，请返回1~n中所有的素数
"""

def isPrime(k):
	for i in range(2,k):
		if k % i == 0:
			return False
	return True

def getPrimes(n):
	primes = []
	for i in range(1,n+1):
		if isPrime(i):
			primes.append(i)
	return primes



def isPrime2(k):
	# 先保存最小的三个素数，对于给定整数k，它会记录所有小于k的素数
	prime_array = [1, 2, 3]
	if k <= 3:
		return True
	for i in range(len(prime_array)):
		if k > prime_array[i] and k % prime_array[i] == 0:
			return False
	# 如果k是素数，把它键入素数数组
	prime_array.append(k)
	return True


def getPrime2(n):
	primes = []
	for i in range(1,n+1):
		if isPrime2(i):
			primes.append(i)
	return primes

def getPrimesInRange(n):
	primes = []
	for i in range(n+1):
		primes.append(True)
	for i in range(2,n+1):
		# 从第二个素数2开始删除，删除一轮下来后，如果接下来的primes[i]是Ture，那么其对应的整数就是素数
		if primes[i] == True:
			p = i
			j = 2
			# 把当前素数的倍数全部删除
			while p * j <= n :
				primes[p*j] = False
				j += 1
	for i in range(len(primes)):
		if primes[i] == True:
			print("{0},".format(i),end=" ")


if __name__ == "__main__":
	n = 100
	print(getPrimes(n))
	print(getPrime2(n))
	getPrimesInRange(n)