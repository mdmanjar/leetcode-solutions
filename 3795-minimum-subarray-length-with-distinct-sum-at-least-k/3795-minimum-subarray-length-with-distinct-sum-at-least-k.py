from collections import defaultdict
from typing import List

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = n + 1
        left = sm = 0
        freq = defaultdict(int)

        for right, e in enumerate(nums):
            sm += e
            freq[e] += 1

            # Resolve duplicates: shrink left until 'e' appears only once
            while freq[e] > 1:
                sm -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Shrink window while sum condition is met
            while sm >= k:
                ans = min(ans, right - left + 1)
                sm -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return ans if ans != n + 1 else -1