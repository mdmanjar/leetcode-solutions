class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        sources.sort(key=lambda x:x[2],reverse=True)
        m,n=n,m
        grid=[[0]*n for _ in range(m)]
        q=deque()

        dirs=(-1,0,1,0)


        for i,j,color in sources:
            q.append((i,j,color))
            grid[i][j]=color



        while q:
            sz=len(q)

            for _ in range(sz):
                i,j,color=q.popleft()

                for k in range(4):
                    u=i+dirs[k]
                    v=j+dirs[3-k]

                    if not (-1<u<m and -1<v<n and not grid[u][v]):
                        continue
                    grid[u][v]=color
                    q.append((u,v,color))
        return grid
            
        