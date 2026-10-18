import heapq
import math
from typing import List

class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        if source == target:
            return [0, power]
            
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
            
        # dist[u] will store a list/dict of (time, power) states we've seen at node u
        # To avoid exponential blowup, we only keep states that are Pareto-optimal 
        # (better or equal time, and better or equal power).
        # Alternatively, a full 2D table if power is small:
        
        # Since power <= 58 in this test case, a 2D array works great:
        # best_time[u][p] = minimum time to reach node u with remaining power p
        best_time = [[math.inf] * (power + 1) for _ in range(n)]
        
        # Priority queue: (time, -power, node)
        hp = [(0, -power, source)]
        best_time[source][power] = 0
        
        ans_t = math.inf
        ans_p = -1
        
        while hp:
            t, neg_p, u = heapq.heappop(hp)
            p = -neg_p
            
            # If we've already found a strictly better time to reach target with >= power, we can prune
            if t > ans_t:
                continue
                
            if u == target:
                if t < ans_t:
                    ans_t = t
                    ans_p = p
                elif t == ans_t:
                    ans_p = max(ans_p, p)
                continue
                
            # If we've found a way to reach u with less time and >= power, skip this state
            if t > best_time[u][p]:
                continue
                
            # Check if we have enough power to leave node u
            if p < cost[u]:
                continue
                
            new_p = p - cost[u]
            
            for v, weight in g[u]:
                new_t = t + weight
                # Only push if this path improves the time for state (v, new_p)
                if new_t < best_time[v][new_p]:
                    best_time[v][new_p] = new_t
                    heapq.heappush(hp, (new_t, -new_p, v))
                    
        return [ans_t, ans_p] if ans_t != math.inf else [-1, -1]