class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)

        @lru_cache(m*n+2)
        def dfs(i,j):
            if i==m or j==n:return 0
            if text1[i]==text2[j]:
                return dfs(i+1,j+1)+1
            return max(dfs(i+1,j),dfs(i,j+1))
        return dfs(0,0)
        