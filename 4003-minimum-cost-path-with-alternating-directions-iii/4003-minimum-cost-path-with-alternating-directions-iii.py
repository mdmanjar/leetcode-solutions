class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        INF = float('inf')
        dist = [[INF] * 2 for _ in range(m * n)]

        # parity: 0 = even, 1 = odd
        dist[0][1] = 1

        heap = [(1, 1, 0)]

        directions = [
            (0, 1),   # right
            (1, 0),   # down
            (0, -1),  # left
            (-1, 0)   # up
        ]

        while heap:
            cost, parity, idx = heapq.heappop(heap)

            if cost != dist[idx][parity]:
                continue

            if idx == m * n - 1:
                return cost

            i, j = divmod(idx, n)
            pen = penalty[i][j]

            # Wait
            new_parity = parity ^ 1
            new_cost = cost + pen

            if new_cost < dist[idx][new_parity]:
                dist[idx][new_parity] = new_cost
                heapq.heappush(
                    heap,
                    (new_cost, new_parity, idx)
                )

            # Move
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue

                new_idx = ni * n + nj

                # Moving cost = destination cell cost
                new_cost = cost + (ni + 1) * (nj + 1)

                # Odd parity prefers right/down.
                # Even parity prefers left/up.
                is_right_down = di + dj > 0

                if parity == 1 and not is_right_down:
                    new_cost += pen

                if parity == 0 and is_right_down:
                    new_cost += pen

                new_parity = parity ^ 1

                if new_cost < dist[new_idx][new_parity]:
                    dist[new_idx][new_parity] = new_cost
                    heapq.heappush(
                        heap,
                        (new_cost, new_parity, new_idx)
                    )

        return -1