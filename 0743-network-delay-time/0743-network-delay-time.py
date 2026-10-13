class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        g=[[] for _ in range(n)]

        for u,v,w in times:
            g[u-1].append((v-1,w))

        q=deque([k-1])
        in_q=[False]*n
        dist=[inf]*n
        dist[k-1]=0

        while q:
            u=q.popleft()
            in_q[u]=False

            for v,w in g[u]:
                nd=w+dist[u]
                if nd<dist[v]:
                    dist[v]=nd
                    if not in_q[v]:
                        in_q[v]=True
                        q.append(v)
        x=max(dist)
        return x if x!=inf else -1
        