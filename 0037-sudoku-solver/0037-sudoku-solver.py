class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=[[False]*10 for _ in range(10)]
        col=[[False]*10 for _ in range(10)]
        box=[[False]*10 for _ in range(10)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    v=ord(board[i][j])-48
                    row[i][v]=col[j][v]=box[i//3*3+j//3][v]=True
        
        def dfs(i,j):
            if i==9:return True
            if j==9:return dfs(i+1,0)
            if board[i][j]!='.':return dfs(i,j+1)

            for k in range(1,10):
                if row[i][k] or col[j][k] or box[i//3*3+j//3][k]:
                    continue

                board[i][j]=str(k)

                row[i][k] = col[j][k] = box[i//3*3+j//3][k]=True

                if dfs(i,j+1):return True

                board[i][j]='.'

                row[i][k] = col[j][k] = box[i//3*3+j//3][k]=False

            return False

        dfs(0,0)


