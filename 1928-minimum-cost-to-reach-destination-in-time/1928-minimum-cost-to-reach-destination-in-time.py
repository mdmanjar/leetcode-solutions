
import heapq
from typing import List

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFee: List[int]) -> int:
        n = len(passingFee)
        
        g = [[] for _ in range(n)]

        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))
        
        # Track the minimum time to reach each node (instead of minimum fee)
        min_time = [inf] * n

        # hp stores: (current_fee, current_time, current_node)
        hp = [(passingFee[0], 0, 0)]
        
        while hp:
            fee, time, u = heapq.heappop(hp)
            
            # Prune: If we've already reached this node earlier with a cheaper fee 
            # AND a faster/equal time, this current path is strictly worse. Discard it.
            if time >= min_time[u]:
                continue
                
            # Update the best time to reach this node
            min_time[u] = time
            
            # Since hp prioritizes lowest fee, the first time we pop the target, it's the minimum cost.
            if u == n - 1:
                return fee

            for nei, nei_time in g[u]:
                nxt_time = time + nei_time
                
                # Only push if it doesn't exceed maxTime
                if nxt_time <= maxTime:
                    heapq.heappush(hp, (fee + passingFee[nei], nxt_time, nei))
        
        return -1
    