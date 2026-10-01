
class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dist=[[inf]*n for _ in range(m)]
        dir=(-1,0,1,0)
        q=deque([(0,0)])
        dist[0][0]=0

        while q:
            i,j=q.popleft()
            d=dist[i][j]

            for k in range(4):
                u,v=i+dir[k],j+dir[3-k]

                if not (-1<u<m and -1<v<n):continue
                new_d=max(d,grid[u][v])+1
                if new_d>=dist[u][v] or new_d>=dist[-1][-1]:continue
                if new_d==d+1:
                    q.appendleft((u,v))
                else:
                    q.append((u,v))
                dist[u][v]=new_d
        return dist[-1][-1]

        