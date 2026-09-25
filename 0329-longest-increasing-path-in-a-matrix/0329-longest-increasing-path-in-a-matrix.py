class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        deg=[[0]*n for _ in range(m)]
        dirs=(-1,0,1,0)

        for i in range(m):
            for j in range(n):
                for k in range(4):
                    u,v=i+dirs[k],j+dirs[3-k]
                    if -1<u<m and -1<v<n and matrix[i][j]<matrix[u][v]:
                        deg[u][v]+=1
        
        q=deque((i,j,1) for i in range(m) for j in range(n) if deg[i][j]==0)
        ans=0

        while q:
            i,j,level=q.popleft()

            ans=max(level,ans)

            for k in range(4):
                u,v=i+dirs[k],j+dirs[3-k]
                if -1<u<m and -1<v<n and matrix[i][j]<matrix[u][v]:
                    deg[u][v]-=1

                    if deg[u][v]==0:
                        q.append((u,v,level+1))
        
        return ans

        