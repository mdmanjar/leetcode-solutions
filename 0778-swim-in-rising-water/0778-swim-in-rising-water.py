class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        dir=(-1,0,1,0)
        n=len(grid)
        hp=[(grid[0][0],0,0)]
        grid[0][0]=-1
        ans=0

        while hp:
            d,i,j=heapq.heappop(hp)
            ans=max(d,ans)

            if (i,j)==(n-1,n-1):return ans

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]

                if -1<u<n and -1<v<n and grid[u][v]!=-1:
                    heapq.heappush(hp,(grid[u][v],u,v))
                    grid[u][v]=-1