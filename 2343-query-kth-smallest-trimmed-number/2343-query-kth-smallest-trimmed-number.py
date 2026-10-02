from itertools import accumulate

class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        n = len(nums[0])
        queries = sorted((trim, k, idx) for idx, (k, trim) in enumerate(queries))
        nums = [(e, i) for i, e in enumerate(nums)]

        ans = [0] * len(queries)

        def radix_sort(i):
            count = [0] * 10

            for e, _ in nums:
                count[ord(e[i]) - 48] += 1

            count = list(accumulate(count))
            temp = [None] * len(nums)

            for e, j in reversed(nums):
                x = ord(e[i]) - 48
                count[x] -= 1
                temp[count[x]] = (e, j)

            return temp

        idx = 0

        for i in range(n - 1, -1, -1):
            nums = radix_sort(i)
            trim = n - i

            while idx < len(queries) and queries[idx][0] == trim:
                _, k, qidx = queries[idx]
                ans[qidx] = nums[k - 1][1]
                idx += 1

        return ans