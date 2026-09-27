class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid=[[0]*m for _ in range(n)]
        sources.sort(key=lambda x:x[2],reverse=True)
        q=deque()
        
        for i,j,color in sources:
            grid[i][j]=color
            q.append((i,j,color))
        
        dir=(-1,0,1,0)
        while q:
            i,j,color=q.popleft()

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]
                if -1<u<n and -1<v<m and grid[u][v]==0:
                    grid[u][v]=color
                    q.append((u,v,color))
        return grid
        