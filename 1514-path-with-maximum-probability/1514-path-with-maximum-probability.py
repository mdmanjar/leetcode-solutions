class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:

        g=[[] for _ in range(n)]

        for (u,v),p in zip(edges,succProb):
            g[u].append((v,p))
            g[v].append((u,p))

        visit=[False]*n
        hp=[(1,start)]

        while hp:
            p,u=heapq.heappop_max(hp)
            if u==end:return p
            if visit[u]:continue

            visit[u]=True

            for v,w in g[u]:
                np=p*w
                heapq.heappush_max(hp,(np,v))
        return 0