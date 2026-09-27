class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        ans=inf
        left=0
        mp=defaultdict(int)
        sm=0


        left=0

        for right,e in enumerate(nums):
            if e not in mp:
                sm+=e
            mp[e]+=1
            while sm>=k:
                ans=min(right-left+1,ans)
                x=nums[left]
                mp[x]-=1
                if mp[x]==0:
                    sm-=nums[left]
                    del mp[x]
                left+=1
            if ans==1:
                return ans

        return ans if ans!=inf else -1