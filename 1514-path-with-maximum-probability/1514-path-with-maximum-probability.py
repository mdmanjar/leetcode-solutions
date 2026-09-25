class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        visited=[False]*n
        g=[[] for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            g[u].append((v,succProb[i]))
            g[v].append((u,succProb[i]))
        
        hp=[(1,start_node)]

        while hp:
            d,u=heapq.heappop_max(hp)

            if u==end_node:return d
            if visited[u]:continue
            visited[u]=True

            for v,w in g[u]:
                if visited[v]:continue
                nd=w*d
                heapq.heappush_max(hp,(nd,v))

        return 0