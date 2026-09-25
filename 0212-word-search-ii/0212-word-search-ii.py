class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root={}

        def add(word):
            t=root

            for c in word:
                t=t.setdefault(c,{})

            t['#']=word
        
        for word in words:add(word)

        ans=[]
        m,n=len(board),len(board[0])
        dirs=(-1,0,1,0)

        def dfs(root,i,j):

            if '#' in root:
                ans.append(root['#'])
                del root['#']

            x=board[i][j]
            board[i][j]='#'

            for k in range(4):
                u,v=i+dirs[k],j+dirs[3-k]

                if -1<u<m and -1<v<n and board[u][v]!='#' and board[u][v] in root:
                    dfs(root[board[u][v]],u,v)

            board[i][j]=x
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(root[board[i][j]],i,j)
        
        return ans 
        