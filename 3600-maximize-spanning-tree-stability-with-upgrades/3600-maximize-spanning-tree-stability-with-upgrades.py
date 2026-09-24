
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        p = [-1] * n

        def find(x):
            if p[x] < 0:
                return x
            p[x] = find(p[x])
            return p[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return False

            if p[a] > p[b]:
                a, b = b, a

            p[a] += p[b]
            p[b] = a
            return True

        optional = []
        remaining = n - 1
        min_must = float('inf')

        for u, v, s, m in edges:
            if m:
                if not union(u,v): return -1
                remaining-=1
                min_must = min(min_must,s)
            else:
                optional.append((u, v, s))

        if remaining == 0:
            return min_must

        optional.sort(key=lambda x: x[2], reverse=True)

        chosen = []

        for u, v, s in optional:
            if union(u, v):
                chosen.append(s)
                remaining -= 1

                if remaining == 0:
                    break

        if remaining:
            return -1



        if k >= len(chosen):
            return min(min_must, 2 * chosen[-1])


        return min(
            min_must,
            2 * chosen[-1],
            chosen[-k - 1]
        )