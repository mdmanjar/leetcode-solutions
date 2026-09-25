class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dirs=((0,1),(0,-1),(1,0),(-1,0))
        dist=[[float('inf')]*n for _ in range(m)]
        q=[(0,0,0)]
        dist[0][0]=0

        while q:
            d,i,j=heapq.heappop(q)

            if (i,j)==(m-1,n-1):return d

            if d!=dist[i][j]:
                continue

            for k,(x,y) in enumerate(dirs,1):
                u,v=i+x,j+y
                if -1<u<m and -1<v<n:
                    nd=d+(grid[i][j]!=k)

                    if nd<dist[u][v]:
                        dist[u][v]=nd
                        heapq.heappush(q,(nd,u,v))

        return dist[m-1][n-1]