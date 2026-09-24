class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n=len(edges)
        cycle=[0]*n
        ans=[0]*n

        def dfs(u):
            if ans[u]:
                return ans[u]

            if cycle[u]==1:
                length=0
                while cycle[u]==1:
                    length+=1
                    cycle[u]=2
                    u=edges[u]

                while ans[u]==0:
                    ans[u]=length
                    u=edges[u]

                return length

            cycle[u]=1
            x=dfs(edges[u])

            if cycle[u]==1:
                ans[u]=x+1
                cycle[u]=2
                return x+1

            ans[u]=x
            return x

        for i in range(n):
            if ans[i]==0:
                dfs(i)

        return ans