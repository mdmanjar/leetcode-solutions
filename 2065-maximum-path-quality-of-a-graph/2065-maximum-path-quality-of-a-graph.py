class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        n=len(values)
        visit=[0]*n
        g=[[] for _ in range(n)]

        for u,v ,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))
        ans=0

        def dfs(u,sm,time):
            nonlocal ans
            if visit[u]==0:
                sm+=values[u]
            if u==0:ans=max(ans,sm)
            visit[u]+=1
            for v,t in g[u]:
                if time-t>=0:
                    dfs(v,sm,time-t)
            visit[u]-=1
        dfs(0,0,maxTime)
        return ans


        