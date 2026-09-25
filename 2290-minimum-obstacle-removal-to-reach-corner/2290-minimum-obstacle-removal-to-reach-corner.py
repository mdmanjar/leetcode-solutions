class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        q=deque([(0,0,grid[0][0])])
        dirs=(-1,0,1,0)
        grid[0][0]=-1

        while q:
            i,j,old_obstacle=q.popleft()

            if (i,j)==(m-1,n-1):return old_obstacle

            for k in range(4):
                u,v=i+dirs[k],j+dirs[3-k]
                if -1<u<m and -1<v<n and grid[u][v]!=-1:
                    new_obstacle=old_obstacle+grid[u][v]

                    if new_obstacle==old_obstacle:
                        q.appendleft((u,v,new_obstacle))
                    else:
                        q.append((u,v,new_obstacle))
                    grid[u][v]=-1




        