class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}

        for num in nums:
            points[num] = points.get(num, 0) + num

        values = sorted(points)

        prev = None
        take = skip = 0

        for num in values:
            if prev == num - 1:
                take, skip = skip + points[num], max(take, skip)
            else:
                take, skip = max(take, skip) + points[num], max(take, skip)

            prev = num

        return max(take, skip)