class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        ans=[[1],[1,1]]

        for i in range(2,n):
            ans.append([1]*(i+1))
            for j in range(1,i):
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans
        