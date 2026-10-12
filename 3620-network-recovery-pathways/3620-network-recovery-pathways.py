class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        if not edges:
            return -1

        n = len(online)
        g = [[] for _ in range(n)]
        deg=[0]*n
        min_w = inf
        max_w = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            min_w = min(min_w, w)
            max_w = max(max_w, w)
            g[u].append((v, w))
            deg[v]+=1
        q=deque(i for i in range(n) if deg[i]==0)
        topo=[]

        while q:
          u=q.popleft()
          topo.append(u)
          for v,_ in g[u]:
            deg[v]-=1
            if deg[v]==0:q.append(v)

        def check(limit: int) -> bool:
                    dist = [inf] * n
                    dist[0] = 0

                    for u in topo:
                        if dist[u] == inf:
                            continue
                        if u == n - 1:
                            break
                        d_u = dist[u]
                        for v, w in g[u]:
                            if w >= limit:
                                if d_u + w < dist[v]:
                                    dist[v] = d_u + w

                    return dist[n - 1] <= k

        left = min_w
        right = max_w

        # If even with the minimum possible edge weight requirement we can't reach n-1
        if not check(left):
            return -1

        ans = -1

        # Binary search for the maximum minimum-edge cost
        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid       # 'mid' is feasible, try to go higher
                left = mid + 1
            else:
                right = mid - 1 # 'mid' is too strict, try lower

        return ans