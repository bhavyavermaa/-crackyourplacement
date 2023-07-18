"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)==str(x)[::-1] else False

"""
Easiest one line answer:
I have converted the number to string and reversed it using list slicing methods and return true if same else false