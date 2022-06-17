# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:35:23 2022

@author: asus
"""

#河內塔(Tower of Hanoi, 又名'漢諾塔')，其實踐如下

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b) #將小於最大片者，移至B柱，借助C柱
        hanoi(1, a, b, c) #將最大片移至C柱
        hanoi(n - 1, b, a, c) #將其餘移至C柱，借助A柱
def total(n):
    return print('總移動次數', pow(2, n) - 1)

nums = int(input('請輸入片數: '))

hanoi(nums, 'A', 'B', 'C')
total(nums)