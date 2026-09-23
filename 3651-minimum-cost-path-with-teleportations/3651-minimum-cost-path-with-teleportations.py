class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n,m=len(grid),len(grid[0])

        maxVal=0
        for row in grid:
            for v in row:
                maxVal=max(maxVal,v)

        dp=[[0]*m for _ in range(n)]
        bestVal=[math.inf]*(maxVal+1)
        prefix=[math.inf]*(maxVal+1)

        bestVal[grid[n-1][m-1]]=0

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:
                    continue

                down=dp[i+1][j]+grid[i+1][j] if i+1<n else math.inf
                right=dp[i][j+1]+grid[i][j+1] if j+1<m else math.inf

                dp[i][j]=min(down,right)
                bestVal[grid[i][j]]=min(bestVal[grid[i][j]],dp[i][j])

        for _ in range(k):
            prefix[0]=bestVal[0]

            for v in range(1,maxVal+1):
                prefix[v]=min(prefix[v-1],bestVal[v])

            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if i==n-1 and j==m-1:
                        continue

                    down=dp[i+1][j]+grid[i+1][j] if i+1<n else math.inf
                    right=dp[i][j+1]+grid[i][j+1] if j+1<m else math.inf

                    walk=min(down,right)

                    dp[i][j]=min(walk,prefix[grid[i][j]])
                    bestVal[grid[i][j]]=min(
                        bestVal[grid[i][j]],dp[i][j]
                    )

        return dp[0][0]