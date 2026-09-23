class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}

        for i,e in enumerate(nums):
            if target-e in mp:
                return [mp[target-e],i]
            mp[e]=i
        return [-1,-1]
        