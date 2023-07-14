"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ans=[i,j]
        return ans

"""
SOLUTION:
1) Create an empty array ans=[]
2)Loop until the last element from zeroeth element -->i
3) Another loop from 1st element to last-->j
4)Check if the sum of two element is equal to target--> return else continue