class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n=len(online)
        g=[[] for _ in range(n)]
        deg=[0]*n
        left=math.inf
        right=0

        for u,v,w in edges:
            if online[u] and online[v]:
                g[u].append((v,w))
                deg[v]+=1
                left=min(left,w)
                right=max(right,w)

        def topo():
            q=deque(i for i in range(n) if deg[i]==0)
            arr=[]

            while q:
                u=q.popleft()
                arr.append(u)
                for v,_ in g[u]:
                    deg[v]-=1
                    if deg[v]==0:
                        q.append(v)

            return arr

        order=topo()

        def sort(limit):
            dist=[math.inf]*n
            dist[0]=0

            for u in order:
                if dist[u]==math.inf:
                    continue

                for v,w in g[u]:
                    if w>=limit:
                        dist[v]=min(dist[v],dist[u]+w)

            return dist[n-1]<=k

        ans=-1

        while left<=right:
            mid=(left+right)//2

            if sort(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1

        return ans