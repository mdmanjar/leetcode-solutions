class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        deg = [0] * n
        graph = [set() for _ in range(n)]

        for u, v in edges:
            u -= 1
            v -= 1

            deg[u] += 1
            deg[v] += 1

            graph[u].add(v)
            graph[v].add(u)

        odd = [i for i in range(n) if deg[i] % 2]

        if len(odd) == 0:
            return True

        if len(odd) == 2:
            a, b = odd

            # Add edge directly between the two odd vertices
            if b not in graph[a]:
                return True

            # Or use an intermediate even-degree vertex
            for i in range(n):
                if deg[i] % 2 == 0:
                    if i not in graph[a] and i not in graph[b]:
                        return True

            return False

        if len(odd) == 4:
            # Pair the four odd vertices in all 3 possible ways.
            a, b, c, d = odd

            def can_add(x, y):
                return y not in graph[x]

            return (
                can_add(a, b) and can_add(c, d)
                or can_add(a, c) and can_add(b, d)
                or can_add(a, d) and can_add(b, c)
            )

        return False