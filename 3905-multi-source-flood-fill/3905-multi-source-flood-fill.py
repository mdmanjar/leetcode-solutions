class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key=lambda x:x[2],reverse=True)
        m,n=n,m
        grid=[[0]*n for _ in range(m)]
        q=deque()
        for i,j,c in sources:
            if grid[i][j]==0:
                grid[i][j]=c
            q.append((i,j,c))
        
        dir=(-1,0,1,0)
        
        while q:
            i,j,c=q.popleft()

            for k in range(4):
                u,v=i+dir[k],j+dir[k-1]

                if -1<u<m and -1<v<n and grid[u][v]==0:
                    grid[u][v]=c
                    q.append((u,v,c))
        


        return grid
        