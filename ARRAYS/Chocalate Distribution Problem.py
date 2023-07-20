"""
Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.
"""
class Solution:

    def findMinDiff(self, A,N,M):
        if M==0 or N==0:
            return 0
        if N<M:
            return -1
        A.sort()
        min_diff=A[N-1]-A[0]
        for i in range(N-M+1):
            min_diff=min(min_diff,A[i+M-1]-A[i])
        return min_diff
"""
The bruteforce approach would have been doing an exhaustive search and then finding the right answer by iterating through them.
The optimal approach is a sliding window approach.
    We first sort the array.
    We make a window of size m and traverse it through the array and update the minimum difference we can find by subtracting the 
    smallest element from the largest element.
    And then return the minimum difference.
