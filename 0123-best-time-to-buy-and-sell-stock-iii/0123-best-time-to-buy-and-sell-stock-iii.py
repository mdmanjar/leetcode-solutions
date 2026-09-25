class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)

        @lru_cache(None)

        def dfs(i,state,transaction):
            
            if i==n or transaction==-1:return 0

            return max(dfs(i+1,0,transaction-1)+prices[i],dfs(i+1,1,transaction)) if state else max(dfs(i+1,1,transaction)-prices[i],dfs(i+1,0,transaction))

        return dfs(0,0,1)
        