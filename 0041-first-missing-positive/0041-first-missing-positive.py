class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        mp=set()

        for e in nums:
            if e>0 and e<=len(nums):
                mp.add(e)
        
        for i in range(1,len(nums)+1):
            if i not in mp:
                return i
        return len(nums)+1