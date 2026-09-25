class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        path=[[1]*n for _ in range(m)]
        deg=[[0]*n for _ in range(m)]
        dir=(-1,0,1,0)
        mod=10**9+7

        for i in range(m):
            for j in range(n):
                for k in range(4):
                    u,v=i+dir[k],j+dir[3-k]
                    if -1<u<m and -1<v<n and grid[i][j]<grid[u][v]:
                        deg[u][v]+=1
        
        q=deque((i,j) for i in range(m) for j in range(n) if deg[i][j]==0)
        ans=0
        while q:
            i,j=q.popleft()
            ans+=path[i][j]

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]
                if -1<u<m and -1<v<n and grid[i][j]<grid[u][v]:
                    path[u][v]=(path[i][j]+path[u][v])%mod
                    deg[u][v]-=1
                    if deg[u][v]==0:
                        q.append((u,v))
        return ans%mod

    

        