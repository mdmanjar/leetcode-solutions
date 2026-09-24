class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g=[[] for _ in range(n)]

        for u,v in edges:
            g[u].append((v,0))
            g[v].append((u,1))

        ans=[0]*n
        count=[0]*n

        def post_order(u,p):
            for v,cost in g[u]:
                if v==p:continue
                post_order(v,u)
                count[u]+=count[v]+cost

        def pre_order(u,p):
            for v,cost in g[u]:
                if v==p:continue
                if cost==0:
                    ans[v]=ans[u]+1
                else:
                    ans[v]=ans[u]-1
                pre_order(v,u)

        post_order(0,-1)
        ans[0]=count[0]
        pre_order(0,-1)

        return ans