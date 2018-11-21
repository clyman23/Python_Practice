# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:07:52 2018

Given an array of integers, return indices
of two numbers such that the two numbers add up
to a specific target

Assume each input has exactly one solution and
that the same element cannot be used twice

@author: clyman
"""

class Solution:
    def twoSum_bruteForce(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    pass
                elif target - nums[i] == nums[j]:
                    return i, j
                
    def twoSum_twoPassHashTable(self, nums, target):
        hash_map = {key:i for i,key in enumerate(nums)}
        for i in nums:
            complement = target - i
            if complement in hash_map.keys() and \
            hash_map.get(complement) != hash_map.get(i):
                return hash_map.get(i), hash_map.get(complement)
        return "Error"
    
    def twoSum_onePassHashTable(self, nums, target):
        hash_map = {}
        for i in nums:
            complement = target - i
            if complement in hash_map:
                return hash_map.get(complement), nums.index(i)
            hash_map[i] = nums.index(i)
        return 'Error'

nums = [1,2,3,19,5,64,6]
target = 67

print(Solution().twoSum_bruteForce(nums, target))
print(Solution().twoSum_twoPassHashTable(nums, target))
print(Solution().twoSum_onePassHashTable(nums, target))