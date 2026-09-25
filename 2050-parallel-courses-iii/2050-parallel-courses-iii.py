from functools import cache

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n + 1)]

        # reverse graph: course -> prerequisites
        for u, v in relations:
            g[v].append(u)
        dp={}

        def dfs(u):
            if u in dp:return dp[u]
            ans = 0
            for v in g[u]:
                ans = max(ans, dfs(v))
            dp[u]=ans + time[u - 1]
            return dp[u]

        return max(dfs(i) for i in range(1, n + 1))