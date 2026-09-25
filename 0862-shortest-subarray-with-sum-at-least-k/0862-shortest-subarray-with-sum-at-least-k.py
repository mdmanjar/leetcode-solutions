from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = n + 1

        prefix = list(accumulate(nums,initial=0))

        q = deque()

        for i in range(n + 1):
            while q and prefix[i] - prefix[q[0]] >= k:
                res = min(res, i - q.popleft())

            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()

            q.append(i)

        return res if res <= n else -1
        