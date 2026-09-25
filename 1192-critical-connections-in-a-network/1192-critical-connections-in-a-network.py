class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        g=[[] for _ in range(n)]

        for u,v in connections:
            g[u].append(v)
            g[v].append(u)

        ldt=[0]*n
        dt=[0]*n
        time=1
        ans=[]

        def dfs(u,p):
            nonlocal time
            ldt[u]=dt[u]=time
            time+=1

            for v in g[u]:
                if v==p:continue

                if dt[v]==0:
                    dfs(v,u)
                    ldt[u]=min(ldt[u],ldt[v])
                    if ldt[v]>dt[u]:
                        ans.append([u,v])
                else:
                    ldt[u]=min(dt[v],ldt[u])

        dfs(0,-1)
        return ans


        