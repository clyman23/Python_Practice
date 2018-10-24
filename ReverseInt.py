# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:20:57 2018

@author: clyman

Given a 32-bit signed int, reverse digits of int
Assume dealing with environment that can only store
ints within 32-bit signed int range 
[-2^31, 2^31 - 1]
Return 0 when reversed int overflows
"""

'''
NOTE:
In Python 3, int is unbounded.
Python will automatically switch to long 
when limit of int reached.
Can still check with sys.maxsize and
-sys.maxsize-1
'''
import sys

def reverse(num):
    flip = 0
    maxsize = sys.maxsize
    minsize = -sys.maxsize-1
    while num != 0:
        end = num % 10
        num = num//10
        if flip > maxsize/10 or (flip==maxsize/10 and end>7):
            return 0
        if flip < minsize/10 or (flip==minsize/10 and end<-8):
            return 0
        flip = flip*10 + end
    return flip












num = int(input("Give a number: "))
print(reverse(num))