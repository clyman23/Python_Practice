# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:24:31 2018

@author: clyman

Title: Roman Numeral to Int

Take an input string of a Roman numeral and convert into an int

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

I can subtract from V and X
X can subtract from L and C
C can subtract from D and M
"""


class Solution:
    
    def __init__(self):
        self.roman = input("Give a roman numeral: ")
        
    def convert(self):
        values = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}
        subtract = {'iv':4, 'ix':9, 'xl':40, 'xc':90, 'cd':400, 'cm':900}
        numerals = list(self.roman.lower())
        length = len(self.roman)
        number = 0
        next_char = ''
        for i in range(0,length):
            if next_char in subtract:
                next_char = ''
                pass
            else:
                character = numerals[i]
                try:
                    next_char = character+numerals[i+1]
                except:
                    next_char = ''
                if next_char in subtract:
                    number += subtract.get(next_char)
                elif character in values:
                    number += values.get(character)
        return number
    
def main():
    sol = Solution()
    print(sol.convert())
    
if __name__ == '__main__':
    main()

