class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        m,n=n,m
        grid=[[0]*n for _ in range(m)]
        sources.sort(key=lambda x:-x[2])
        q=deque()

        for i,j,color in sources:
            grid[i][j]=color
            q.append((i,j,color))
        dir=(-1,0,1,0)

        while q:
            i,j,color=q.popleft()
            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]
                if -1<u<m and -1<v<n and grid[u][v]==0:
                    grid[u][v]=color
                    q.append((u,v,color))
        return grid
        