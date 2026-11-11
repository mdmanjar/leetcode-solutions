class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1==text2:return len(text1)
        m,n=len(text1),len(text2)

        dp=[0]*(n+1)

        for i in range(1,m+1):
            temp=[0]*(n+1)

            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    temp[j]=dp[j-1]+1
                else:
                    temp[j]=max(dp[j],temp[j-1])
            dp=temp
        return dp[-1]

        