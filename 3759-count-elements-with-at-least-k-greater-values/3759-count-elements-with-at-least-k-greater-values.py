class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        return sum(x < nums[n-k] for x in nums) if k else n
        