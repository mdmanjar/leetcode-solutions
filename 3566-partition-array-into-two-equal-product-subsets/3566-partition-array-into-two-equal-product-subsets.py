class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        pro = 1

        for e in nums:
            pro *= e

        if pro != target * target:
            return False

        n = len(nums)
        used = [False] * n

        def dfs(pro):
            if pro == 1:
                return True

            for i, e in enumerate(nums):
                if used[i] or pro % e != 0:
                    continue

                used[i] = True

                if dfs(pro // e):
                    return True

                used[i] = False

            return False

        return dfs(target)