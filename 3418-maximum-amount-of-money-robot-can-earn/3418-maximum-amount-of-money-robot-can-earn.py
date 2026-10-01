class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[None] * 3 for _ in range(n)] for _ in range(m)]

        def dfs(i, j, k):
            if i >= m or j >= n:
                return float('-inf')

            if dp[i][j][k] is not None:
                return dp[i][j][k]

            val = coins[i][j]

            if i == m - 1 and j == n - 1:
                if val < 0 and k > 0:
                    return 0
                return val

            # Take the coin normally
            ans = val + max(
                dfs(i + 1, j, k),
                dfs(i, j + 1, k)
            )

            # Neutralize a negative coin
            if val < 0 and k > 0:
                ans = max(
                    ans,
                    dfs(i + 1, j, k - 1),
                    dfs(i, j + 1, k - 1)
                )

            dp[i][j][k] = ans
            return ans

        return dfs(0, 0, 2)