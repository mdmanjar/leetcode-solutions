class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str2==str1:return str1
        m,n=len(str1),len(str2)
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        i=m
        j=n
        ans=[]

        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                ans.append(str1[i-1])
                i-=1
            else:
                ans.append(str2[j-1])
                j-=1
        while i>0:
          ans.append(str1[i-1])
          i-=1
        while j>0:
          ans.append(str2[j-1])
          j-=1
        return ''.join(reversed(ans))