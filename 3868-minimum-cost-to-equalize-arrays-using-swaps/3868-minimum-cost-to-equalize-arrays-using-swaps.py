class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        mp=defaultdict(int)
        for a,b in zip(nums1,nums2):
            mp[a]+=1
            mp[b]-=1

        ans=0
        for v in mp.values():
            if v==0:continue
            if v&1:return -1
            if v>0:ans+=v//2
        return ans



        