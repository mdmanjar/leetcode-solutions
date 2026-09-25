class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        freq=Counter(cnt.values())

        for e in nums:
            if freq[cnt[e]]==1:
                return e
        
        return -1


            
        

        