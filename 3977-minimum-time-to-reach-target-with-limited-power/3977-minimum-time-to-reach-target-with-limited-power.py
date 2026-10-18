class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        
        cost_sp, time, heap = [inf] * n, [inf] * n, [(0, 0, source)]
        cost_sp[source], time[source] = 0, 0
        while heap:
            t, d, u = heappop(heap)
            if d > power:
                continue
            
            if u == target:
                return [t, power-d]
            
            if d + cost[u] > power:
                continue
            
            for v, w in graph[u]:
                if d + cost[u] < cost_sp[v] or t + w < time[v]:
                    cost_sp[v], time[v] = d + cost[u], t + w
                    heappush(heap, (t + w, d + cost[u], v))

        return [-1, -1]