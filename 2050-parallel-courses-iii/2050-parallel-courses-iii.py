from functools import cache

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n + 1)]

        # reverse graph: course -> prerequisites
        for u, v in relations:
            g[v].append(u)
        dp=[None]*n

        def dfs(u):
            if dp[u-1] is not None:return dp[u-1]
            ans = 0
            for v in g[u]:
                ans = max(ans, dfs(v))
            dp[u-1]=ans + time[u - 1]
            return dp[u-1]

        return max(dfs(i) for i in range(1, n + 1))