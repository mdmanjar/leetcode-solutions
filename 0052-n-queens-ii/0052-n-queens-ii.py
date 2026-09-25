class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        col=[False]*n
        pdig=[False]*(2*n)
        ndig=[False]*(2*n)
        ans=0

        def dfs(i):
            nonlocal ans
            if i==n:
                ans+=1
                return

            for j in range(n):
                if col[j] or pdig[i+j] or ndig[n+i-j]:continue
                col[j]=pdig[i+j]=ndig[n+i-j]=True
                dfs(i+1)
                col[j]=pdig[i+j]=ndig[n+i-j]=False
        dfs(0)
        return ans