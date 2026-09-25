class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)

        lp = [1] * n
        deg = [0] * n

        for i in range(1, n):
            deg[parent[i]] += 1

        q = deque()

        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        ans = 1

        while q:
            u = q.popleft()
            
            if u==0:continue

            if s[u] != s[parent[u]]:
                ans = max(ans, lp[u] + lp[parent[u]])
                lp[parent[u]] = max(lp[parent[u]], lp[u] + 1)

            deg[parent[u]] -= 1
            
            if deg[parent[u]] == 0:
                q.append(parent[u])

        return ans
