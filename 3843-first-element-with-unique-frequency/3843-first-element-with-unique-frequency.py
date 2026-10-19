class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        mp=defaultdict(int)

        for e in nums:freq[e]+=1
        
        for val in freq.values():mp[val]+=1

        for e in nums:
            if mp[freq[e]]==1:return e
        return -1

            
        