class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        parent = list(range(len(vals)))
        count = [1] * len(vals)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            nonlocal ans

            a, b = find(a), find(b)

            if a == b:
                return

            if vals[a] == vals[b]:
                ans += count[a] * count[b]
                count[a] += count[b]
                parent[b] = a

            elif vals[a] > vals[b]:
                parent[b] = a
            else:
                parent[a] = b

        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))

        ans = len(vals)

        for u, v in edges:
            union(u, v)

        return ans