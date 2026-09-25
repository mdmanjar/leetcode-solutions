class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @ lru_cache(None)
        def dfs(i,j):
            if len(s) - i < len(t) - j:
                return 0
            if j==len(t):return 1
            if i==len(s):return 0
            if s[i]!=t[j]:return dfs(i+1,j)
            else:return dfs(i+1,j+1)+dfs(i+1,j)
        return dfs(0,0)