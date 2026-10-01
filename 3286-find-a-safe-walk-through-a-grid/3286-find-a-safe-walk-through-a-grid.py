class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n=len(grid),len(grid[0])
        dist=[0]*(m*n)
        q=deque([(health-grid[0][0],0,0)])
        dir=(-1,0,1,0)

        while q:
            health,i,j=q.popleft()

            if (i,j)==(m-1,n-1):return True
            if health<=dist[i*n+j]:
                continue
            dist[i*n+j]=health

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]
                if not (-1<u<m and -1<v<n):continue
                new_health=health-grid[u][v]
                if new_health>0:
                    if new_health==health:q.appendleft((new_health,u,v))
                    else:q.append((new_health,u,v))
        return False


        