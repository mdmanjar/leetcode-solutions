class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m=numRows
        n=len(s)
        ans=[[None]*n for _ in range(m)]

        if m==1:
            return s

        dirs=((1,0),(-1,1))
        idx=0
        i=j=k=0

        while k<len(s):
            ans[i][j]=s[k]
            k+=1

            u,v=dirs[idx]
            ni,nj=i+u,j+v

            if not (0<=ni<m and 0<=nj<n):
                idx=(idx+1)%2
                u,v=dirs[idx]
                ni,nj=i+u,j+v

            i,j=ni,nj

        return ''.join(
            ans[i][j]
            for i in range(m)
            for j in range(n)
            if ans[i][j] is not None
        )