class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        grid=[]
        temp=[['.']*n for _ in range(n)]
        rows=[False]*n
        x=[False]*(n*2)
        y=[False]*(n*2)


        def dfs(i:int):
            if i==n:
                grid.append([''.join(e) for e in temp])
                return
            for j in range(n):
                if rows[j] or x[i+j] or y[n+i-j]:
                    continue
                rows[j]=x[i+j]=y[n+i-j]=True
                temp[i][j]='Q'
                dfs(i+1)
                rows[j]=x[i+j]=y[n+i-j]=False
                temp[i][j]='.'
        dfs(0)
        return grid
        