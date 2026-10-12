class Solution:
    def longestCycle(self, edges: list[int]) -> int:
        n=len(edges)
        visit=[0]*n
        ans=-1

        def dfs(u):
            nonlocal ans

            if visit[u]==2:return
            if visit[u]==1:
                length=0
                while visit[u]==1:
                    length+=1
                    visit[u]=2
                    u=edges[u]
                ans=max(ans,length)
                return
            if edges[u]==-1:return
            visit[u]=1
            dfs(edges[u])
            visit[u]=2
        for i in range(n):dfs(i)
        return ans

            
        