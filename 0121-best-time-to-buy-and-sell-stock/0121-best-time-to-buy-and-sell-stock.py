class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)==0:return 0
        buy=prices[0]
        profit=0

        for cost in prices:
            profit,buy=max(profit,cost-buy),min(cost,buy)
        return profit
        