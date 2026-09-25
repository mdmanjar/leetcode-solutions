class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        g=[[] for _ in range(n)]
        deg=[0]*n
        for u,v in relations:
            g[v-1].append(u-1)
            deg[u-1]+=1
        x=[0]*n
        q=deque()
        for i in range(n):
            if deg[i]==0:
                # x[i]=time[i]
                q.append(i)

        ans=0
        while q:
            u=q.popleft()
            ans=max(x[u]+time[u],ans)
            for v in g[u]:
                deg[v]-=1
                x[v]=max(x[v],x[u]+time[u])
                if deg[v]==0:q.append(v)
        return ans

        