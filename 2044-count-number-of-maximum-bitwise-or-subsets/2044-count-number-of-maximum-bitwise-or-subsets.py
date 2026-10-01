class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        ans=0
        count=0

        def dfs(xor,i,c):
            nonlocal ans,count
            if i==len(nums):
                if c==0:return
                if xor>ans:
                    count=1
                    ans=xor
                elif xor==ans:count+=1
                return
            dfs(xor,i+1,c)
            dfs(xor|nums[i],i+1,c+1)
        dfs(0,0,0)
        return count

        