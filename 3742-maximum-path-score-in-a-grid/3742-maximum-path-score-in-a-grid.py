class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}

        def dfs(i, j, cost):
            if cost > k: return -float('inf')
            if (i, j) == (m - 1, n - 1): return grid[i][j]
            if (i, j, cost) in dp: return dp[(i, j, cost)]

            res = -float('inf')
            for x, y in ((0, 1), (1, 0)):
                u, v = i + x, j + y
                if u < m and v < n:
                    c = cost + (1 if grid[u][v] > 0 else 0)
                    res = max(res, grid[i][j] + dfs(u, v, c))

            dp[(i, j, cost)] = res
            return res

        start_cost = 1 if grid[0][0] > 0 else 0
        ans = dfs(0, 0, start_cost)
        return ans if ans != -float('inf') else -1