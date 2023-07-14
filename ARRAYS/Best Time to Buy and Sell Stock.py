
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


"""
After several attempts of bruteforce and failure on corner cases, this is my solution.:
1) Calculate the length of the array
2) Check if the number of elements is=0 --> return 0
3)else: set the minimum price to the zeroeth element
4)set maximum profit to 0
5)Loop: Start a loop ranging from the second element to the n:
6) If the elements is smaller than minimum element: --> Update the minimum price
7) else: set the maximum profit by checking if which is maximum - the current maximum profit OR the different of the current element and the minimum price
8) At the end of the loop we will attain the maximum profit which is returned.