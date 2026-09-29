from collections import deque
from math import inf

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])

        if matrix[-1][-1] == '#':
            return -1

        mp = [[] for _ in range(26)]
        dist = [[inf] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if c != '#' and c != '.':
                    mp[ord(c) - 65].append((i, j))

        dr = (-1, 0, 1, 0)
        dc = (0, 1, 0, -1)

        q = deque([(0, 0)])
        dist[0][0] = 0

        used = [False] * 26

        while q:
            i, j = q.popleft()
            d = dist[i][j]

            if (i, j) == (m - 1, n - 1):
                return d

            c = matrix[i][j]

            # Teleport through this letter
            if c != '.' and not used[ord(c) - 65]:
                idx = ord(c) - 65
                used[idx] = True

                for u, v in mp[idx]:
                    if d < dist[u][v]:
                        dist[u][v] = d
                        q.appendleft((u, v))

            # Normal moves
            for k in range(4):
                u, v = i + dr[k], j + dc[k]

                if 0 <= u < m and 0 <= v < n and matrix[u][v] != '#':
                    if d + 1 < dist[u][v]:
                        dist[u][v] = d + 1
                        q.append((u, v))

        return -1



        