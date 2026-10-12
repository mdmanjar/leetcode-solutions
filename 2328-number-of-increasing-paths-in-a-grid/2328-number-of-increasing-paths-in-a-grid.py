class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        dir=(-1,0,1,0)
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for _ in range(m)]
        mod=10**9+7

        def dfs(i,j,prev):
            if not (-1<i<m and -1<j<n and prev<grid[i][j]):return 0
            if dp[i][j]:return dp[i][j]
            ans=1
            for k in range(4): ans+=dfs(i+dir[k],j+dir[k-1],grid[i][j])
            dp[i][j]=ans%mod

            return ans%mod
        return sum(dfs(i,j,0) for i in range(m) for j in range(n))%mod
            

        