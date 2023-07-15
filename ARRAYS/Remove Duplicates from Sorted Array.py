"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[unique]=nums[i]
                unique+=1
        return unique
"""
In-place we have sorted the array using the widely used Two Pointer Method
1) We have set a pointer "unique" as 1 which is used to denote the next place available for replacing the next unique element with.
note:- we have not used unique=0 since the array is sorted and the first element is naturally at the right position
2)We iterate the array from second elememt to end and check if it is a repeated element or a unique one.
3)On finding a unique element we replace it at the unique index and increment the value of unique index.
4)We return the count of the unique elements.
