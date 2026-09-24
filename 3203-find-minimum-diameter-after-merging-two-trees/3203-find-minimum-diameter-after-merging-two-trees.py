class Solution:
    def minimumDiameterAfterMerge(
        self,
        edges1: List[List[int]],
        edges2: List[List[int]]
    ) -> int:

        def build_tree(edges):
            n = len(edges) + 1
            g = [[] for _ in range(n)]

            for u, v in edges:
                g[u].append(v)
                g[v].append(u)

            return g

        def diameter(g):
            n = len(g)

            if n <= 1:
                return 0

            deg = [len(x) for x in g]
            q = deque()

            for u in range(n):
                if deg[u] <= 1:
                    q.append(u)

            remaining = n
            layers = 0

            while remaining > 2:
                size = len(q)
                remaining -= size
                layers += 1

                for _ in range(size):
                    u = q.popleft()

                    for v in g[u]:
                        deg[v] -= 1

                        if deg[v] == 1:
                            q.append(v)

            # layers = radius for even diameter
            # If two centers remain, diameter = 2 * layers + 1
            if remaining == 1:
                return 2 * layers
            else:
                return 2 * layers + 1

        d1 = diameter(build_tree(edges1))
        d2 = diameter(build_tree(edges2))

        r1 = (d1 + 1) // 2
        r2 = (d2 + 1) // 2

        return max(d1, d2, r1 + r2 + 1)