class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        # create a graph
        graph=[[] for _ in range(n)]

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        dt=[0]*n # current discovery time
        ldt=[0]*n # lowest discovery time
        vst=[False]*n # visit
        time=1
        ans=[]

        def dfs(u,p): # u: is a source and p: parent
            nonlocal time
            vst[u]=True
            ldt[u]=time
            dt[u]=time
            time+=1

            for v in graph[u]:
                if v==p:continue
                elif not vst[v]:
                    dfs(v,u)
                    
                    if ldt[v]>dt[u]:
                        ans.append([u,v])
                
                ldt[u]=min(ldt[u],ldt[v])
        dfs(0,-1)
        return ans

    
        