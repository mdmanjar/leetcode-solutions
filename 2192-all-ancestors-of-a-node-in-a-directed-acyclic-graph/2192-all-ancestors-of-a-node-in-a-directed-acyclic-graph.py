class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        g=[[] for _ in range(n)]
        ancestors=[set() for _ in range(n)]

        deg=[0]*n

        for u,v in edges:
            g[u].append(v)
            deg[v]+=1
        q=deque(i for i in range(n) if deg[i]==0)

        while q:
            u=q.popleft()
            for v in g[u]:
                deg[v]-=1
                ancestors[v]|=ancestors[u]
                ancestors[v].add(u)
                if deg[v]==0:q.append(v)
        return [sorted(e) for e in ancestors]
        