class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g=[[] for _ in range(n)]

        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))
        
        def dijkstra(src):
            dist=[inf]*n
            dist[src]=0
            hp=[(0,src)]

            while hp:
                d,u=heapq.heappop(hp)
                if d!=dist[u]:continue

                for v,w in g[u]:
                    nd=w+d
                    if nd<dist[v]:
                        dist[v]=nd
                        heapq.heappush(hp,(nd,v))
            return dist
        d1=dijkstra(0)
        d2=dijkstra(n-1)
        sp=d1[-1]

        ans=[False]*len(edges)
        for i,(u,v,w) in enumerate(edges):
            if inf in (d1[u],d2[v]) or inf in (d1[v],d2[u]):
                continue
            if d1[u]+d2[v]+w==sp or d1[v]+d2[u]+w==sp:
                ans[i]=True
        return ans
        