"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:]=nums2[0:]
        for i in range(m+n):
            min_idx=i
            for j in range(i+1,m+n):
                if nums1[min_idx]>nums1[j]:
                    min_idx=j
            nums1[min_idx],nums1[i]=nums1[i],nums1[min_idx]
"""
APPROACH:-
1) Since it is given that nums1 has a length of m+n total so we append the elements of nums2 at the end of nums1 in the leading zeroes.
2) Applying Selection Sort: 
# We have chosen selection sort since we cannot return an array and just have to sort it in nums1 only and selection sort is an
in-place algorithm.
    3)Loop in a range of m+n
    4)set the element as min_idx
    5) Loop from the next element until end and look for an element which is smaller than this one.
    6) If found store the index and swap in the end otherwise continue.
7) Eventually nums1 is sorted in-place
