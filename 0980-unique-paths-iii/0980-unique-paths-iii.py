class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        must=0
        start=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:start=i*n+j
                elif grid[i][j]==0:must+=1
        ans=0

        def dfs(i,j,must):
            nonlocal ans
            if not (-1<i<m and -1<j<n and grid[i][j]!=-1):
                return
            if grid[i][j]==2:
                if must==0:ans+=1
                return
            grid[i][j]=-1
            for k in range(4):
                dfs(i+dir[k],j+dir[3-k],must-1)
            grid[i][j]=0

        dir=(-1,0,1,0)
        dfs(start//n,start%n,must+1)

        return ans
        