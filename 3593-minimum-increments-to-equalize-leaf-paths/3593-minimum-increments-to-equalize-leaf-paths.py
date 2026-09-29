class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        tree = [[] for _ in range(n)]
        ans = 0

        def solve(root, p):
            nonlocal ans

            max_cost = 0
            count_max = 0
            count = 0

            for adj in tree[root]:
                if adj != p:
                    m = solve(adj, root)

                    if m > max_cost:
                        max_cost = m
                        count_max = 1
                    elif m == max_cost:
                        count_max += 1

                    count += 1

            ans += count - count_max

            return max_cost + cost[root]

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        solve(0, -1)

        return ans