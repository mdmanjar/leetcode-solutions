class dsu:
    def __init__(self, n: int):
        self.p = [-1] * n

    def find(self, u: int) -> int:
        if self.p[u] < 0:
            return u
        self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.p[a] > self.p[b]:
            a, b = b, a
        self.p[a] += self.p[b]
        self.p[b] = a
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        critical_edges = []
        pseudo_critical_edges = []

        # Store original index alongside (u, v, w) before sorting by weight
        sorted_edges = sorted([(u, v, w, idx) for idx, (u, v, w) in enumerate(edges)], key=lambda x: x[2])

        def mst(must_idx=None, ignore_idx=None):
            uf = dsu(n)
            count = 0
            weight = 0

            if must_idx is not None:
                u, v, w, _ = sorted_edges[must_idx]
                weight += w
                uf.union(u, v)
                count += 1

            for i, (u, v, w, _) in enumerate(sorted_edges):
                if i == must_idx or i == ignore_idx:
                    continue
                if uf.union(u, v):
                    count += 1
                    weight += w

            return weight if count == n - 1 else float('inf')

        min_weight = mst()

        for i, (_, _, _, orig_idx) in enumerate(sorted_edges):
            if mst(ignore_idx=i) > min_weight:
                critical_edges.append(orig_idx)
            elif mst(must_idx=i) == min_weight:
                pseudo_critical_edges.append(orig_idx)

        return [critical_edges, pseudo_critical_edges]