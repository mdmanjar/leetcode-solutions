class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        dir=(-1,0,1,0)
        q=deque([(0,0,k,0)])
        vis=[[-1]*n for _ in range(m)]
        vis[0][0]=k

        while q:
            i,j,ob,d=q.popleft()
            if (i,j)==(m-1,n-1):return d

            for x in range(4):
                u,v=i+dir[x],j+dir[3-x]
                if -1<u<m and -1<v<n:
                    nob=ob-grid[u][v]
                    if nob>=0 and nob>vis[u][v]:
                        vis[u][v]=nob
                        q.append((u,v,nob,d+1))

        return -1