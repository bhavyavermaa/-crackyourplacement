"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                profit+=(prices[i]-prices[i-1])
        return profit

"""
I have used an iterative approach to optimize this solution:
OKay so first understand that whether we use the max function or iteratively calculate every single consecutive profit the
answer will always remain the same
 
I have iteratively checked every consecutive element to see if it is greater than the previous one and calculated the difference 
and have added it in the total profit at the same time and then returned it in the end"""