class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @cache
        def dfs(i,state,transaction):

          return 0 if i== len(prices) or transaction==0 \
            else (max(dfs(i+1,0,transaction-1)+prices[i],dfs(i+1,1,transaction)) if state \
            else max(dfs(i+1,1,transaction)-prices[i],dfs(i+1,0,transaction)))

        return dfs(0,0,k)