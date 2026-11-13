class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[[False]*10 for _ in range(10)]
        cols=[[False]*10 for _ in range(10)]
        boxes=[[False]*10 for _ in range(10)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    a=ord(board[i][j])-48
                    rows[i][a]=True
                    cols[j][a]=True
                    boxes[i//3*3+j//3][a]=True

        def dfs(i:int,j:int):
            if i==9:return True

            if j==9:return dfs(i+1,0)

            if board[i][j]!='.':return dfs(i,j+1)

            for n in range(1,10):
                if rows[i][n] or cols[j][n] or boxes[i//3*3+j//3][n]:
                    continue
                rows[i][n] = cols[j][n] = boxes[i//3*3+j//3][n]=True
                board[i][j]=str(n)
                if (dfs(i,j+1)):return True
                rows[i][n] = cols[j][n] = boxes[i//3*3+j//3][n]=False
                board[i][j]='.'
            return False


        dfs(0,0)



