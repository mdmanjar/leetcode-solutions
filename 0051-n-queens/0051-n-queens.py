class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid=[['.']*n for _ in range(n)]

        col=[False]*n
        pdig=[False]*(2*n)
        ndig=[False]*(2*n)
        ans=[]
        
        def dfs(i):
            if i==n:
                ans.append([''.join(row) for row in grid])
                return

            for j in range(n):
                if col[j] or pdig[i+j] or ndig[n+i-j]:continue
                col[j]=pdig[i+j]=ndig[n+i-j]=True
                grid[i][j]='Q'
                dfs(i+1)
                grid[i][j]='.'
                col[j]=pdig[i+j]=ndig[n+i-j]=False
        dfs(0)
        return ans
        