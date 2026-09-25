class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dst: int) -> int:
        g=[[] for _ in range(n)]
        rg=[[] for _ in range(n)]


        for u,v,w in edges:
            g[u].append((v,w))
            rg[v].append((u,w))
        
        def dijkstra(src,g):
            dist=[inf]*n
            hp=[(0,src)]
            dist[src]=0

            while hp:
                d,u=heapq.heappop(hp)
                if d!=dist[u]:continue
                for v,w in g[u]:
                    nd=d+w
                    if nd<dist[v]:
                        dist[v]=nd
                        heapq.heappush(hp,(nd,v))
            return dist
        d1=dijkstra(src1,g)
        if d1[dst]==inf:return -1
        d2=dijkstra(src2,g)
        if d2[dst]==inf:return -1
        d3=dijkstra(dst,rg)
        ans=inf

        for i in range(n):
            if inf not in (d1[i],d2[i],d3[i]):
                ans=min(d1[i]+d2[i]+d3[i],ans)
        return ans 



        