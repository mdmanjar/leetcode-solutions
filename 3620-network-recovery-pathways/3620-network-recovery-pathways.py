import heapq
from math import inf
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        if not edges:
            return -1
        
        n = len(online)
        g = [[] for _ in range(n)]
        min_w = inf
        max_w = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            min_w = min(min_w, w)
            max_w = max(max_w, w)
            g[u].append((v, w))
        
        def dijkstra(limit):
            dist = [inf] * n
            dist[0] = 0
            hp = [(0, 0)]

            while hp:
                d, u = heapq.heappop(hp)
                
                if u == n - 1:
                    return True
                
                if d > dist[u]:
                    continue
                
                for v, w in g[u]:
                    if w < limit:  # Discard edges lighter than our minimum threshold
                        continue
                    new_d = d + w
                    if new_d < dist[v] and new_d <= k:
                        dist[v] = new_d
                        heapq.heappush(hp, (new_d, v))
            
            return False

        left = min_w
        right = max_w

        # If even with the minimum possible edge weight requirement we can't reach n-1
        if not dijkstra(left):
            return -1

        ans = -1

        # Binary search for the maximum minimum-edge cost
        while left <= right:
            mid = (left + right) // 2

            if dijkstra(mid):
                ans = mid       # 'mid' is feasible, try to go higher
                left = mid + 1
            else:
                right = mid - 1 # 'mid' is too strict, try lower
                
        return ans