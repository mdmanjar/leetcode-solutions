class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        left=0
        ans=inf
        sum=0

        for right,e in enumerate(nums):
            if e not in mp:sum+=e
            mp[e]+=1
            while sum>=k and left<=right:
                ans=min(ans,right-left+1)
                mp[nums[left]]-=1
                if mp[nums[left]]==0:
                    sum-=nums[left]
                    del mp[nums[left]]
                left+=1
        return -1 if ans==inf else ans

        