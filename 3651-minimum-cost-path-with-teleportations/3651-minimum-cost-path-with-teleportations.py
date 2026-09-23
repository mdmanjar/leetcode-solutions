from functools import cache

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        cells=sorted((grid[i][j],i,j) for i in range(m) for j in range(n))

        @cache
        def dfs(i,j,k):
            if (i,j)==(m-1,n-1):
                return 0

            ans=math.inf

            if i+1<m:
                ans=min(ans,grid[i+1][j]+dfs(i+1,j,k))

            if j+1<n:
                ans=min(ans,grid[i][j+1]+dfs(i,j+1,k))

            if k:
                for v,x,y in cells:
                    if v>grid[i][j]:
                        break
                    ans=min(ans,dfs(x,y,k-1))

            return ans

        return dfs(0,0,k)