class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        freq=defaultdict(int)
        for val in cnt.values():
            freq[val]+=1
        
        for e in nums:
            if freq[cnt[e]]==1:return e
        return -1
        