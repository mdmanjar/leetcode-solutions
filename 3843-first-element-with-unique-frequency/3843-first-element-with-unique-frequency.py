class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        mp=Counter(nums)
        freq=Counter(mp.values())

        for e in nums:
            if freq[mp[e]]==1:return e
        return -1
        

        