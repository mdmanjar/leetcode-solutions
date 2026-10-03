class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: list[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:

        if valueDiff < 0:
            return False

        mp = {}
        width = valueDiff + 1

        for i, x in enumerate(nums):

            b = x // width

            if b in mp:
                return True

            if b - 1 in mp and abs(x - mp[b - 1]) <= valueDiff:
                return True

            if b + 1 in mp and abs(x - mp[b + 1]) <= valueDiff:
                return True

            mp[b] = x

            if i >= indexDiff:
                old = nums[i - indexDiff]
                old_b = old // width
                del mp[old_b]

        return False