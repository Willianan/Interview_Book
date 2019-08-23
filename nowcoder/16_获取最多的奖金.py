# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-19 10:09
@Project:InterView_Book
@Filename:16_获取最多的奖金.py
@description:
题目描述
小明在越南旅游，参加了当地的娱乐活动。小明运气很好，拿到了大奖， 到了最后的拿奖金环节。
小明发现桌子上放着一列红包，每个红包上写着奖金数额。现在主持人给要求小明在这一列红包之
间“切”2刀，将这一列红包“切”成3组，并且第一组的奖金之和等于最后一组奖金和（允许任意一组
的红包集合是空）。最终第一组红包的奖金之和就是小明能拿到的总奖金。小明想知道最多能拿到的
奖金是多少，你能帮他算算吗。
举例解释：桌子上放了红包  1, 2, 3, 4, 7, 10。小明在“4,7”之间、“7,10” 之间各切一刀，
将红包分成3组 [1, 2, 3, 4]   [7]   [10]，其中第一组奖金之和=第三组奖金之和=10，所以小明可以拿到10越南盾。

输入描述:
第一行包含一个正整数n，(1<=n<= 200 000)，表示有多少个红包。
第二行包含n个正整数d[i]，表示每个红包包含的奖金数额。其中1<= d[i] <= 1000 000 000

输出描述:
小明可以拿到的总奖金
"""

def redPacket(n, nums):
    left, right = -1, n
    sum_left, sum_right = 0, 0
    res = 0
    while left < right:
        if sum_left == sum_right:
            res = sum_left
            left += 1
            right -= 1
            sum_left += nums[left]
            sum_right += nums[right]
        elif sum_left < sum_right:
            left += 1
            sum_left += nums[left]
        else:
            right -= 1
            sum_right += nums[right]
    return res
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    print(redPacket(n, nums))