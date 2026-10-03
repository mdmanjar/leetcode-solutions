class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        if k == 0:
            return n

        x = nums[n - k]

        left = 0
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid

        return left