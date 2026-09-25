class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if m == 1 and n == 1:
            return 0

        # Can't make the first move
        if (m > 1 and grid[1][0] > 1) and (n > 1 and grid[0][1] > 1):
            return -1

        hp = [(0, 0, 0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        dirs = (-1, 0, 1, 0)

        while hp:
            d, i, j = heapq.heappop(hp)

            if d != dist[i][j]:
                continue

            if (i, j) == (m - 1, n - 1):
                return d

            for k in range(4):
                u = i + dirs[k]
                v = j + dirs[k - 1]

                if not (0 <= u < m and 0 <= v < n):
                    continue

                nd = max(d + 1, grid[u][v])

                # Need correct parity because we can wait only
                # by moving back and forth.
                if (nd - (d + 1)) % 2:
                    nd += 1

                if nd < dist[u][v]:
                    dist[u][v] = nd
                    heapq.heappush(hp, (nd, u, v))

        return -1