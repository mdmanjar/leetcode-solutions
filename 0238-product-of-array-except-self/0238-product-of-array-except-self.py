class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[1]*n
        left=1

        for i,e in enumerate(nums):
            ans[i]*=left
            left*=e
        right=1

        for i,e in enumerate(nums[::-1]):
            ans[n-i-1]*=right
            right*=e

        return ans
        