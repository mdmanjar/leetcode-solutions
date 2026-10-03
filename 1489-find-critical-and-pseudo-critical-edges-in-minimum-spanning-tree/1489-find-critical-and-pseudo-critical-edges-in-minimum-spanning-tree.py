
class dsu:

    def __init__(self, n):
        self.p = [-1] * n

    def find(self, a):
        if self.p[a] < 0:
            return a

        self.p[a] = self.find(self.p[a])
        return self.p[a]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)

        if a == b:
            return False

        if self.p[a] > self.p[b]:
            a, b = b, a

        self.p[a] += self.p[b]
        self.p[b] = a

        return True


class Solution:

    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: list[list[int]]
    ) -> list[list[int]]:

        edges = [
            [u, v, w, i]
            for i, (u, v, w) in enumerate(edges)
        ]

        edges.sort(key=lambda x: x[2])

        def mst(skip=-1, force=-1):

            uf = dsu(n)
            weight = 0
            count = 0

            # Force this edge first
            if force != -1:
                u, v, w, _ = edges[force]

                uf.union(u, v)
                weight += w
                count += 1

            for i, (u, v, w, _) in enumerate(edges):

                if i == skip or i == force:
                    continue

                if uf.union(u, v):
                    weight += w
                    count += 1

                    if count == n - 1:
                        break

            if count != n - 1:
                return math.inf

            return weight

        base = mst()

        critical = []
        pseudo = []

        for i in range(len(edges)):

            # If removing this edge increases MST weight,
            # it is critical.
            if mst(skip=i) > base:
                critical.append(edges[i][3])

            # Otherwise, if forcing it still gives the same MST,
            # it is pseudo-critical.
            elif mst(force=i) == base:
                pseudo.append(edges[i][3])

        return [critical, pseudo]


