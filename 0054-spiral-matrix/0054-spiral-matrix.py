class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        dir=((0,1),(1,0),(0,-1),(-1,0))
        m,n=len(matrix),len(matrix[0])
        i=j=d=0
        ans=[]

        def next(i,j,d):
            a,b=i+dir[d][0],j+dir[d][1]
            if a<m and b<n and matrix[a][b]!=None:return a,b,d
            d=(d+1)%4
            return i+dir[d][0],j+dir[d][1],d
            

        while len(ans)<m*n:
            ans.append(matrix[i][j])
            matrix[i][j]=None
            i,j,d=next(i,j,d)

        return ans
    
        