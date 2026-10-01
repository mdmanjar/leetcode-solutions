class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        dist=[[inf]*n for _ in range(m)]
        dist[0][0]=0
        hp=[((0,0,0,0))]
        dir=(-1,0,1,0)

        while hp:
            d,i,j,a=heapq.heappop(hp)

            if (i,j)==(m-1,n-1):return d

            if d!=dist[i][j]:continue

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]

                if not (-1<u<m and -1<v<n):continue
                new_d=max(d,grid[u][v])+(2 if a else 1)
                new_a=not a

                if new_d<dist[u][v]:
                    dist[u][v]=new_d
                    heapq.heappush(hp,(new_d,u,v,new_a))
        