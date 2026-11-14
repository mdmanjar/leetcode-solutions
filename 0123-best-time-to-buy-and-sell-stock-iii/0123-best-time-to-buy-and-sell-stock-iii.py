from functools import lru_cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @lru_cache(None)
        def dfs(i, holding, transactions_left):
            if i == len(prices) or transactions_left == 0:
                return 0
            
            # Choice 1: Do nothing
            ans = dfs(i + 1, holding, transactions_left)
            
            if not holding:
                # Buy stock
                ans = max(ans, dfs(i + 1, True, transactions_left) - prices[i])
            else:
                # Sell stock (completes a transaction)
                ans = max(ans, dfs(i + 1, False, transactions_left - 1) + prices[i])
                
            return ans

        return dfs(0, False, 2)