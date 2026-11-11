class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans=-inf
        left=1

        for e in nums:
            left*=e
            ans=max(left,ans)
            if left==0:left=1

        left=1

        for e in nums[::-1]:
            left*=e
            ans=max(left,ans)
            if left==0:left=1
        return ans

        