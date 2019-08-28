# -*- coding:utf-8 -*-
"""
@Author：Charles Van
@E-mail:  williananjhon@hotmail.com
@Time：2019-08-23 22:01
@Project:InterView_Book
@Filename:6_旋转数组的最小数字.py
@description:
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        elif length == 1:
            return rotateArray[0]
        else:
            left = 0
            right = length - 1
            while left < right:
                mid = (left + right) / 2
                if rotateArray[mid] < rotateArray[right]:
                    right = mid
                else:
                    left = mid + 1
            return rotateArray[left]