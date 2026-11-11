class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])

        row=[False]*n
        col=[False]*m

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[j]=True
                    col[i]=True
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    if row[j] or col[i]:
                        matrix[i][j]=0
