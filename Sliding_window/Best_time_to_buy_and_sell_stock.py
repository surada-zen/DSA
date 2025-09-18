"""
Best Time to Buy and Sell Stock

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        bp = 0
        sp = 0
        size = len(prices)

        while bp <= sp and sp < size:
            possible_income = prices[sp] - prices[bp]
            maxprofit = max(maxprofit,possible_income)

            # make sure buyprice bp is less and sellprice sp is more

            if prices[sp] < prices[bp]:
                bp = sp            
            sp +=1

        return maxprofit


