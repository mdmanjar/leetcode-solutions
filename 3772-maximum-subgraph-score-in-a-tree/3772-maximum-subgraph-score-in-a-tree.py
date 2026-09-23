class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g=[[] for _ in range(n)]

        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        for i in range(n):
            good[i]=1 if good[i] else -1
        dp=[0]*n
        ans=[0]*n
        
        def post_order(u,p):
            dp[u]=good[u]
            for v in g[u]:
                if v!=p:
                    post_order(v,u)
                    dp[u]+=max(0,dp[v])
        def pre_order(u,p):
            if p==-1:
                ans[u]=dp[u]
            else:
                ans[u]=dp[u]+max(0,ans[p]-max(0,dp[u]))
            for v in g[u]:
                if v!=p:pre_order(v,u)
        post_order(0,-1)
        pre_order(0,-1)
        return ans


        