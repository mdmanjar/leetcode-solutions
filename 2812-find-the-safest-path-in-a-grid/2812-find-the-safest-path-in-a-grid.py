from collections import deque
from math import inf
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dirs = (-1, 0, 1, 0)
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = inf

        bucket = []
        while q:
            i, j = q.popleft()

            if len(bucket) == grid[i][j]:
                bucket.append([])
            bucket[grid[i][j]].append((i, j))

            for k in range(4):
                u = i + dirs[k]
                v = j + dirs[3 - k]

                if 0 <= u < m and 0 <= v < n and grid[u][v] == inf:
                    grid[u][v] = grid[i][j] + 1
                    q.append((u, v))

        p = [-1] * (m * n)
        active = [[False] * n for _ in range(m)]

        def find(x):
            if p[x] < 0:
                return x
            p[x] = find(p[x])
            return p[x]

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if p[a] > p[b]:
                a, b = b, a
            p[a] += p[b]
            p[b] = a

        TOP = 0
        BOTTOM = m * n - 1

        for val in range(len(bucket) - 1, -1, -1):
            for i, j in bucket[val]:
                active[i][j] = True

                for d in range(4):
                    ni = i + dirs[d]
                    nj = j + dirs[3 - d]

                    if 0 <= ni < m and 0 <= nj < n and active[ni][nj]:
                        union(i * n + j, ni * n + nj)

            if active[0][0] and active[m - 1][n - 1] and find(TOP) == find(BOTTOM):
                return val

        return 0