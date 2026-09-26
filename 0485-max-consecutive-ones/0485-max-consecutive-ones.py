class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        freq=0

        for e in nums:
            if not e:
                ans=max(ans,freq)
                freq=0
            else:
                freq+=1
            
        return max(ans,freq)
        