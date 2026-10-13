class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        g=[[] for _ in range(n)]

        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
        
        dist=[inf]*n
        ways=[0]*n
        ways[0]=1
        mod=10**9+7

        dist[0]=0

        hp=[(0,0)]

        while hp:
            d,u=heapq.heappop(hp)
            if d!=dist[u]:continue

            for v,w in g[u]:
                nd=w+d
                if nd<dist[v]:
                    dist[v]=nd
                    ways[v]=ways[u]
                    heapq.heappush(hp,(nd,v))
                elif nd==dist[v]:
                    ways[v]+=ways[u]
        return ways[-1]%mod

        