class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = y = z = float('-inf')

        for e in nums:
            if e > x:
                z, y, x = y, x, e
            elif x > e > y:
                z, y = y, e
            elif y > e > z:
                z = e

        return z if z != float('-inf') else x