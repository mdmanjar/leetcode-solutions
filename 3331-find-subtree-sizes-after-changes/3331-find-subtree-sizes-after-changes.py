class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        tree = [[] for _ in range(n)]
        ans = [0] * n
        last = [-1] * 26

        for i in range(1, n):
            tree[parent[i]].append(i)

        def dfs(u):
            ans[u] = 1

            idx = ord(s[u]) - 97

            prev = last[idx]
            last[idx] = u

            for v in tree[u]:
                size = dfs(v)

                child_char = ord(s[v]) - 97
                attach = last[child_char]

                if attach == v:
                    attach = prev

                if attach == -1:
                    ans[u] += size
                else:
                    ans[attach] += size

            last[idx] = prev

            return ans[u]

        dfs(0)

        return ans