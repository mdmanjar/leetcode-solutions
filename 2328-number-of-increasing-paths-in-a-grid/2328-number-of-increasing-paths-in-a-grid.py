class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        dir=(-1,0,1,0)
        m,n=len(grid),len(grid[0])
        deg=[[0]*n for _ in range(m)]
        path=[[1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for k in range(4):
                    u,v=dir[k]+i,j+dir[3-k]
                    if -1<u<m and -1<v<n and grid[i][j]<grid[u][v]:
                        deg[u][v]+=1

        q=deque((i,j) for i in range(m) for j in range(n) if deg[i][j]==0)
        ans=0
        mod=10**9+7

        while q:
            i,j=q.popleft()
            ans+=path[i][j]

            for k in range(4):
                u,v=dir[k]+i,dir[k-1]+j

                if -1<u<m and -1<v<n and grid[i][j]<grid[u][v]:
                    deg[u][v]-=1
                    path[u][v]=(path[i][j]+path[u][v])%mod
                    if deg[u][v]==0:q.append((u,v))
        return ans%mod

        