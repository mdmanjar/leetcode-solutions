class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = [0] * n
        count = [0] * n

        def postorder(u, p):
            count[u] = 1

            for v in g[u]:
                if v == p:
                    continue

                postorder(v, u)

                count[u] += count[v]
                ans[u] += ans[v] + count[v]

        def preorder(u, p):
            for v in g[u]:
                if v == p:
                    continue

                ans[v] = ans[u] - count[v] + (n - count[v])

                preorder(v, u)

        postorder(0, -1)
        preorder(0, -1)

        return ans