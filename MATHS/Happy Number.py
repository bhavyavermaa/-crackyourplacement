"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def loop(num):
            sum=0
            while num!=0:
                d=num%10
                sum+=(d*d)
                num=int(num/10)
            return sum
        h=[]
        while n!=0:
            n=loop(n)
            if n==1:
                return True
                break
            if n not in h:
                h.append(n)
            else:
                return False
                break

"""
Approach:
1)Create a function loop which is used to find the sum of the squares of the digit of the number passed as parameter.
2) Create an empty array to store elements which are already once looped through.
note-We are using this array to detect an infinite cycle without letting the program go to infinite loop
3)Loop :-
    till number is not equal to zero
    4)find the sum of squares of the digits of the number
    5)Check if it is equal to 1 and return if TRUE
    6) Else check if res in h[], if not append
    7)if res is in h[] then return FALSE and break(Cycle detected)