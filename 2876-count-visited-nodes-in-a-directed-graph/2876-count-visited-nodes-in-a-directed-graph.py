class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n=len(edges)
        ans=[0]*n
        visit=[0]*n

        def dfs(u):
            if visit[u]==2:return ans[u]

            if visit[u]==1:
                length=0

                while visit[u]==1:
                    length+=1
                    visit[u]=2
                    u=edges[u]

                return length

            visit[u]=1
            length=dfs(edges[u])
            if visit[u]==2:
                ans[u]=length
                return length
            ans[u]=length+1
            visit[u]=2
            return length+1
        
        for i in range(n):
            dfs(i)
        return ans
        