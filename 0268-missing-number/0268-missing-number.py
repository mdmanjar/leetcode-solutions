class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        for i in range(n+1):
            total^=i

        for e in nums:
            total^=e
        return total
        