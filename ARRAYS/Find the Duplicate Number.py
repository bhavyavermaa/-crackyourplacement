"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            curr=abs(num)
            if nums[curr]<0:
                repeater=curr
            else:
                nums[curr]=-nums[curr]
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        return repeater
"""
Simple solution in O(1) space using the concept of Negative Marking
1) Iterate through the array and store the element in curr as current
2) If the element was less than 0 it was considered as the repeater and stored as repeater
3) Otherwise the number is converted into its negative and updated in array
4) Now in the second loop the array is iterated again and the numbers are restored to their previous positive form.
5) The repeated element stored hence is returned. 