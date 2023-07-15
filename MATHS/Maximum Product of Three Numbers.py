"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return max(nums[0]*nums[1]*nums[n-1],nums[n-1]*nums[n-2]*nums[n-3])

"""
-This is the easiest answer to the following problem:
-This problem is easier but there is a twist of negative numbers.
-The main thought that comes as soon as one see this problem is simply return the product of last three numbers but it wont pass all
the test cases because there can be huge numbers with negative sign in the front too.
-There can be two scenarios in which the product can be largest-
-One is simple the product of the last numbers but it works only when numbers at the positive end are greater than the neg ones.
-Another is product of the first two negative numbers and the last element(positive number) which gives the positive largest product.
