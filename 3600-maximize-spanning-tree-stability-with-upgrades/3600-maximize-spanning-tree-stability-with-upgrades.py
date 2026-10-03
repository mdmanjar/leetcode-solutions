
class dsu:

    def __init__(self, n):
        self.p = [-1] * n

    def union(self, a, b):
        a, b = self.find(a), self.find(b)

        if a == b:
            return False

        if self.p[a] > self.p[b]:
            a, b = b, a

        self.p[a] += self.p[b]
        self.p[b] = a

        return True

    def find(self, a):
        if self.p[a] < 0:
            return a

        self.p[a] = self.find(self.p[a])
        return self.p[a]


class Solution:

    def maxStability(
        self,
        n: int,
        edges: List[List[int]],
        k: int
    ) -> int:

        minimum_weight = math.inf
        optional = []
        must = []

        for u, v, s, m in edges:

            if m:
                must.append((u, v, s))
            else:
                optional.append((u, v, s))

        # Mandatory edges must form a forest.
        uf = dsu(n)

        for u, v, s in must:

            if not uf.union(u, v):
                return -1

            minimum_weight = min(minimum_weight, s)

        def can(mid):

            uf = dsu(n)

            # Mandatory edges must have stability >= mid.
            for u, v, s in must:

                if s < mid:
                    return False

                uf.union(u, v)

            used = 0

            # First use optional edges without doubling.
            for u, v, s in optional:

                if s < mid:
                    continue

                if uf.union(u, v):
                    used += 0

            # Then use optional edges with doubling.
            for u, v, s in optional:

                if s >= mid:
                    continue

                if s * 2 < mid:
                    continue

                if uf.union(u, v):
                    used += 1

                    if used > k:
                        return False

            # Check whether everything is connected.
            root = uf.find(0)

            for i in range(1, n):
                if uf.find(i) != root:
                    return False

            return True

        left = 0
        right = max(
            [s for _, _, s, _ in edges] +
            [s * 2 for _, _, s, m in edges if not m]
        )

        ans = -1

        while left <= right:

            mid = left + (right - left) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

        