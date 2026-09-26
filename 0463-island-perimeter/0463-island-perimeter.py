class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        dirs=(-1,0,1,0)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:

                    for k in range(4):
                        u,v=i+dirs[k],j+dirs[k-1]
                        if not (-1<u<m and -1<v<n):
                            ans+=1
                            continue
                        if grid[u][v]==0:
                            ans+=1
                    grid[i][j]=-1
        return ans
    
        