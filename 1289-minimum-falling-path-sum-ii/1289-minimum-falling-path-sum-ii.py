class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)
        dp=grid[-1]

        # for j in range(n):
        #     dp[j]=grid[n-1][j]

        for i in range(n-2,-1,-1):
            min1=-1
            min2=-1

            for j in range(n):
                if min1==-1 or dp[j]<dp[min1]:
                    min2=min1
                    min1=j
                elif min2==-1 or dp[j]<dp[min2]:
                    min2=j

            next=[0]*n

            for j in range(n):
                if j!=min1:
                    next[j]=grid[i][j]+dp[min1]
                else:
                    next[j]=grid[i][j]+dp[min2]

            dp=next

        return min(dp)