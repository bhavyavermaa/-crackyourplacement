"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s2=0
        s=0
        for j in nums:
            s+=j
        for i in range(n+1):
            s2+=i
        d=s2-s
        return d
"""
ADD APPROACH:-
1) Store the len of the array nums
2) Maintain two sum pointers
3) Loop through the array nums and store the actual sum of the elements of the array.
4) Run a loop in range of the number of elements and store a sum of ideal elements.
5) Find difference between the two sum pointers which will be the missing number and return it.