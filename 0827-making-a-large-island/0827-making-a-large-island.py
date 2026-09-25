class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        colored=[0,0]

        def dfs(i,j,new_color):
            if not (-1<i<n and -1<j<n and grid[i][j]==1):return 0
            grid[i][j]=new_color
            return sum(dfs(i+dir[k],j+dir[3-k],new_color) for k in range(4))+1

        n=len(grid)
        dir=(-1,0,1,0)


        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    colored.append(dfs(i,j,len(colored)))
        
        if len(colored)==2:return 1
        if len(colored)==3 and colored[-1]==n*n:return n*n
        ans=1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    count=1
                    visited=set()
                    for k in range(4):
                        u,v=i+dir[k],j+dir[3-k]
                        if -1<u<n and -1<v<n and grid[u][v]!=0:
                            color=grid[u][v]
                            if color in visited:continue
                            visited.add(color)
                            count+=colored[color]
                    ans=max(ans,count)
       
        return ans



        
        