class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        currLen = 1
        prevLen = 0
        ans = 1

        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                currLen += 1
                ans = max(ans, currLen + prevLen)
            else:
                ans = max(ans, currLen + 1)

                if i + 1 < n and nums[i + 1] >= nums[i - 1]:
                    prevLen = currLen
                    currLen = 1

                elif i - 2 >= 0 and nums[i] >= nums[i - 2]:
                    prevLen = currLen
                    currLen = 1

                else:
                    prevLen = 1
                    currLen = 1

        return ans