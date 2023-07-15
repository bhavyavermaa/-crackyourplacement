"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_idx=i
            for j in range(i+1,len(nums)):
                if nums[min_idx]>nums[j]:
                    min_idx=j
            nums[i],nums[min_idx]=nums[min_idx],nums[i]
        return nums

"""
I have used the concept of Selection Sort.
Since the question requires to sort it in-place therefore Selection Sort was the easiest fit.