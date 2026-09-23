class Solution:
    def minTimeMaxPower(self, n:int, edges:List[List[int]], power:int, cost:int, source:int, target:int):

        graph = [[] for _ in range(n)]

        for u, v, t in edges:
            graph[u].append((v, t))

        hp = [(0, -power, source)]

        max_power=[-1]*n

        while hp:
            curr_time, curr_power, node = heapq.heappop(hp)
            curr_power=-curr_power

            if node == target:
                return [curr_time, curr_power]
            if curr_power <= max_power[node]:
                continue

            max_power[node] = curr_power
            updated_power = curr_power - cost[node]

            for neighbour, time in graph[node]:
                if updated_power > max_power[neighbour]:
                    heapq.heappush(hp, (curr_time + time, -updated_power, neighbour))

        return [-1, -1]
        