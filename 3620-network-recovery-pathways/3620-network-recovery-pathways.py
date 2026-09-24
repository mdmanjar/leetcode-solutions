class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n=len(online)

        g=[[] for _ in range(n)]
        right=0
        left=math.inf
        for u,v,w in edges:
            if not (online[u] and online[v]):continue
            g[u].append((v,w))
            right=max(right,w)
            left=min(left,w)

        # def topo_sort():
        #     deg=[0]*n

        #     for i in range(n):
        #         for v,_ in g[i]:
        #             deg[v]+=1
        #     q=deque(i for i in range(n) if deg[i]==0)
        #     ans=[]

        #     while q:
        #         u=q.popleft()
        #         ans.append(u)
        #         for v,_ in g[u]:
        #             deg[v]-=1
        #             if deg[v]==0:
        #                 q.append(v)
        #     return ans

        # arr=topo_sort()

        def sort(limit):
            dist=[inf]*n
            dist[0]=0
            hp=[(0,0)]

            while hp:
                d,u=heapq.heappop(hp)
                if u==n-1:return True
                if d!=dist[u]:continue

                for v,w in g[u]:
                    nd=w+d
                    if w>=limit and nd<dist[v] and nd<=k:
                        dist[v]=nd
                        heapq.heappush(hp,(nd,v))
            return False
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if sort(mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans
            

            
        