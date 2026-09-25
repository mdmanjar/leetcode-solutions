class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for _ in range(m)]

        dirs=(-1,0,1,0)

        def dfs(i,j,prev):
            if not (-1<i<m and -1<j<n and prev<grid[i][j]):return 0
            if dp[i][j]:return dp[i][j]
            dp[i][j]=sum(dfs(i+dirs[k],j+dirs[3-k],grid[i][j]) for k in range(4))+1
            return dp[i][j]%(10**9+7)

        return sum(dfs(i,j,0) for i in range(m) for j in range(n))%(10**9+7)

        